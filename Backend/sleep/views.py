from sysconfig import is_python_build
from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import SleepLog
from .serializers import SleepLogSerializer

from datetime import datetime, timedelta

class SleepLogViewset(viewsets.ModelViewSet):
    serializer_class=SleepLogSerializer

    def get_queryset(self):
        return SleepLog.objects.all().order_by('-sleep_start')

    @action(detail=False, methods=['GET'])
    def sleep_analysis(self, request,user_id=None):
       
        sleep_logs = SleepLog.objects.filter(user=user_id)
        # print(sleep_logs[0].sleep_start)

        daily_summary = []
        tot_dur = timedelta()
        for log in sleep_logs:
            tot_dur+=log.duration
            dt = datetime.fromisoformat(str(log.sleep_start))
            daily_summary.append({
                'date':dt.date(),
                'duration':log.duration
            })

        qualities = [i.quality for i in sleep_logs]



        if not sleep_logs.exists():
            return Response({"message": "No sleep logs found for the specified user"}, status=status.HTTP_404_NOT_FOUND)
        return Response({
            "user_id": user_id,
            "daily_sleep_summary": daily_summary,
            "average_quality":sum(qualities)/len(qualities),
            "total_duration":tot_dur
        })


# Create your views here.
