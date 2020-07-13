from __future__ import unicode_literals
from django import forms
from product.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        error_messages = {
            'name': {
                'min_length': 'Invalid product name',
                'max_length': 'Invalid product name'
            },
            'value': {
                'min_value': 'Invalid value',
                'max_value': 'Invalid value'
            },
            'discount_value': {
                'min_value': 'Invalid discount value',
                'max_value': 'Invalid discount value'
            },
            'stock': {
                'min_value': 'Invalid stock value'
            }
        }

    def save(self, commit=True):
        instance = super(ProductForm, self).save(commit=False)
        return instance
