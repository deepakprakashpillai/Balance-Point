
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HydrationLogViewset

router = DefaultRouter()
router.register(r'hydration', HydrationLogViewset, basename='hydration')

urlpatterns = [
    path('',include(router.urls)),
    path('hydration/total_water_intake/<int:user_id>/', HydrationLogViewset.as_view({'get': 'total_water_intake'}), name='total_water_intake'),
    path('hydration/last_drink_time/<int:user_id>/', HydrationLogViewset.as_view({'get': 'last_drink_time'}), name='last_drink_time'),
]
