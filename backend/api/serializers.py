"""Сериализаторы задач для API."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Преобразование задач в данные API и обратно."""

    class Meta:
        """Модель и поля сериализатора задач."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
