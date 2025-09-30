from django.db import models

from ..core.models import Platform, User


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, related_name="products")
    product_id = models.CharField(max_length=100)

    title = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=500, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True)

    url = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("platform", "product_id", "user")
        indexes = [
            models.Index(fields=["platform", "product_id"]),
            models.Index(fields=["title"]),
            models.Index(fields=["brand"]),
        ]

    def __str__(self):
        return f"{self.title or self.product_id} ({self.platform.name})"


class ProductSnapshot(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="snapshots")

    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True)

    rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    review_count = models.PositiveIntegerField(blank=True, null=True)

    availability = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["created_at"]),
            models.Index(fields=["price"]),
            models.Index(fields=["rating"]),
        ]
        ordering = ["-created_at"]

    def __str__(self):
        return f"Snapshot of {self.product} at {self.created_at}"
