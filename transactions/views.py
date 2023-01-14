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
from .models import Transaction, TransactionItems
from .forms import TransactionForm, TransactionItemsForm


sig = 'SIG SANLIS | '

# List
@login_required(login_url='/auth/login/')
def sale_list(request):
    users = User.objects.all()
    user_login = User.objects.filter(username=request.user)
    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')

    if user_token_company.exists():
        template_name = 'transaction_list.html'
        objects = Transaction.objects.all()
        context = {
            'object_list': objects,
            'users': users,
            'user_login': user_login[0],
            'title': sig + 'Vendas',
            'subtitle': 'Vendas',
            'url_add': 'transactions:sale_new'
        }
        return render(request, template_name, context)
    
    elif user_token_company_id.count() == 0:
        messages.add_message(request, constants.ERROR, 'Não encontramos uma empresa para o seu usuário !!!')
        context =   {   'users': users,
                        'user_login': user_login[0]}
        return redirect('/painel/')


@login_required(login_url='/auth/login/')
def service_list(request):
    users = User.objects.all()
    user_login = User.objects.filter(username=request.user)
    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')

    if user_token_company.exists():
        template_name = 'transaction_list.html'
        objects = Transaction.objects.all()
        context = {
            'object_list': objects,
            'users': users,
            'user_login': user_login[0],
            'title': sig + 'Serviços',
            'subtitle': 'Serviços',
            'url_add': 'transactions:service_new'
        }
        return render(request, template_name, context)

    elif user_token_company_id.count() == 0:
        messages.add_message(request, constants.ERROR, 'Não encontramos uma empresa para o seu usuário !!!')
        context =   {   'users': users,
                        'user_login': user_login[0]}
        return redirect('/painel/')
    

@login_required(login_url='/auth/login/')
def shopping_list(request):
    users = User.objects.all()
    user_login = User.objects.filter(username=request.user)
    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')

    if user_token_company.exists():
        template_name = 'transaction_list.html'
        objects = Transaction.objects.all()
        context = {
            'object_list': objects,
            'users': users,
            'user_login': user_login[0],
            'title': sig + 'Compras',
            'subtitle': 'Compras',
            'url_add': 'transactions:shopping_new'
        }
        return render(request, template_name, context)

    elif user_token_company_id.count() == 0:
        messages.add_message(request, constants.ERROR, 'Não encontramos uma empresa para o seu usuário !!!')
        context =   {   'users': users,
                        'user_login': user_login[0]}
        return redirect('/painel/')
    

@login_required(login_url='/auth/login/')
def production_list(request):
    users = User.objects.all()
    user_login = User.objects.filter(username=request.user)
    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')

    if user_token_company.exists():
        template_name = 'transaction_list.html'
        objects = Transaction.objects.all()
        context = {
            'object_list': objects,
            'users': users,
            'user_login': user_login[0],
            'title': sig + 'Produção',
            'subtitle': 'Produção',
            'url_add': 'transactions:production_new'
        }
        return render(request, template_name, context)

    elif user_token_company_id.count() == 0:
        messages.add_message(request, constants.ERROR, 'Não encontramos uma empresa para o seu usuário !!!')
        context =   {   'users': users,
                        'user_login': user_login[0]}
        return redirect('/painel/')
    

@login_required(login_url='/auth/login/')
def inventary_list(request):
    users = User.objects.all()
    user_login = User.objects.filter(username=request.user)
    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')

    if user_token_company.exists():
        template_name = 'transaction_list.html'
        objects = Transaction.objects.all()
        context = {
            'object_list': objects,
            'users': users,
            'user_login': user_login[0],
            'title': sig + 'Inventário',
            'subtitle': 'Inventário',
            'url_add': 'transactions:inventary_new'
        }
        return render(request, template_name, context)

    elif user_token_company_id.count() == 0:
        messages.add_message(request, constants.ERROR, 'Não encontramos uma empresa para o seu usuário !!!')
        context =   {   'users': users,
                        'user_login': user_login[0]}
        return redirect('/painel/')
    

# Create
@login_required(login_url='/auth/login/')
def transaction_new(request, template_name, movimento, url, title, subtitle):
    users = User.objects.all()
    user_login = User.objects.filter(username=request.user)
    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')

    if user_token_company.exists():
        estoque_form = Transaction()
        item_estoque_formset = inlineformset_factory(
            Transaction,
            TransactionItems,
            form=TransactionItemsForm,
            extra=0,
            can_delete=False,
            min_num=1,
            validate_min=True,
        )
        if request.method == 'POST':
            form = TransactionForm(request.POST, instance=estoque_form, prefix='main')
            formset = item_estoque_formset(
                request.POST,
                instance=estoque_form,
                prefix='estoque'
            )
            if form.is_valid() and formset.is_valid():
                form = form.save()
                form.movimento = movimento
                form.save()
                formset.save()
                return {'id': form.id}
        else:
            form = TransactionForm(instance=estoque_form, prefix='main')
            formset = item_estoque_formset(instance=estoque_form, prefix='estoque')

        context = { 'form': form, 
                    'formset': formset,
                    'title': title[0],
                    'subtitle': subtitle[0],
                    'users': users,
                    'user_login': user_login[0],
                    }
        return context
    
    elif user_token_company_id.count() == 0:
        messages.add_message(request, constants.ERROR, 'Não encontramos uma empresa para o seu usuário !!!')
        context =   {   'users': users,
                        'user_login': user_login[0]}
        return redirect('/painel/')


@login_required(login_url='/auth/login/')
def sale_new(request):
    template_name = 'transaction_form_sale.html'
    movimento = 'S'
    url = 'transactions:sale_detail'
    title = sig + 'Vendas',
    subtitle = 'Vendas',
    context = transaction_new(request, template_name, movimento, url, title, subtitle)
    if context.get('id'):
        return HttpResponseRedirect(resolve_url(url, context.get('id')))
    return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def service_new(request):
    template_name = 'transaction_form_service.html'
    movimento = 'S'
    url = 'transactions:service_detail'
    title = sig + 'Serviços',
    subtitle = 'Serviços',
    context = transaction_new(request, template_name, movimento, url, title, subtitle)
    if context.get('id'):
        return HttpResponseRedirect(resolve_url(url, context.get('id')))
    return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def shopping_new(request):
    template_name = 'transaction_form_shopping.html'
    movimento = 'E'
    url = 'transactions:shopping_detail'
    title = sig + 'Compras',
    subtitle = 'Compras',
    context = transaction_new(request, template_name, movimento, url, title, subtitle)
    if context.get('id'):
        return HttpResponseRedirect(resolve_url(url, context.get('id')))
    return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def production_new(request):
    template_name = 'transaction_form_production.html'
    movimento = 'E'
    url = 'transactions:production_detail'
    title = sig + 'Produção',
    subtitle = 'Produção',
    context = transaction_new(request, template_name, movimento, url, title, subtitle)
    if context.get('id'):
        return HttpResponseRedirect(resolve_url(url, context.get('id')))
    return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def inventary_new(request):
    template_name = 'transaction_form_inventary.html'
    movimento = 'E'
    url = 'transactions:inventary_detail'
    title = sig + 'Inventário',
    subtitle = 'Inventário',
    context = transaction_new(request, template_name, movimento, url, title, subtitle)
    if context.get('id'):
        return HttpResponseRedirect(resolve_url(url, context.get('id')))
    return render(request, template_name, context)


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
