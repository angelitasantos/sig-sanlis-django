from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.models import User
from activation.models import TokenUser, Company
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants

from plataform.models import Partner
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, resolve_url


sig = 'SIG SANLIS | '

# List
@login_required(login_url='/auth/login/')
def sale_list(request):
    users = User.objects.all()
    user_login = User.objects.filter(username=request.user)
    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')

    if user_token_company.exists():
        return HttpResponse("está funcionando")
    
    elif user_token_company_id.count() == 0:
        messages.add_message(request, constants.ERROR, 'Não encontramos uma empresa para o seu usuário !!!')
        context =   {   'users': users,
                        'user_login': user_login[0]}
        return redirect('/painel/')


@login_required(login_url='/auth/login/')
def service_list(request):
    pass
    

@login_required(login_url='/auth/login/')
def shopping_list(request):
    pass
    

@login_required(login_url='/auth/login/')
def production_list(request):
    pass
    

@login_required(login_url='/auth/login/')
def inventary_list(request):
    pass
    

# Create
@login_required(login_url='/auth/login/')
def transaction_new(request, template_name, movimento, url, title, subtitle):
    pass


@login_required(login_url='/auth/login/')
def sale_new(request):
    pass


@login_required(login_url='/auth/login/')
def service_new(request):
    pass


@login_required(login_url='/auth/login/')
def shopping_new(request):
    pass


@login_required(login_url='/auth/login/')
def production_new(request):
    pass


@login_required(login_url='/auth/login/')
def inventary_new(request):
    pass


# View
@login_required(login_url='/auth/login/')
def sale_detail(request, id):
    return HttpResponse('transactions_form_sale.html')


@login_required(login_url='/auth/login/')
def service_detail(request, id):
    return HttpResponse('transactions_form_service.html')


@login_required(login_url='/auth/login/')
def shopping_detail(request, id):
    return HttpResponse('transactions_form_shopping.html')


@login_required(login_url='/auth/login/')
def production_detail(request, id):
    return HttpResponse('transactions_form_production.html')


@login_required(login_url='/auth/login/')
def inventary_detail(request, id):
    return HttpResponse('transactions_form_inventary.html')
