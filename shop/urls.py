from django.conf.urls import  url

urlpatterns = [
    url(r'^find/product/$','shop.views.find_product', name='find-product'),
]
