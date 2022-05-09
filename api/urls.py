from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='home'),
    path('products-list/', views.products_list, name='products-list'),
    path('detail-view/<str:pk>/', views.get_detail_product, name='get_detail_product'),
    path('create-product/', views.create_new_product, name='create_new_product'),
    path('update-product/<str:pk>/', views.update_product, name='update_product'),
    path('delete_product/<str:pk>/', views.delete_product, name='delete_product'),
    ]
