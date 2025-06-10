from django.db import models


class Style(models.Model):
    """Represents a style transfer model."""

    name = models.CharField(max_length=255, unique=True)
    file_path = models.CharField(max_length=1024)
    framework = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
