import json

from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from product.models import Product
from .forms import ProductForm

def product_list(request):
    """Return list of products."""
    products = Product.objects.all()
    data = {"products": list(products.values("id", "name", "value", "discount_value", "stock"))}
    return JsonResponse(data)

@csrf_exempt
def product_create(request):
    """Bulk creation of one or many products."""
    if request.method == "POST":
        all_valid = True
        count_product_errors = 0
        products_report = []
        products = []
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        for product in body['products']:
            product_form = ProductForm(product, instance=Product())
            if product_form.is_valid():
                product = product_form.save()
                products.append(product)
            else:
                all_valid = False
                count_product_errors += 1
                errors = product_form.errors
                products_report.append({
                    'product_name': product.get('name', ''),
                    'errors': errors
                })
        if not all_valid:
            response = json.dumps({
                'status': 'ERROR',
                'products_report': products_report,
                'number_of_products_unable_to_parse': count_product_errors
            })
            return HttpResponse(response, status=422, content_type="application/json")
        # Add products in a bulk creation
        Product.objects.bulk_create(products)
        response = json.dumps({
            'status': 'OK'
        })
        return HttpResponse(response, status=200, content_type="application/json")