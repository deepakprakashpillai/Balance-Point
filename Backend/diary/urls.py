from unicodedata import name
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CounselorViewSet, DiaryLogViewSet,NewsViewSet

router=DefaultRouter()
router.register(r'diary',DiaryLogViewSet,basename='diarylog')
router.register(r'news',NewsViewSet,basename='news')
router.register(r'counselor',CounselorViewSet,basename='counselor')

urlpatterns = [
    path('', include(router.urls)),
    path('diary/user_log/<int:user_id>/', DiaryLogViewSet.as_view({'get': 'user_log'}), name='user_log'),
    

]