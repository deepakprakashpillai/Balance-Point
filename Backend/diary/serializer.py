from dataclasses import fields
from rest_framework import serializers
from .models import DiaryLog,Event,Counselor

class DiaryLogSerializer(serializers.ModelSerializer):
    mood_descriptors=serializers.CharField()
    def create(self,validate_data):
        mood_descriptors=validate_data.get('mood_descriptors','')
        validate_data['mood_descriptors']=mood_descriptors.split(',')
        return super().create(validate_data)
    class Meta:
        model=DiaryLog
        fields=['user','date','mood_descriptors','emotional_rating']
        

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields=['title','content','image','date']

class CounselorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Counselor
        fields=['name','image','designation','available_from','available_to','contact_number']


