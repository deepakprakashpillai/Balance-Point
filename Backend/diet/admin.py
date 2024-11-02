from django.contrib import admin
from .models import Meal,FoodItem,FoodServing
# Register your models here.
admin.site.register(Meal)
admin.site.register(FoodItem)
admin.site.register(FoodServing)