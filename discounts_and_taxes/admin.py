from django.contrib import admin

from discounts_and_taxes.models import Tax, Discount


@admin.register(Tax)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "value")


@admin.register(Discount)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "value", "is_percentage")
