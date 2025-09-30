from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Platform(models.Model):
    name = models.CharField(max_length=50, unique=True)
    base_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
