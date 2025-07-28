import stripe
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from config.settings import STRIPE_SECRET_KEY
from orders.models import Order
from products.models import Item


def buy_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)

    stripe.api_key = STRIPE_SECRET_KEY

    line_items = []
    for item in order.items.all():
        line_items.append({
            "price_data": {
                "currency": "usd",
                "product_data": {"name": item.name},
                "unit_amount": int(item.price * 100),
            },
            "quantity": 1,
        })

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=line_items,
        mode="payment",
        success_url="http://localhost:8000/order-complete/",
        cancel_url="http://localhost:8000/order-canceled/"
    )

    return JsonResponse({"session_id": session.id})
