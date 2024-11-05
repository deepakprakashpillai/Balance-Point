from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import DiaryLogViewSet

router=DefaultRouter()
router.register(r'diary',DiaryLogViewSet,basename='diarylog')

urlpatterns = [
    path('', include(router.urls)),
    path('diary/user_log/<int:user_id>/', DiaryLogViewSet.as_view({'get': 'user_log'}), name='user_log'),
]