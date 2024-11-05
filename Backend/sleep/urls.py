from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import SleepLogViewset

router=DefaultRouter()
router.register(r'sleep',SleepLogViewset,basename='sleep')
urlpatterns=[
    path('',include(router.urls)),
    path('sleep/sleep_analysis/<int:user_id>/', SleepLogViewset.as_view({'get': 'sleep_analysis'}), name='sleep_analysis'),
    
]