from django.conf.urls import url
from .views import product_list

urlpatterns = [
    url(r'^/$', product_list),
]