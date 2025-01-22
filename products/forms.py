from django import forms
from products.models import Product

class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, label='Nombre')
    description = forms.CharField(max_length=300, label='Descripcion')
    precio = forms.DecimalField(max_digits=10, decimal_places=2, label='Precio')
    available = forms.BooleanField(initial=True, required=True, label='Disponible')
    picture = forms.ImageField(required=False, label='Imagen')

    def save(self):
        Product.objects.create(
            name = self.cleaned_data['name'],
            description = self.cleaned_data['description'],
            precio = self.cleaned_data['precio'],
            available = self.cleaned_data['available'],
            picture = self.cleaned_data['picture']
        )