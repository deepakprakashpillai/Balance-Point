from django.urls import path
from .views import user_view,change_password_view,AssessmentView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'assessment',AssessmentView,basename='assessment')


urlpatterns = [
    path('register/',user_view),
    path('<int:id>/',user_view),
    path('change-password/',change_password_view),
    path('login/',TokenObtainPairView.as_view(),name="token_obtain_pair"),
    path('refresh/',TokenRefreshView.as_view(),name="token_refresh"),
]

urlpatterns += router.urls
