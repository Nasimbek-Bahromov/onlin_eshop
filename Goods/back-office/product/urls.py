from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.createProduct, name='createProduct'),
    path('list/', views.listProduct, name='listProduct'),
    path('detail/<str:generate>/', views.detailProduct, name='detailProduct'),
    path('delete/<str:generate>/', views.deleteProduct, name='deleteProduct'),
    path('update/<str:generate>/', views.updateProduct, name='updateProduct'),
    path('product-enter/<str:generate>/', views.update_product_enter, name='update_product_enter'),
    path('product-enter/', views.product_enter_list, name='product_enter_list'),
    path('product_enter/create/', views.create_product_enter, name='create_product_enter'),
    path('product-enter/detail/<str:generate>/', views.product_enter_detail, name='product_enter_detail'),
]
