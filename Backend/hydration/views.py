from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
from .serializers import HydrationLogSerializer
from .models import HydrationLog
from django.db.models import Sum
from datetime import datetime
from collections import defaultdict

class HydrationLogViewset(viewsets.ModelViewSet):
    serializer_class = HydrationLogSerializer

    def get_queryset(self):
        return HydrationLog.objects.all().order_by('-timestamp')

    def perform_create(self, serializer):
        serializer.save()

   
    @action(detail=False, methods=['GET'])
    def last_drink_time(self, request, user_id=None):
        if user_id:
            last_log = self.get_queryset().filter(user=user_id).first()
            if last_log:
                return Response({"last_drink_time": last_log.timestamp})
            return Response({"message": "No hydration logs found for this user."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message": "User ID is required."}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['GET'])
    def total_water_intake_by_user(self, request, user_id=None):
        if user_id:
            # Fetch all hydration logs for the user
            logs = self.get_queryset().filter(user=user_id)

            # Create a dictionary to hold total intake per date
            daily_totals = defaultdict(float)

            # Iterate through logs to sum amounts by date
            for log in logs:
                # Get the date part of the timestamp
                date_str = log.timestamp.date()  # Gets just the date (YYYY-MM-DD)
                daily_totals[date_str] += log.amount  # Sum the amounts for that date

            # Prepare the response data
            result = [{"date": str(date), "total_intake": total} for date, total in daily_totals.items()]
            return Response({"user": user_id, "daily_totals": result})
        else:
            return Response({"message": "User ID is required."}, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
