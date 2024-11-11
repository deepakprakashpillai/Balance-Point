from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class FoodItem(models.Model):
    name = models.CharField(max_length=25)
    calories_per_100g = models.IntegerField()     
    added_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    class Meta:
        verbose_name = ("Food Item")
        verbose_name_plural = ("Food Items")

    def __str__(self):
        return self.name
    
    
    
class Meal(models.Model):
    MEAL_EXPERIENCE_CHOICES = [
        ('Happy', 'Happy'),
        ('Calm', 'Calm'),
        ('Tired', 'Tired'),
        ('Stressed', 'Stressed'),
        ('Energized', 'Energized'),
        ('Unhappy', 'Unhappy'),
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    total_calories = models.IntegerField(default=0)
    meal_experience = models.CharField(max_length = 15,choices=MEAL_EXPERIENCE_CHOICES)
    

    class Meta:
        verbose_name = ("Meal")
        verbose_name_plural = ("Meals")

    def __str__(self):
        servings_info = ", ".join(str(serving) for serving in self.food_servings.all())
        return f"Meal - {servings_info} ({self.meal_experience})"

    
    
    
class FoodServing(models.Model):
    food_item = models.ForeignKey(FoodItem,on_delete=models.CASCADE)
    quantity = models.IntegerField() # grams
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE,related_name='food_servings',null=True)
    note = models.CharField(max_length=255, blank=True, null=True)    

    class Meta:
        verbose_name = ("Food Serving")
        verbose_name_plural = ("Food Servings")

    def __str__(self):
        return f"{self.quantity}g of {self.food_item.name}"
    




