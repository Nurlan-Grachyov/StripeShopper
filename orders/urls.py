from django.http import HttpResponse
from django.urls import path

from orders.apps import OrdersConfig
from orders.services import buy_order
from orders.views import create_order, OrderDetailView

app_name = OrdersConfig.name

urlpatterns = [
    path("create_order/", create_order, name="create_order"),
    path("order/<int:pk>/", OrderDetailView.as_view(), name="order_detail"),
    path("buy/<int:order_id>/", buy_order, name="buy-order"),
    path('order-complete/', lambda r: HttpResponse('Оплата прошла успешно!')),
    path('order-canceled/', lambda r: HttpResponse('Оплата отменена.')),
]
