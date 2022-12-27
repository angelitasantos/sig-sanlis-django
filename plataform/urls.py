from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('parceiros/', views.partners, name='partners'),
    path('novo_parceiro/', views.partner_create, name='partner_create'),
    path('visualizar_parceiro/<int:id>', views.partner_view, name="partner_view"),
    path('alterar_parceiro/<int:id>', views.partner_update, name="partner_update"),
    path('excluir_parceiro/<int:id>', views.partner_delete, name="partner_delete"),
]