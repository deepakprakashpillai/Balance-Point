from functools import partial
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from users.models import UserAssessment
from .serializers import UserSerializer,UserAssessmentSerializer,PasswordChangeSerializer
from rest_framework.response import Response
from rest_framework import status
User = get_user_model()
# Create your views here.

@api_view(['GET','PATCH'])
def user_view(request,id):
    if request.method == 'GET':
        user_obj = get_object_or_404(User,pk=id)
        serializer = UserSerializer(user_obj)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method == 'PATCH':
        user_obj = get_object_or_404(UserAssessment,user_id=id)
        serializer = UserAssessmentSerializer(user_obj,data=request.data,partial=True)
        
        if serializer.is_valid():
            print("Validated data:", serializer.validated_data)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
def user_register_view(request):
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