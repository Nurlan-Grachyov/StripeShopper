from django.db import models


class Discount(models.Model):
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    is_percentage = models.BooleanField(default=False)  # True, если процентная скидка
    
    class Meta:
        verbose_name = "Скидка"
        verbose_name_plural = "Скидки"


class Tax(models.Model):
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    
    class Meta:
        verbose_name = "Налог"
        verbose_name_plural = "Налоги"