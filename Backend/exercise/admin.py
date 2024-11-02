from django.contrib import admin
from .models import Exercise,WorkoutExercise,WorkoutSession
# Register your models here.
admin.site.register(Exercise)
admin.site.register(WorkoutSession)
admin.site.register(WorkoutExercise)