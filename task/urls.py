from django.urls import path
from .views import TaskListCreateAPIView, TaskRetrieveUpdateAPIView

urlpatterns = [
    path('', TaskListCreateAPIView.as_view()),
    path('<int:pk>/', TaskRetrieveUpdateAPIView.as_view()),
]