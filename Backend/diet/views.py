
from functools import partial
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import FoodItem,FoodServing,Meal
from .serializers import FoodItemSerializer,MealSerializer

class FoodItemViewset(ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    
    
@api_view(['POST','GET','DELETE','PATCH'])
def meal_view(request,id=None):
    if request.method == 'POST':
        serializer = MealSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'GET':
        meal_data = get_object_or_404(Meal, pk=id)
        serializer = MealSerializer(meal_data)
        return Response(serializer.data, status = status.HTTP_200_OK)
        
    elif request.method == 'DELETE':
        meal_data = get_object_or_404(Meal,pk=id)
        meal_data.delete()
        return Response("Meal Deleted Succesffully",status = status.HTTP_200_OK)
    
    elif request.method == 'PATCH':
        meal_data = get_object_or_404(Meal,pk=id)
        serializer = MealSerializer(meal_data,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET'])
def user_meals_view(request,id):
    try:
        meals = Meal.objects.filter(user = id)
        serializer = MealSerializer(meals,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Meal.DoesNotExist:
        return Response({'details' : "No such Meal for the user"}, status=status.HTTP_404_NOT_FOUND)