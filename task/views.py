from django.shortcuts import render
from rest_framework import authentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .models import Task, Log
from .serializers import TaskSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner


class TaskListCreateAPIView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # authentication_classes = [BasicAuthentication,]
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)
        status = self.request.GET.get('status')
        end_plan_at = self.request.GET.get('end_plan_at')
        if status is not None and status != '':
            queryset = queryset.filter(status=status)
        if end_plan_at is not None and end_plan_at != '':
            queryset = queryset.filter(end_plan_at__lte=end_plan_at)
        return queryset


class TaskRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # authentication_classes = [BasicAuthentication, ]
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_update(self, serializer):
        print(serializer.validated_data)

        name = serializer.validated_data['name']
        if name != self.get_object().name:
            Log.objects.create(field_name='name', new_value=name)

        description = serializer.validated_data['description']
        if description != self.get_object().description:
            Log.objects.create(field_name='description', new_value=description)

        status = serializer.validated_data['status']
        if status != self.get_object().status:
            Log.objects.create(field_name='status', new_value=status)

        end_plan_at = serializer.validated_data['end_plan_at']
        if end_plan_at != self.get_object().end_plan_at:
            Log.objects.create(field_name='end_plan_at', new_value=end_plan_at)

        serializer.save()

