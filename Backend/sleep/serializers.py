from pyexpat import model
from rest_framework import serializers
from .models import SleepLog
class SleepLogSerializer(serializers.ModelSerializer):
    class Meta:
        model=SleepLog
        fields=[
            'user', 'sleep_start', 'sleep_end', 'duration', 'quality', 'interrupted'
            
        ]
        read_only_fields=['user','duration']

        def create(self,validate_data):
            validate_data['duration']=validate_data['sleep_end']-validate_data['sleep_start']
            return super.create(validate_data)


