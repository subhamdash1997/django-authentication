from django.urls import path, include
from django.shortcuts import redirect
# from .views import list_products, list_messages
# from .views import Products,ProductDetailView
# from .views import ListProductMixins,DetailedProductMixins
from .views import ListProductGenerics,DetailedProductGenerics

urlpatterns = [
    path('', lambda request: redirect('pgl'), name='home'),
    # path('products/', list_products, name='product-list'),
    # path('messages/', list_messages, name='message-list'),
    # path('products/',Products.as_view(),name='product-list'),
    # path('products/<pid>/',ProductDetailView.as_view(),name='product-detail'),
    # path('mixinpath/',ListProductMixins.as_view(),name='mp'),
    # path('product-mixin/<pk>/',DetailedProductMixins.as_view(),name='mdp'),
    path('product-generic-list/',ListProductGenerics.as_view(),name='pgl'),
    path('product-generic-detail/<pk>/',DetailedProductGenerics.as_view(),name='pgd'),
    
]