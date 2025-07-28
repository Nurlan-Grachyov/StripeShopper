from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView, DetailView

from config import settings
from products.models import Item
from django.http import JsonResponse


class ItemCreateView(CreateView):
    model = Item
    fields = ["name", "description", "price", "currency"]

    def form_valid(self, form):
        instance = form.save()
        return JsonResponse({
            'message': 'Item created successfully.',
            'data': {
                'id': instance.id,
                'name': instance.name,
                'description': instance.description,
                'price': str(instance.price),
                'currency': instance.currency
            }
        })


class ItemDetailView(DetailView):
    model = Item
    template_name = "item_detail.html"
    context_object_name = "item"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['STRIPE_PUBLIC_KEY'] = settings.STRIPE_PUBLIC_KEY
        return context
