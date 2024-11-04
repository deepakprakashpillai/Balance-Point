from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    gender = models.CharField(max_length=6,choices=[('male','male'),('female','female'),('other','other')],blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    age = models.IntegerField(default=0)
    height = models.IntegerField(blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class UserAssessment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_assessment")
    goal = models.CharField(max_length=50, null=True,blank=True, choices=[
        ('Maintain', 'Maintain'),
        ('Loss', 'Loss'),
        ('Gain', 'Gain'),
    ])
    target_weight = models.FloatField(null=True, blank=True)

    # Fitness level
    activity_level = models.CharField(max_length=50, null=True,blank=True,choices=[
        ('Sedentary', 'Sedentary'),
        ('Lightly active', 'Lightly active'),
        ('Moderately active', 'Moderately active'),
        ('Very active', 'Very active'),
        ('Extra active', 'Extra active'),
    ])
    exercise_frequency = models.IntegerField(null=True, blank=True)  # Number of days per week
    exercise_type = models.CharField(max_length=50, null=True, blank=True, choices=[
        ('cardio', 'Cardio'),
        ('weightlifting', 'Weightlifting'),
        ('sports', 'Sports'),
        ('other', 'Other'),
    ])
    exercise_duration = models.IntegerField(null=True, blank=True)  # Duration in minutes
    rmr = models.FloatField(null=True, blank=True)  # Resting Metabolic Rate
    bmi = models.FloatField(null=True,blank=True)

    # Sleep
    average_sleep_time = models.DurationField(null=True, blank=True)
    sleep_quality_rating = models.IntegerField(null=True, blank=True)  # 1-10 scale
    sleep_issues = models.CharField(max_length=50, null=True, blank=True, choices=[
        ("Insomnia","Insomnia"),
        ("Nightmares","Nightmares"),
        ("Stress or Anxiety","Stress or Anxiety"),
        ("Discomfort","Discomfort"),
        ("Irregular Sleep Schedule","Irregular Sleep Schedule"),
    ])

    # Hydration
    average_water_intake = models.IntegerField(null=True, blank=True)  # Glasses of water per day

    # Mental health
    stress_level = models.IntegerField(null=True, blank=True)  # 1-10 scale
    mood_frequency = models.IntegerField(null=True, blank=True)  # How often they feel low (1-4 scale)
    mood_improvement_goal = models.CharField(max_length=50, null=True, blank=True, choices=[
        ('Mindfulness', 'Mindfulness'),
        ('More Physical Activity', 'More Physical Activity'),
        ('Gratitude Journal', 'Gratitude Journal'),
        ('Connect with Others', 'Connect with Others'),
        ('Establish a Sleep Routine', 'Establish a Sleep Routine'),
    ])

    # Lifestyle
    smokes = models.BooleanField(default=False)
    alcohol_consumption = models.CharField(max_length=50, null=True, blank=True, choices=[
        ('None', 'None'),
        ('Occasional', 'Occasional'),
        ('Moderate', 'Moderate'),
        ('Frequent', 'Frequent'),
        ('Heavy', 'Heavy'),
    ])  # Frequency of consumption
    mindfulness_practices = models.BooleanField(default=False)
    screen_time = models.IntegerField(null=True, blank=True)  # Hours on screens per day

    # Long-term goals
    main_wellness_goal = models.CharField(null=True, max_length=50, blank=True, choices=[
        ('Physical Health', 'Physical Health'),
        ('Mental Wellbeing', 'Mental Wellbeing'),
        ('Emotional Balance', 'Emotional Balance'),
        ('Social Connections', 'Social Connections'),
        ('Overall Wellness', 'Overall Wellness'),
    ])
    self_motivation = models.IntegerField(null=True, blank=True)  # 1-10 scale
    biggest_challenge = models.CharField(max_length=50, null=True, blank=True, choices=[
        ('Time Management', 'Time Management'),
        ('Motivation', 'Motivation'),
        ('Stress Management', 'Stress Management'),
        ('Access to Resources', 'Access to Resources'),
        ('Support System', 'Support System'),
    ])

    def __str__(self):
        return f"Fitness Assessment for {self.user.username}"
