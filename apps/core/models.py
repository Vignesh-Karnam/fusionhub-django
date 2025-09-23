from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Platform(models.Model):
    name = models.CharField(max_length=50)
    base_url = models.CharField()
