from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

sig = 'SIG SANLIS | '


def dashboard(request):
    title = sig + 'Painel'
    user_login = User.objects.filter(username=request.user)

    context =   {   'title': title,
                    'user_login': user_login[0]}

    return render(request, 'painel.html', context)
