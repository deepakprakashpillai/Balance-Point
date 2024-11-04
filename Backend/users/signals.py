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
        # Get user details
        weight_kg = instance.user.weight
        height_cm = instance.user.height
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
            
            height_m = height_cm / 100  # Convert height from cm to meters
            if height_m > 0:  # Ensure height is not zero
                bmi = weight_kg / (height_m ** 2)
                instance.bmi = bmi  # Assuming you have a bmi field in UserAssessment model
            else:
                instance.bmi = None  # Handle case where height is zero or invalid
            # Save the UserAssessment instance with the calculated RMR
            instance.save()