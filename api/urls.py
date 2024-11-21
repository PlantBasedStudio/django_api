from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('products/', views.getData, name='products'), #endpoint
    path('products/add', views.addProduct, name='add_product'),
]
