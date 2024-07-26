from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.listCategory, name='listCategory'),
    path('detail/<str:generate>/', views.detailCategory, name='detailCategory'),
    path('update/', views.updateCategory, name='updateCategory'),  
    path('delete/<str:generate>/', views.deleteCategory, name='deleteCategory'),
    path('create/', views.createCategory, name='createCategory'),
]