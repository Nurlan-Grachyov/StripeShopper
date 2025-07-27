from django.contrib import admin

from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("get_items_names", "total_price")

    def get_items_names(self, obj):
        return ", ".join([item.name for item in obj.items.all()])

    get_items_names.short_description = 'Items'