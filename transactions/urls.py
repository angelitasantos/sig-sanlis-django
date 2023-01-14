from django.urls import path, include
from . import views

app_name = 'transactions'


sale_patterns = [
    path('', views.sale_list, name='sale_list'),
    path('incluir/', views.sale_new, name='sale_new'),
    path('<int:pk>/', views.sale_detail, name='sale_detail'),
]

service_patterns = [
    path('', views.service_list, name='service_list'),
    path('incluir/', views.service_new, name='service_new'),
    path('<int:pk>/', views.service_detail, name='service_detail'),
]

shopping_patterns = [
    path('', views.shopping_list, name='shopping_list'),
    path('incluir/', views.shopping_new, name='shopping_new'),
    path('<int:pk>/', views.shopping_detail, name='shopping_detail'),
]

production_patterns = [
    path('', views.production_list, name='production_list'),
    path('incluir/', views.production_new, name='production_new'),
    path('<int:pk>/', views.production_detail, name='production_detail'),
]

inventary_patterns = [
    path('', views.inventary_list, name='inventary_list'),
    path('incluir/', views.inventary_new, name='inventary_new'),
    path('<int:pk>/', views.sale_detail, name='sale_detail'),
]


urlpatterns = [
    path('vendas/', include(sale_patterns)),
    path('servicos/', include(service_patterns)),
    path('compras/', include(shopping_patterns)),
    path('producao/', include(production_patterns)),
    path('inventario/', include(inventary_patterns)),
]
