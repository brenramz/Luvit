import json

from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from product.models import Product

def product_list(request):
    products = Product.objects.all()
    data = {"products": list(products.values("id", "name", "value", "discount_value", "stock"))}
    return JsonResponse(data)

@csrf_exempt
def product_create(request):
    if request.method == "POST":
        all_valid = True
        count_product_errors = 0
        products_report = []
        products = []
        for product in request.POST.get('products', []):
            product_form = forms.ProductForm(request.POST or None, instance=Product())
            if product_form.is_valid():
                product = product_form.save()
                products.append(product)
            else:
                all_valid = False
                count_product_errors += 1
                errors = []
                for key,value in reschedule_form.errors.items():
                    error_msg +="{}: {}".format(key, ','.join(value))
                    errors.append(error_msg)
                products_report.append({
                    'product_id': str(product.id),
                    'errors': errors
                })
        # Add products in a bulk creation
        if not all_valid:
            response = json.dumps({
                'status': 'ERROR',
                'products_report': products_report,
                'number_of_products_unable_to_parse': count_product_errors
            })
            return HttpResponse(response, status=422, content_type="application/json")
        Product.objects.bulk_create(products)
        response = json.dumps({
            'status': 'OK'
        })
        return HttpResponse(response, status=200, content_type="application/json")