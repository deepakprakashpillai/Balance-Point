from pyexpat import model
from rest_framework import serializers
from .models import SleepLog
class SleepLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepLog
        fields = ['user', 'sleep_start', 'sleep_end', 'duration', 'quality', 'interrupted']
        read_only_fields = ['duration']

    def create(self, validated_data):
        sleep_start = validated_data['sleep_start']
        sleep_end = validated_data['sleep_end']
        # Calculate duration in hours
        duration = sleep_end - sleep_start
        validated_data['duration'] = duration
        return super().create(validated_data)

