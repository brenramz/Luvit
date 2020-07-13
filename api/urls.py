from django.conf.urls import include, url

urlpatterns = [
    url(r'^product/', include('api.product.urls')),
]
