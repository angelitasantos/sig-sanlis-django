from django.shortcuts import render, redirect, resolve_url
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from activation.models import TokenUser, Company
from plataform.models import Item, Partner
from .models import (   
                        Estoque,
                        StockSale, 
                        StockService,
                        StockShopping,
                        StockProduction,
                        StockInventary,
                        EstoqueItens
                    )
from .forms import EstoqueForm, EstoqueItensEntradaForm, EstoqueItensSaidaForm


sig = 'SIG SANLIS | '

#######################################################
@login_required(login_url='/auth/login/')
def stock_sale_list(request):
    title = sig + 'Vendas'
    subtitle = 'Vendas'
    users = User.objects.all()
    user_login = User.objects.filter(username=request.user)
    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    company_id_value = user_token_company_id[0][0]
    
    if user_token_company.exists():
        template_name = 'stock_sale_list.html'
        objects = StockSale.objects.filter(company_id=company_id_value)
        context =   {
                        'title': title,
                        'subtitle': subtitle,
                        'users': users,
                        'user_login': user_login[0],
                        'object_list': objects
                    }
        return render(request, template_name, context)
    
    elif user_token_company_id.count() == 0:
        messages.add_message(request, constants.ERROR, 'Não encontramos uma empresa para o seu usuário !!!')
        context =   {   'title': title,
                        'users': users,
                        'user_login': user_login[0]}
        return redirect('/painel/')

    return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def stock_service_list(request):
    title = sig + 'Serviços'
    subtitle = 'Serviços'
    users = User.objects.all()
    user_login = User.objects.filter(username=request.user)
    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    company_id_value = user_token_company_id[0][0]
    
    if user_token_company.exists():
        template_name = 'stock_service_list.html'
        objects = StockService.objects.filter(company_id=company_id_value)
        context =   {
                        'title': title,
                        'subtitle': subtitle,
                        'users': users,
                        'user_login': user_login[0],
                        'object_list': objects
                    }
        return render(request, template_name, context)
    
    elif user_token_company_id.count() == 0:
        messages.add_message(request, constants.ERROR, 'Não encontramos uma empresa para o seu usuário !!!')
        context =   {   'title': title,
                        'users': users,
                        'user_login': user_login[0]}
        return redirect('/painel/')

    return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def stock_shopping_list(request):
    title = sig + 'Compras'
    subtitle = 'Compras'
    users = User.objects.all()
    user_login = User.objects.filter(username=request.user)
    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    company_id_value = user_token_company_id[0][0]
    
    if user_token_company.exists():
        template_name = 'stock_shopping_list.html'
        objects = StockShopping.objects.filter(company_id=company_id_value)
        context =   {
                        'title': title,
                        'subtitle': subtitle,
                        'users': users,
                        'user_login': user_login[0],
                        'object_list': objects
                    }
        return render(request, template_name, context)
    
    elif user_token_company_id.count() == 0:
        messages.add_message(request, constants.ERROR, 'Não encontramos uma empresa para o seu usuário !!!')
        context =   {   'title': title,
                        'users': users,
                        'user_login': user_login[0]}
        return redirect('/painel/')

    return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def stock_production_list(request):
    title = sig + 'Produção'
    subtitle = 'Produção'
    users = User.objects.all()
    user_login = User.objects.filter(username=request.user)
    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    company_id_value = user_token_company_id[0][0]
    
    if user_token_company.exists():
        template_name = 'stock_production_list.html'
        objects = StockProduction.objects.filter(company_id=company_id_value)
        context =   {
                        'title': title,
                        'subtitle': subtitle,
                        'users': users,
                        'user_login': user_login[0],
                        'object_list': objects
                    }
        return render(request, template_name, context)
    
    elif user_token_company_id.count() == 0:
        messages.add_message(request, constants.ERROR, 'Não encontramos uma empresa para o seu usuário !!!')
        context =   {   'title': title,
                        'users': users,
                        'user_login': user_login[0]}
        return redirect('/painel/')

    return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def stock_inventary_list(request):
    title = sig + 'Inventário'
    subtitle = 'Inventário'
    users = User.objects.all()
    user_login = User.objects.filter(username=request.user)
    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    company_id_value = user_token_company_id[0][0]
    
    if user_token_company.exists():
        template_name = 'stock_inventary_list.html'
        objects = StockInventary.objects.filter(company_id=company_id_value)
        context =   {
                        'title': title,
                        'subtitle': subtitle,
                        'users': users,
                        'user_login': user_login[0],
                        'object_list': objects
                    }
        return render(request, template_name, context)
    
    elif user_token_company_id.count() == 0:
        messages.add_message(request, constants.ERROR, 'Não encontramos uma empresa para o seu usuário !!!')
        context =   {   'title': title,
                        'users': users,
                        'user_login': user_login[0]}
        return redirect('/painel/')

    return render(request, template_name, context)


#######################################################
@login_required(login_url='/auth/login/')
def stock_sale_detail(request, pk):
    title = sig + 'Vendas'
    subtitle = 'Vendas'
    users = User.objects.all()
    user_login = User.objects.filter(username=request.user)
    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    
    if user_token_company.exists():
        template_name = 'stock_sale_detail.html'
        obj = StockSale.objects.get(pk=pk)
        context =   {
                            'title': title,
                            'subtitle': subtitle,
                            'users': users,
                            'user_login': user_login[0],
                            'object': obj
                        }
        return render(request, template_name, context)

    elif user_token_company_id.count() == 0:
        messages.add_message(request, constants.ERROR, 'Não encontramos uma empresa para o seu usuário !!!')
        context =   {   'title': title,
                        'users': users,
                        'user_login': user_login[0]}
        return redirect('/painel/')
    
    return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def stock_service_detail(request, pk):
    title = sig + 'Serviços'
    subtitle = 'Serviços'
    users = User.objects.all()
    user_login = User.objects.filter(username=request.user)
    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    
    if user_token_company.exists():
        template_name = 'stock_service_detail.html'
        obj = StockService.objects.get(pk=pk)
        context =   {
                            'title': title,
                            'subtitle': subtitle,
                            'users': users,
                            'user_login': user_login[0],
                            'object': obj
                        }
        return render(request, template_name, context)

    elif user_token_company_id.count() == 0:
        messages.add_message(request, constants.ERROR, 'Não encontramos uma empresa para o seu usuário !!!')
        context =   {   'title': title,
                        'users': users,
                        'user_login': user_login[0]}
        return redirect('/painel/')
    
    return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def stock_shopping_detail(request, pk):
    title = sig + 'Compras'
    subtitle = 'Compras'
    users = User.objects.all()
    user_login = User.objects.filter(username=request.user)
    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    
    if user_token_company.exists():
        template_name = 'stock_shopping_detail.html'
        obj = StockShopping.objects.get(pk=pk)
        context =   {
                            'title': title,
                            'subtitle': subtitle,
                            'users': users,
                            'user_login': user_login[0],
                            'object': obj
                        }
        return render(request, template_name, context)

    elif user_token_company_id.count() == 0:
        messages.add_message(request, constants.ERROR, 'Não encontramos uma empresa para o seu usuário !!!')
        context =   {   'title': title,
                        'users': users,
                        'user_login': user_login[0]}
        return redirect('/painel/')
    
    return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def stock_production_detail(request, pk):
    title = sig + 'Produção'
    subtitle = 'Produção'
    users = User.objects.all()
    user_login = User.objects.filter(username=request.user)
    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    
    if user_token_company.exists():
        template_name = 'stock_production_detail.html'
        obj = StockProduction.objects.get(pk=pk)
        context =   {
                            'title': title,
                            'subtitle': subtitle,
                            'users': users,
                            'user_login': user_login[0],
                            'object': obj
                        }
        return render(request, template_name, context)

    elif user_token_company_id.count() == 0:
        messages.add_message(request, constants.ERROR, 'Não encontramos uma empresa para o seu usuário !!!')
        context =   {   'title': title,
                        'users': users,
                        'user_login': user_login[0]}
        return redirect('/painel/')
    
    return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def stock_inventary_detail(request, pk):
    title = sig + 'Inventário'
    subtitle = 'Inventário'
    users = User.objects.all()
    user_login = User.objects.filter(username=request.user)
    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    
    if user_token_company.exists():
        template_name = 'stock_inventary_detail.html'
        obj = StockInventary.objects.get(pk=pk)
        context =   {
                            'title': title,
                            'subtitle': subtitle,
                            'users': users,
                            'user_login': user_login[0],
                            'object': obj
                        }
        return render(request, template_name, context)

    elif user_token_company_id.count() == 0:
        messages.add_message(request, constants.ERROR, 'Não encontramos uma empresa para o seu usuário !!!')
        context =   {   'title': title,
                        'users': users,
                        'user_login': user_login[0]}
        return redirect('/painel/')
    
    return render(request, template_name, context)


#######################################################
@login_required(login_url='/auth/login/')
def stock_add(request, template_name, movimento, tipo_movimento, url, title, subtitle):
    users = User.objects.all()
    user_login = User.objects.filter(username=request.user)
    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    company_id_value = user_token_company_id[0][0]
    
    if user_token_company.exists():
        estoque_form = Estoque()
        item_estoque_formset = inlineformset_factory(
            Estoque,    
            EstoqueItens,
            form=EstoqueItensSaidaForm,
            extra=0,
            min_num=1,
            validate_min=True,
        )
        if request.method == 'POST':
            form = EstoqueForm(request.POST, instance=estoque_form, prefix='main')
            formset = item_estoque_formset(
                request.POST,
                instance=estoque_form,
                prefix='estoque'
            )
            if form.is_valid() and formset.is_valid():
                form = form.save(commit=False)
                form.funcionario = request.user
                form.movimento = movimento
                form.tipo_movimento = tipo_movimento
                form.save()
                formset.save()
                stock_moviment(form)
                return {'pk': form.pk}
        else:
            form = EstoqueForm(instance=estoque_form, prefix='main')
            formset = item_estoque_formset(instance=estoque_form, prefix='estoque')
        context =   {
                        'form': form, 
                        'formset': formset,
                        'title': title, 
                        'subtitle': subtitle,
                    }
        return context  
    elif user_token_company_id.count() == 0:
        messages.add_message(request, constants.ERROR, 'Não encontramos uma empresa para o seu usuário !!!')
        context =   {   
                        'users': users,
                        'user_login': user_login[0]
                    }
        return redirect('/painel/')
    
    return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def stock_sale_add(request):
    title = sig + 'Vendas'
    subtitle = 'Vendas'
    template_name = 'stock_sale_form.html'
    url = 'stock:stock_sale_detail'
    movimento = 'S'
    tipo_movimento = 'V'

    context = stock_add(request, template_name, movimento, tipo_movimento, url, title, subtitle)
    if context.get('pk'):
        return HttpResponseRedirect(resolve_url(url, context.get('pk')))
    return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def stock_service_add(request):
    title = sig + 'Serviços'
    subtitle = 'Serviços'
    template_name = 'stock_service_form.html'
    url = 'stock:stock_service_detail'
    movimento = 'S'
    tipo_movimento = 'S'

    context = stock_add(request, template_name, movimento, tipo_movimento, url, title, subtitle)
    if context.get('pk'):
        return HttpResponseRedirect(resolve_url(url, context.get('pk')))
    return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def stock_shopping_add(request):
    title = sig + 'Compras'
    subtitle = 'Compras'
    template_name = 'stock_shopping_form.html'
    url = 'stock:stock_shopping_detail'
    movimento = 'E'
    tipo_movimento = 'C'

    context = stock_add(request, template_name, movimento, tipo_movimento, url, title, subtitle)
    if context.get('pk'):
        return HttpResponseRedirect(resolve_url(url, context.get('pk')))
    return render(request, template_name, context)
        

@login_required(login_url='/auth/login/')
def stock_production_add(request):
    title = sig + 'Produção'
    subtitle = 'Produção'
    template_name = 'stock_production_form.html'
    url = 'stock:stock_production_detail'
    movimento = 'E'
    tipo_movimento = 'P'

    context = stock_add(request, template_name, movimento, tipo_movimento, url, title, subtitle)
    if context.get('pk'):
        return HttpResponseRedirect(resolve_url(url, context.get('pk')))
    return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def stock_inventary_add(request):
    title = sig + 'Inventário'
    subtitle = 'Inventário'
    template_name = 'stock_inventary_form.html'
    url = 'stock:stock_inventary_detail'
    movimento = 'E'
    tipo_movimento = 'I'

    context = stock_add(request, template_name, movimento, tipo_movimento, url, title, subtitle)
    if context.get('pk'):
        return HttpResponseRedirect(resolve_url(url, context.get('pk')))
    return render(request, template_name, context)


def stock_moviment(form):
    # Pega os produtos a partir da instância do formulário (Estoque).
    produtos = form.estoques.all()
    for item in produtos:
        produto = Item.objects.get(pk=item.produto.pk)
        produto.stock_qtd = item.saldo
        produto.save()
    print('Estoque atualizado com sucesso.')

