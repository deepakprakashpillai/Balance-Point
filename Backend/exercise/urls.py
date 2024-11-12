from rest_framework.routers import DefaultRouter
from .views import ExerciseView,workout_session_view,user_sessions_view,get_exercises_view
from django.urls import path

Router = DefaultRouter()
Router.register(r'exercise',ExerciseView)

urlpatterns = [
    path('workout-session/',workout_session_view),
    path('workout-session/user/<int:id>', user_sessions_view),
    path('workout-session/<int:id>',workout_session_view),
    path('exercises/<int:user_id>',get_exercises_view)
]

urlpatterns += Router.urls