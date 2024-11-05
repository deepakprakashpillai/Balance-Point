from pyexpat import model
from django.db import models
from django.contrib.auth import get_user_model
from multiselectfield import MultiSelectField  

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



class News(models.Model):
    title=models.CharField(max_length=156)
    content=models.TextField(max_length=256)
    image=models.CharField(max_length=256,null=True)
    date_published=models.DateTimeField(auto_now_add=True)
    is_published=models.BooleanField(default=True)


class Counselor(models.Model):
    name=models.CharField(max_length=25)
    image=models.CharField(max_length=256,null=True)
    designation=models.CharField(max_length=30)
    available_from=models.TimeField()
    available_to=models.TimeField()
    contact_number=models.CharField(max_length=15)



