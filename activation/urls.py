from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('sair/', views.logout, name='logout'),
]