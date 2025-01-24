from django.urls import path
from products.views import ListProductsView, ProductFormView

# http://127.0.0.1:8000/products/

urlpatterns = [
    path("", ListProductsView.as_view(), name="list_product"),
    path("add/", ProductFormView.as_view(), name="add_product"),
]
