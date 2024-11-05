# views.py

from rest_framework import viewsets
from .models import Counselor, DiaryLog,News
from .serializer import CounselorSerializer, DiaryLogSerializer,NewsSerializer
from rest_framework.response import Response
from django.utils import timezone
from rest_framework.decorators import action

class DiaryLogViewSet(viewsets.ModelViewSet):
    queryset = DiaryLog.objects.all().order_by('-date')
    serializer_class = DiaryLogSerializer

    def perform_create(self, serializer):
        serializer.save() 
    @action(detail=False, methods=['GET'])
    def user_log(self, request,user_id=None):

        if user_id:
            logs = DiaryLog.objects.filter(user=user_id).order_by('-date')
            serializer = self.get_serializer(logs, many=True)
            return Response(serializer.data)
        return Response({"detail": "User ID not provided."}, status=400)


class NewsViewSet(viewsets.ModelViewSet):
    queryset=News.objects.filter(is_published=True).order_by('-date_published')
    serializer_class=NewsSerializer
class CounselorViewSet(viewsets.ModelViewSet):
    queryset=Counselor.objects.all()
    serializer_class=CounselorSerializer


