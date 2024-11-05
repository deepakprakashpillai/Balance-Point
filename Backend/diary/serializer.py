from dataclasses import fields
from rest_framework import serializers
from .models import DiaryLog,News,Counselor

class DiaryLogSerializer(serializers.ModelSerializer):
    class Meta:
        model=DiaryLog
        fields=['user','date','mood_descriptors','emotional_rating']
        read_only_fields=['date']
        

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=News
        fields=['title','content','image','date_published']

class CounselorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Counselor
        fields=['name','image','designation','available_from','available_to','contact_number']


