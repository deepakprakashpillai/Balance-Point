from django.urls import path
from .views import user_view,user_register_view,change_password_view
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    path('profile/<int:id>',user_view),
    path('register/',user_register_view),
    path('change-password/',change_password_view),
    path('login/',TokenObtainPairView.as_view(),name="token_obtain_pair"),
    path('refresh/',TokenRefreshView.as_view(),name="token_refresh"),
]
