from __future__ import unicode_literals
from django import forms
from product.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fiels = '__all__'

    def save(self, commit=True):
        instance = super(ProductForm, self).save(commit=False)
        return instance
