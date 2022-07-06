from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRouters),
    path('products/', views.getProducts),
    path('products/create/', views.postProduct),
    path('products/edit/<str:pk>/', views.putProduct),
    path('products/warehouses/', views.getWarehouse),
]
