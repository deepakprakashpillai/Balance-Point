from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('exercise.urls')),
    path('', include('diet.urls')),
    path('', include('sleep.urls')),
    path('', include('hydration.urls')),
    path('', include('diary.urls')),
    path('user/',include('users.urls'))
]
