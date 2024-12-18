from functools import partial
from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from users.models import UserAssessment
from .serializers import UserSerializer,UserAssessmentSerializer,PasswordChangeSerializer
from rest_framework.response import Response
from rest_framework import status
User = get_user_model()
# Create your views here.

@api_view(['GET','PATCH'])
@permission_classes([IsAuthenticated])
def user_view(request,id=None):
    if request.method == 'GET':
        if id == None:
            user_obj = request.user
        else:
            user_obj = get_object_or_404(User,pk=id)
        serializer = UserSerializer(user_obj)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method == 'PATCH':
        user_obj = get_object_or_404(User,pk=id)
        serializer = UserSerializer(user_obj,data=request.data,partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
def new_user_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     
@api_view(['PATCH'])
def change_password_view(request):
    serializer = PasswordChangeSerializer(data=request.data,context={'request': request})
    
    if serializer.is_valid():
        user = request.user
        user.set_password(serializer.validated_data['new_password'])
        user.save()
        return Response({"details":"Password reset successfull"},status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def toggle_assessment_view(request):
    user = request.user
    user.is_assessment_completed = True
    user.save()
    return Response({"detail" : "Assessment marked as complete"})


class AssessmentView(ModelViewSet):
    serializer_class = UserAssessmentSerializer
    queryset = UserAssessment.objects.all()

    def get_object(self):
        user_id = self.kwargs.get('pk')
        try:
            return UserAssessment.objects.get(user_id=user_id)
        except UserAssessment.DoesNotExist:
            return None

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)