from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.generic import DetailView, CreateView

from config import settings
from orders.models import Order
from products.models import Item


class OrderDetailView(DetailView):
    model = Order
    template_name = "order_detail.html"
    context_object_name = "order"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['STRIPE_PUBLIC_KEY'] = settings.STRIPE_PUBLIC_KEY
        return context


@csrf_protect
def create_order(request):
    if request.method == 'POST':
        cart = request.session.get('cart', [])

        order = Order.objects.create()
        for item_id in cart:
            item = Item.objects.get(id=item_id)
            order.items.add(item)
        total = sum(item.price for item in order.items.all())
        order.total_price = total
        order.save()

        del request.session['cart']
        request.session.modified = True

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})
