from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(default="USD")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
