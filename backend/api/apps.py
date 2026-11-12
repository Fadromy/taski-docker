"""Конфигурация приложения API."""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Настройки приложения API."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
