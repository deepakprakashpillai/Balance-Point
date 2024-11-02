from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
#from rest_framework.permissions import IsAuthenticated
from .serializers import HydrationLogSerializer
from .models import HydrationLog
from django.db.models import Sum

class HydrationLogViewset(viewsets.ModelViewSet):
    serializer_class=HydrationLogSerializer


    def get_queryset(self):
        return HydrationLog.objects.all().order_by('-timestamp')
    def perform_create(self, serializer):
        serializer.save()
    

    @action(detail=False, methods=['GET'])
    def total_water_intake(self, request, user_id=None):
        # Check if a user ID is provided
        if user_id:
            total = self.get_queryset().filter(user=user_id).aggregate(total_intake=Sum('amount'))['total_intake'] or 0
            return Response({"user": user_id, "total_water_intake": total})
        else:
            return Response({"message": "User ID is required."}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['GET'])
    def last_drink_time(self, request, user_id=None):
        if user_id:
            last_log = self.get_queryset().filter(user=user_id).first()
            if last_log:
                return Response({"last_drink_time": last_log.timestamp})
            return Response({"message": "No hydration logs found for this user."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message": "User ID is required."}, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
