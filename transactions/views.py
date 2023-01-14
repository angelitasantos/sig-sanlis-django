from django.shortcuts import render
from plataform.models import Partner
from django.http import HttpResponse


sig = 'SIG SANLIS | '

def sale_list(request):
    template_name = 'transaction_list.html'
    objects = Partner.objects.all()
    context = {
        'object_list': objects,
        'title': sig + 'Vendas',
        'subtitle': 'Vendas',
        'url_add': 'transactions:sale_new'
    }
    return render(request, template_name, context)


def service_list(request):
    template_name = 'transaction_list.html'
    objects = Partner.objects.all()
    context = {
        'object_list': objects,
        'title': sig + 'Serviços',
        'subtitle': 'Serviços',
        'url_add': 'transactions:service_new'
    }
    return render(request, template_name, context)


def shopping_list(request):
    template_name = 'transaction_list.html'
    objects = Partner.objects.all()
    context = {
        'object_list': objects,
        'title': sig + 'Compras',
        'subtitle': 'Compras',
        'url_add': 'transactions:shopping_new'
    }
    return render(request, template_name, context)


def production_list(request):
    template_name = 'transaction_list.html'
    objects = Partner.objects.all()
    context = {
        'object_list': objects,
        'title': sig + 'Produção',
        'subtitle': 'Produção',
        'url_add': 'transactions:production_new'
    }
    return render(request, template_name, context)


def inventary_list(request):
    template_name = 'transaction_list.html'
    objects = Partner.objects.all()
    context = {
        'object_list': objects,
        'title': sig + 'Inventário',
        'subtitle': 'Inventário',
        'url_add': 'transactions:inventary_new'
    }
    return render(request, template_name, context)


def sale_new(request):
    return HttpResponse('transactions_form_sale.html')


def service_new(request):
    return HttpResponse('transactions_form_service.html')


def shopping_new(request):
    return HttpResponse('transactions_form_shopping.html')


def production_new(request):
    return HttpResponse('transactions_form_production.html')


def inventary_new(request):
    return HttpResponse('transactions_form_inventary.html')


def sale_detail(request, id):
    return HttpResponse('transactions_form_sale.html')


def service_detail(request, id):
    return HttpResponse('transactions_form_service.html')


def shopping_detail(request, id):
    return HttpResponse('transactions_form_shopping.html')


def production_detail(request, id):
    return HttpResponse('transactions_form_production.html')


def inventary_detail(request, id):
    return HttpResponse('transactions_form_inventary.html')
