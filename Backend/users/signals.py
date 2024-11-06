from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import User,UserAssessment

@receiver(post_save,sender=User)
def calculate_age(sender,instance,created,**kwargs):
    if created:
        if instance.dob:
            today = timezone.now().date()
            instance.age = today.year - instance.dob.year -((today.month, today.day) < (instance.dob.month, instance.dob.day))
            instance.save()
            
            
@receiver(post_save, sender=UserAssessment)
def calculate_rmr_bmi(sender, instance, created, **kwargs):
    if created:
        weight_kg = instance.weight
        height_cm = instance.height
        age = instance.user.age

        # Check if weight and height are not None
        if weight_kg is not None and height_cm is not None:
            # Convert Decimal to float if necessary
            weight_kg = float(weight_kg)
            height_cm = float(height_cm)

            # Calculate RMR based on gender
            if instance.user.gender == 'male':
                instance.rmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
            else:
                instance.rmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
            
            height_m = height_cm / 100  
            if height_m > 0: 
                bmi = weight_kg / (height_m ** 2)
                instance.bmi = bmi 
            else:
                instance.bmi = None  
            instance.save()