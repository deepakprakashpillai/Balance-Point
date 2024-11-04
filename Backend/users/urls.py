from django.urls import path
from .views import user_view,user_register_view,change_password_view
urlpatterns = [
    path('profile/<int:id>',user_view),
    path('register/',user_register_view),
    path('change-password/',change_password_view)
]
