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

    def clean_discount_value(self):
        discount_value = self.cleaned_data['discount_value']
        if discount_value and :

        cashback_discount_maximum_value = self.cleaned_data['cashback_discount_maximum_value']
        if cashback_discount_value_type and cashback_discount_value_type != DiscountValueType.PERCENTAGE:
            return Price(0, currency=settings.DEFAULT_CURRENCY)
        return cashback_discount_maximum_value

    def clean(self):
        super(ProductForm, self).clean()
        discount_value = self.cleaned_data.get('discount_value', '')
        value = self.cleaned_data.get('value')
        if discount_value and discount_value > value:
            self.add_error('discount_value', 'Invalid discount value')
        return self.cleaned_data