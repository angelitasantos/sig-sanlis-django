from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants


def register(request):
    messages.add_message(request, constants.ERROR, 'Erro Interno do Sistema.')
    return HttpResponse('Pagina Registrar Usuário Funcionando ...')

def login(request):
    return HttpResponse('Pagina Login Funcionando ...')

def logout(request):
    return HttpResponse('Logou Funcionando ...')