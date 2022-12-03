from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required
from .models import Company

sig = 'SIG SANLIS | '


def register(request):
    messages.add_message(request, constants.ERROR, 'Erro Interno do Sistema.')
    return HttpResponse('Pagina Registrar Usuário Funcionando ...')

def login(request):
    return HttpResponse('Pagina Login Funcionando ...')

def logout(request):
    return HttpResponse('Sair Funcionando ...')


## Database Company
@login_required(login_url='/auth/login/')
def companies(request):
    title = sig + 'Empresas'
    companies = Company.objects.all()

    context =   {   'title': title,
                    'companies': companies}
    return render(request, 'company/company_list.html', context)


@login_required(login_url='/auth/login/')
def company_create(request):
    title = sig + 'Empresa'
    if request.method == "GET":
        return render(request, 'company/company_create.html', {'title': title})
    elif request.method == "POST":
        return redirect('/auth/nova_empresa')


@login_required(login_url='/auth/login/')
def company_view(request, id):
    title = sig + 'Empresa'
    company = get_object_or_404(Company, id=id)
    companies = Company.objects.all()
    return render(request, 'company/company_view.html', {   'title': title,
                                                            'company': company,
                                                            'companies': companies})


@login_required(login_url='/auth/login/')
def company_update(request, id):
    title = sig + 'Empresa'
    company = get_object_or_404(Company, id=id)
    companies = Company.objects.all()
    return render(request, 'company/company_update.html', { 'title': title,
                                                            'company': company,
                                                            'companies': companies})


@login_required(login_url='/auth/login/')
def company_delete(request, id):
    company = Company.objects.get(id=id)
    company.delete()
    messages.add_message(request, constants.SUCCESS, 'Empresa Excluída com Sucesso!')
    return redirect('auth/empresas')