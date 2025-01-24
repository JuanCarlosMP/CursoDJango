from django.urls import path
from orders.views import MyOrderView, CreateOrderProductView

urlpatterns = [
    path("", MyOrderView.as_view(), name="my_order"),
    path("add/", CreateOrderProductView.as_view(), name="add_order_product"),
]
