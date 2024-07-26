from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.createProduct, name='createProduct'),
    path('list/', views.listProduct, name='listProduct'),
    path('detail/<str:generate>/', views.detailProduct, name='detailProduct'),
    path('delete/<str:generate>/', views.deleteProduct, name='deleteProduct'),
    path('update/<str:generate>/', views.updateProduct, name='updateProduct'),
]