from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import FoodServing, Meal

def calculate_total_calories(meal):
    total_calories = sum(
        food_serving.quantity * food_serving.food_item.calories_per_100g / 100
        for food_serving in meal.food_servings.all()
    )

    if meal.total_calories != total_calories:
        meal.total_calories = total_calories
        meal.save(update_fields=['total_calories'])

@receiver(post_save, sender=FoodServing)
def update_meal_calories_on_food_serving_save(sender, instance, created, **kwargs):
    """Update the total calories of the meal whenever a FoodServing is saved."""
    meal = instance.meal
    calculate_total_calories(meal)

@receiver(pre_delete, sender=FoodServing)
def update_meal_calories_on_food_serving_delete(sender, instance, **kwargs):
    """Update the total calories of the meal whenever a FoodServing is deleted."""
    meal = instance.meal
    calculate_total_calories(meal)

@receiver(post_save, sender=Meal)
def update_meal_calories_on_meal_save(sender, instance, created, **kwargs):
    """Update the total calories of the meal whenever a Meal is updated."""
    calculate_total_calories(instance)
