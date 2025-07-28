from django.db import models

from products.models import Item


class Order(models.Model):
    items = models.ManyToManyField(Item, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def calculate_total_price(self):
        return sum(item.price for item in self.items.all())

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.total_price = self.calculate_total_price()
        super().save(*args, **kwargs)