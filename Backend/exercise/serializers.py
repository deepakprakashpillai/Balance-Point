from rest_framework import serializers
from .models import Exercise, WorkoutExercise, WorkoutSession

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class WorkoutExerciseSerializer(serializers.ModelSerializer):
    exercise = serializers.PrimaryKeyRelatedField(queryset = Exercise.objects.all())
    class Meta:
        model = WorkoutExercise
        fields = ['id', 'workout_session', 'exercise', 'intensity', 'duration', 'sets', 'reps', 'weight', 'distance']
        extra_kwargs = {'workout_session': {'required': False}}
        
    def to_representation(self, instance):
        repr =  super().to_representation(instance)
        repr['exercise'] = ExerciseSerializer(instance.exercise).data
        return repr

class WorkoutSessionSerializer(serializers.ModelSerializer):
    workout_exercises = WorkoutExerciseSerializer(many=True)

    class Meta: 
        model = WorkoutSession
        fields = ['id', 'user', 'date', 'feelings', 'total_duration', 'workout_exercises'] 

    def create(self, validated_data):
        workout_exercises_data = validated_data.pop('workout_exercises')
        workout_session = WorkoutSession.objects.create(**validated_data)
        
        for exercise_data in workout_exercises_data:
            WorkoutExercise.objects.create(workout_session=workout_session, **exercise_data)
         
        return workout_session
    
    def update(self, instance, validated_data):
        # Update basic fields of the WorkoutSession
        instance.date = validated_data.get('date', instance.date)
        instance.feelings = validated_data.get('feelings', instance.feelings)
        instance.total_duration = validated_data.get('total_duration', instance.total_duration)
        instance.save()
    
        # Retrieve workout exercises data
        workout_exercises_data = validated_data.pop('workout_exercises', [])
        current_exercises = {exercise.id: exercise for exercise in instance.workout_exercises.all()}
        updated_exercise_ids = [exercise_data.get('id') for exercise_data in workout_exercises_data if 'id' in exercise_data]
    
        # Update existing exercises and create new ones
        for exercise_data in workout_exercises_data:
            exercise_id = exercise_data.get('id')
    
            if exercise_id and exercise_id in current_exercises:
                # Update existing WorkoutExercise
                exercise_instance = current_exercises[exercise_id]
                for attr, value in exercise_data.items():
                    setattr(exercise_instance, attr, value)
                exercise_instance.save()
            else:
                # Remove workout_session key from exercise_data if it exists to avoid duplication
                exercise_data.pop('workout_session', None)
                # Create a new WorkoutExercise
                WorkoutExercise.objects.create(workout_session=instance, **exercise_data)
    
        # Delete exercises that are not in the updated data
        for exercise_id, exercise_instance in current_exercises.items():
            if exercise_id not in updated_exercise_ids:
                exercise_instance.delete()
    
        return instance


