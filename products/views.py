from django.shortcuts import render
from django.views.generic import TemplateView
from products.forms import ProductForm
from products.models import Product
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# class ListProductsView(TemplateView):
#     template_name = 'products/list_products.html'

#     def get_context_data(self, **kwargs):
#         products = Product.objects.all()

#         context = super().get_context_data(**kwargs)
#         context['list_products'] = products

#         return context


class ListProductsView(LoginRequiredMixin, generic.ListView):
    template_name = "products/list_products.html"
    model = Product
    context_object_name = "list_products"


class ProductFormView(LoginRequiredMixin, generic.FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy("list_product")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
