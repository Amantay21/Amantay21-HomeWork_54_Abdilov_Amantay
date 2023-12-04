from django.urls import path
from webapp.views import index_view, delete_product, create_product, product_view, create_category

urlpatterns = [
    path('', index_view, name='index'),
    path('product/add/', create_product, name='product_create'),
    path('product/<int:pk>', product_view, name='product_view'),
    path('product/delete/', delete_product, name='delete_product'),
    path('category/add/', create_category, name='category_create')
]