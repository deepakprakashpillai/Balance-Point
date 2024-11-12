from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import FoodItemViewset,meal_view,user_meals_view,get_food_items_view

Router = DefaultRouter()
Router.register(r'food-item',FoodItemViewset)

urlpatterns = [
    path('meals/<int:id>',meal_view),
    path('meals/',meal_view),
    path('meals/user/<int:id>',user_meals_view),
    path('food-items/<int:user_id>',get_food_items_view)
]

urlpatterns += Router.urls
