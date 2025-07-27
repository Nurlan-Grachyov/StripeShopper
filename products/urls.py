from django.urls import path

from products.apps import ProductsConfig
from products.services import test_session
from products.views import ItemCreateView

app_name = ProductsConfig.name

urlpatterns = [
    path("create_item", ItemCreateView.as_view(), name="create_item"),
    path("test_session/<str:session_id>/", test_session, name="test_session")
]
