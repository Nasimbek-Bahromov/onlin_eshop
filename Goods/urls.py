from django.urls import path, include
from Goods import views

urlpatterns = [
    path('', views.main, name='index'),
    path('authentication/', include('Goods.authentication.urls')),
    path('back-office/', include('Goods.back-office.urls')),
    path('admin/', views.admin_page, name='admin_page'),
]