from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.detailed_product, name='detailed_product'),
    path('add/', views.add_product, name='add_product'),
]
