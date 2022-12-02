from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    title = 'Home'
    return render(request, 'index.html', {'title': title})


def about(request):
    title = 'Sobre'
    return render(request, 'about.html', {'title': title})


def contact(request):
    title = 'Contato'
    return render(request, 'contact.html', {'title': title})