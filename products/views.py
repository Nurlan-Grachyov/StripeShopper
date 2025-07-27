from django.views.generic import CreateView

from products.models import Item
from django.http import JsonResponse


class ItemCreateView(CreateView):
    model = Item

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
