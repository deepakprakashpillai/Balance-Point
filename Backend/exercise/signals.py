from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import WorkoutExercise, WorkoutSession

@receiver(post_save, sender=WorkoutExercise) 
def update_workout_session_total_duration_on_save(sender, instance, **kwargs): 
    workout_session = instance.workout_session 
    workout_session.total_duration = sum(
        exercise.duration for exercise in workout_session.workout_exercises.all() if exercise.duration is not None
    )
    workout_session.save()

@receiver(post_delete, sender=WorkoutExercise)
def update_workout_session_total_duration_on_delete(sender, instance, **kwargs):
    workout_session = instance.workout_session
    workout_session.total_duration = sum(
        exercise.duration for exercise in workout_session.workout_exercises.all() if exercise.duration is not None
    ) 
    workout_session.save()
