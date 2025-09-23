from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Platform(models.Model):
    name = models.CharField(max_length=50)
    base_url = models.CharField()


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    product_id = models.CharField(max_length=100)
    title = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField()
    brand = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Competitor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="competitors")
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    competitor_id = models.CharField(max_length=100)
    title = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField()
    brand = models.CharField(max_length=100, blank=True, null=True)
    last_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    added_by_user = models.BooleanField(default=True)
    confirmed = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
