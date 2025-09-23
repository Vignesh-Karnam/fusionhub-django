from django.db import models

from ..core.models import Platform, User


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    product_id = models.CharField(max_length=100)
    title = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField()
    brand = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
