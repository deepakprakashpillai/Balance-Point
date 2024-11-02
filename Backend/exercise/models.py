from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Exercise(models.Model):
    EXERCISE_TYPE_CHOICES = [
        ('cardio', 'Cardio'),
        ('weightlifting', 'Weightlifting'),
        ('sports', 'Sports'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=15, choices=EXERCISE_TYPE_CHOICES)
    
    class Meta:
        verbose_name = ("Exercise")
        verbose_name_plural = ("Exercises")

    def __str__(self):
        return self.name
    
    
class WorkoutSession(models.Model):
    FEELING_CHOICES = [
        ('happy', 'Happy'),
        ('calm', 'Calm'),
        ('tired', 'Tired'),
        ('stressed', 'Stressed'),
        ('energized', 'Energized'),
        ('unhappy', 'Unhappy'),
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    feelings = models.CharField(max_length=15,choices=FEELING_CHOICES)
    total_duration = models.IntegerField(default=0)
    

    class Meta:
        verbose_name = ("Workout Session")
        verbose_name_plural = ("Workout Sessions")

    def __str__(self):
        return str(self.date)
    
    
class WorkoutExercise(models.Model):
    INTENSITY_CHOICES = [
        ('low','Low'),
        ('medium','Medium'),
        ('high','High')
    ]

    workout_session = models.ForeignKey(WorkoutSession,on_delete=models.CASCADE,related_name='workout_exercises')
    exercise = models.ForeignKey(Exercise,on_delete=models.CASCADE)
    intensity = models.CharField(max_length=15,choices = INTENSITY_CHOICES)
    duration = models.IntegerField(blank=True,null=True)
    
    sets = models.IntegerField(null=True, blank=True) # make sure to validate in frontend for weighlifting
    reps = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True,null=True)
    
    distance = models.FloatField(blank=True,null=True)
    

    class Meta:
        verbose_name = ("Workout Exercise")
        verbose_name_plural = ("Workout Exercises")

    def __str__(self):
        return f"{self.exercise} on {self.workout_session}"



