from django.http import HttpResponse
from django.urls import path

from products.apps import ProductsConfig
from products.services import buy_item
from products.views import ItemCreateView, ItemDetailView

app_name = ProductsConfig.name

urlpatterns = [
    path("create_item/", ItemCreateView.as_view(), name="create_item"),
    path("item/<int:pk>/", ItemDetailView.as_view(), name="item_detail"),
    path("buy/<int:item_id>/", buy_item, name="buy-item"),
    path('order-complete/', lambda r: HttpResponse('Оплата прошла успешно!')),
    path('order-canceled/', lambda r: HttpResponse('Оплата отменена.')),
]
