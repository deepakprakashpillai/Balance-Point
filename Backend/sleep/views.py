from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import SleepLog
from .serializers import SleepLogSerializer
from datetime import datetime, timedelta

class SleepLogViewset(viewsets.ModelViewSet):
    serializer_class = SleepLogSerializer

    def get_queryset(self):
        return SleepLog.objects.all().order_by('-sleep_start')

    @action(detail=False, methods=['GET'])
    def sleep_analysis(self, request, user_id=None):
        # Filter sleep logs for the specific user
        sleep_logs = SleepLog.objects.filter(user=user_id)
        print(sleep_logs)

        # If there are no sleep logs, return a message
        if not sleep_logs.exists():
            return Response({"message": "No sleep logs found for the specified user"}, status=status.HTTP_404_NOT_FOUND)

        for log in sleep_logs:
            print(log.duration)

        # Calculate total duration (in seconds) and daily summary (in hours)
        total_duration_seconds = sum((log.duration.total_seconds() for log in sleep_logs), 0)
        daily_summary = [
            {
                'date': log.sleep_start.date(),
                'duration': log.duration.total_seconds() / 3600  
            }
            for log in sleep_logs
        ]

        # Calculate average quality
        qualities = [log.quality for log in sleep_logs]
        average_quality = sum(qualities) / len(qualities) if qualities else 0

        return Response({
            "user_id": user_id,
            "daily_sleep_summary": daily_summary,
            "average_quality": average_quality,
            "total_duration": total_duration_seconds  
        })
