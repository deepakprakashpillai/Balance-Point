from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import FoodItemViewset,meal_view,user_meals_view

Router = DefaultRouter()
Router.register(r'food-items',FoodItemViewset)

urlpatterns = [
    path('meals/<int:id>',meal_view),
    path('meals/',meal_view),
    path('meals/user/<int:id>',user_meals_view)
]

urlpatterns += Router.urls
