from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import SleepLog
from .serializers import SleepLogSerializer

@api_view(['GET', 'POST'])
def sleep_log_view(request, user_id=None):
    if user_id:
        if request.method == 'GET':
            # Retrieve all sleep logs for the user
            sleep_logs = SleepLog.objects.filter(user=user_id)
            serializer = SleepLogSerializer(sleep_logs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'POST':
            # Create a new sleep log
            serializer = SleepLogSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user_id=user_id)  # Save with the user_id
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({"message": "Invalid input."}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({"message": "User ID is required."}, status=status.HTTP_400_BAD_REQUEST)

from datetime import timedelta

@api_view(['GET'])
def sleep_analysis_view(request, user_id=None):
    if user_id:
        # Filter sleep logs for the specific user
        sleep_logs = SleepLog.objects.filter(user=user_id)
        if not sleep_logs.exists():
            return Response({"message": "No sleep logs found for the specified user."}, status=status.HTTP_404_NOT_FOUND)

        # Calculate total duration in seconds
        total_duration_seconds = sum((log.duration.total_seconds() for log in sleep_logs), 0)

        # Daily summary in hours
        daily_summary = [
            {
                'date': log.sleep_start.date(),
                'duration': log.duration.total_seconds() / 3600  # Convert to hours
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
        }, status=status.HTTP_200_OK)
    
    return Response({"message": "User ID is required."}, status=status.HTTP_400_BAD_REQUEST)
