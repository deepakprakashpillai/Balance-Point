import re
from asyncio.windows_events import NULL
from importlib.metadata import requires
from pyexpat import model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from .models import UserAssessment

User = get_user_model()

class UserAssessmentSerializer(ModelSerializer):
    class Meta:
        model = UserAssessment
        fields = '__all__'
     


class UserSerializer(ModelSerializer): 
    password = serializers.CharField(write_only=True)

    class Meta: 
        model = User 
        fields = ['id','first_name', 'last_name', 'email', 'username', 'password','date_joined', 'gender', 'phone_number', 'age', 'dob','is_assessment_completed'] 
        
    def create(self, validated_data):
        password = validated_data.pop("password")
        user_obj = User.objects.create(**validated_data)
        user_obj.set_password(password)
        user_obj.save()
        return user_obj
    
    
class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required = True)
    new_password = serializers.CharField(required = True)
    
    def validate_old_password(self,value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is incorrect")
        return value
    
    def validate_new_password(self,value):
        # if not re.search(r'[A-Z]', value):
        #     raise serializers.ValidationError("New password must contain at least one uppercase letter.")
        # if not re.search(r'[a-z]', value):
        #     raise serializers.ValidationError("New password must contain at least one lowercase letter.")
        # if not re.search(r'\d', value):
        #     raise serializers.ValidationError("New password must contain at least one digit.")
        # if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
        #     raise serializers.ValidationError("New password must contain at least one special character.")
        return value


