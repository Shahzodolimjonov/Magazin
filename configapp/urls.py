from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.shop_list, name='shop-list'),
    path('product/', views.product_list, name='product-list'),
    path('category/', views.category_list, name='category-list'),
]
