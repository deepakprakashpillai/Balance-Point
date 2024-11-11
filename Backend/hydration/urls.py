
from django.urls import path, include
from .views import hydration_log_view,last_drink_time,total_water_intake_by_user


urlpatterns = [
    path('hydration/<int:user_id>/',hydration_log_view),
    path('hydration/last_drink_time/<int:user_id>/', last_drink_time),
    path('hydration/total_water_intake_by_user/<int:user_id>/', total_water_intake_by_user),
]
