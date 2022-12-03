from django.shortcuts import render
from django.http import HttpResponse

def register(request):
    return HttpResponse('Pagina Registrar Usuário Funcionando ...')

def login(request):
    return HttpResponse('Pagina Login Funcionando ...')

def logout(request):
    return HttpResponse('Logou Funcionando ...')