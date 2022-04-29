from django.urls import path, include
from .views import UserCreateAPIView

urlpatterns = [
    path('create/', UserCreateAPIView.as_view()),
    path('', include('rest_framework.urls')),
]