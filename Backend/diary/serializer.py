from dataclasses import fields
from rest_framework import serializers
from .models import DiaryLog

class DiaryLogSerializer(serializers.ModelSerializer):
    class Meta:
        model=DiaryLog
        fields=['user','date','mood_descriptors','emotional_rating']
        read_only_fields=['date']
        