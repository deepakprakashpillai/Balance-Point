from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import sleep_analysis_view,sleep_log_view
urlpatterns=[
    path('sleep/<int:user_id>/',sleep_log_view),
    path('sleep/sleep_analysis/<int:user_id>/', sleep_analysis_view),
]