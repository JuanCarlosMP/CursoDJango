from django.shortcuts import render
from django.views.generic import TemplateView
from products.models import Product

# Create your views here.
class ListProductsView(TemplateView):
    template_name = 'products/list_products.html'

    def get_context_data(self, **kwargs):
        products = Product.object.all()

        context = super().get_context_data(**kwargs)
        context['list_products'] = products

        return context