from django.conf.urls import url
from .product import views as product_views

urlpatterns = [
    url(r'^product/$', product_views.product_list),
]
