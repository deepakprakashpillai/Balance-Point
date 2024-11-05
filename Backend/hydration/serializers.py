from dataclasses import fields
from rest_framework import serializers
from .models import HydrationLog

class HydrationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model=HydrationLog
        fields=['id','user','amount','timestamp']
        read_only_fields=['timestamp']