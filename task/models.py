from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('Новая', 'Новая'),
        ('Запланированная', 'Запланированная'),
        ('в Работе', 'в Работе'),
        ('Завершённая', 'Завершённая'),
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    end_plan_at = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Log(models.Model):
    field_name = models.CharField(max_length=255)
    new_value = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.field_name
