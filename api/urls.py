from django.conf.urls import url
from .product import views as product_views

urlpatterns = [
    url(r'^products/$', product_views.product_list),
    url(r'^products/bulk_insert/$', product_views.product_create),
]
