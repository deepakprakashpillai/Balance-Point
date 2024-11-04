from django.db import models
from django.contrib.auth import get_user_model
from multiselectfield import MultiSelectField  # Make sure to install this package

User = get_user_model()

class DiaryLog(models.Model):
    MOOD_CHOICES = [
        ("productive", "Productive"),
        ("energetic", "Energetic"),
        ("happy", "Happy"),
        ("motivated", "Motivated"),
        ("content", "Content"),
        ("relaxed", "Relaxed"),
        ("accomplished", "Accomplished"),
        ("tired", "Tired"),
        ("stressed", "Stressed"),
        ("anxious", "Anxious"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='diary_logs', null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    mood_descriptors = MultiSelectField(choices=MOOD_CHOICES)  
    emotional_rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])

