from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Sum,Avg
from .models import SleepLog
from .serializers import SleepLogSerializer

class SleepLogViewset(viewsets.ModelViewSet):
    serializer_class=SleepLogSerializer

    def get_queryset(self):
        return SleepLog.objects.all().order_by('-sleep_start')

    @action(detail=False, methods=['GET'])
    def sleep_analysis(self, request):
        sleep_logs = self.get_queryset()
        total_duration = sum([(log.sleep_end - log.sleep_start).total_seconds() for log in sleep_logs], 0)
        total_duration_hours=total_duration/3600
        total_sleep_logs = sleep_logs.count()

        average_quality = sleep_logs.aggregate(Avg('quality'))['quality__avg'] or 0

        return Response({
            "total_sleep_logs": total_sleep_logs,
            "total_duration": total_duration_hours,  
            "average_quality": average_quality,
        })
# Create your views here.
