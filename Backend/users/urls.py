from django.urls import path
from .views import new_user_view, toggle_assessment_view, user_view,change_password_view,AssessmentView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'assessment',AssessmentView,basename='assessment')


urlpatterns = [
    path('',user_view),
    path('register/',new_user_view),
    path('<int:id>/',user_view),
    path('change-password/',change_password_view),
    path('login/',TokenObtainPairView.as_view(),name="token_obtain_pair"),
    path('refresh/',TokenRefreshView.as_view(),name="token_refresh"),
    path('toggle-assessment/',toggle_assessment_view)
]

urlpatterns += router.urls
