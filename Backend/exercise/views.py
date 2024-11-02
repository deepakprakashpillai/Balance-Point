from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Exercise,WorkoutSession
from .serializers import ExerciseSerializer,WorkoutSessionSerializer

class ExerciseView(ModelViewSet):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()
    
    
@api_view(['POST','GET','DELETE','PATCH'])
def workout_session_view(request,id=None):
    if request.method == 'POST':
        serializer = WorkoutSessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # This calls the create method in your serializer
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        session_data = get_object_or_404(WorkoutSession,pk=id)
        serializer = WorkoutSessionSerializer(session_data)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        session_data = get_object_or_404(WorkoutSession,pk=id)
        session_data.delete()
        return Response("Session deleted successfully",status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        session_data = get_object_or_404(WorkoutSession,pk=id)
        serializer = WorkoutSessionSerializer(session_data,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET'])
def user_sessions_view(request,id):
    try:
        sessions = WorkoutSession.objects.filter(user = id)
        serializer = WorkoutSessionSerializer(sessions,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except WorkoutSession.DoesNotExist:
        return Response({'detail': 'No sessions found for this user.'}, status=status.HTTP_404_NOT_FOUND)