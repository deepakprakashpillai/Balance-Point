from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
from .serializers import HydrationLogSerializer
from .models import HydrationLog
from django.db.models import Sum
from datetime import datetime
from collections import defaultdict

@api_view(['GET','POST'])
def hydration_log_view(request,user_id=None):
    if user_id:
        if request.method == 'GET':
            logs = HydrationLog.objects.filter(user = user_id).order_by('-timestamp')
            serializer = HydrationLogSerializer(logs,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            
            serializer = HydrationLogSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save(user_id=user_id)
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response({"message" : "Invalid input"},status=status.HTTP_400_BAD_REQUEST)
                
    return Response({"message": "User ID is required."}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def last_drink_time(request, user_id=None):
    if user_id:
        last_log = HydrationLog.objects.filter(user=user_id).last() 
        if last_log:
            serializer = HydrationLogSerializer(last_log)
            return Response({"last_drink_time": serializer.data['timestamp']}, status=status.HTTP_200_OK)
        return Response({"message": "No hydration logs found for this user."}, status=status.HTTP_404_NOT_FOUND) 
    return Response({"message": "User ID is required."}, status=status.HTTP_400_BAD_REQUEST)


from datetime import datetime

@api_view(['GET'])
def total_water_intake_by_user(request, user_id=None):
    if user_id:
        logs = HydrationLog.objects.filter(user=user_id)
        
        # Check if logs exist for the given user_id
        if not logs.exists():
            return Response({"message": "No hydration logs found for this user."}, status=status.HTTP_404_NOT_FOUND)

        serializer = HydrationLogSerializer(logs, many=True)
        daily_totals = defaultdict(float)

        for log in serializer.data:
            # Convert the timestamp string to a date
            date_str = datetime.fromisoformat(log['timestamp']).date()  # Convert string to date
            daily_totals[date_str] += log['amount']

        # Prepare the response data
        result = [{"date": str(date), "total_intake": total} for date, total in daily_totals.items()]
        return Response({"user": user_id, "daily_totals": result}, status=status.HTTP_200_OK)

    return Response({"message": "User ID is required."}, status=status.HTTP_400_BAD_REQUEST)


