import stripe
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from config.settings import STRIPE_SECRET_KEY
from products.models import Item


def buy_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    stripe.api_key = STRIPE_SECRET_KEY

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {"name": item.name},
                    "unit_amount": int(item.price * 100),
                },
                "quantity": 1,
            },
        ],
        mode="payment",
        success_url="http://localhost:8000/order-complete/",
        cancel_url="http://localhost:8000/order-canceled/"
    )

    return JsonResponse({"session_id": session.id})
