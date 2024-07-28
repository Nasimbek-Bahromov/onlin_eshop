from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.myCart, name='cart_detail'),
    path('cart/add/<str:generate_code>/<int:quantity>/', views.addProductToCart, name='add_product_to_cart'),
    path('cart/substract/<str:generate_code>/<int:quantity>/', views.substractProductFromCart, name='substract_product_from_cart'),
    path('cart/delete/<str:generate_code>/', views.deleteProductCart, name='delete_product_from_cart'),
    path('order/create/', views.CreateOrder, name='create_order'),
]
