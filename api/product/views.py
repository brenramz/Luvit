from django.shortcuts import render
from django.http import JsonResponse

from product.models import Product

def product_list(request):
    products = Product.objects.all()
    data = {"products": products}
    return JsonResponse(data)
