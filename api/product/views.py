from django.shortcuts import render
from django.http import JsonResponse

from product.models import Product

def product_list(request):
    products = Product.objects.all()
    data = {"products": list(products.values("id", "name", "value", "discount_value", "stock"))}
    return JsonResponse(data)
