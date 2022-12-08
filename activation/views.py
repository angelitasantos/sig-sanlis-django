from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required
from .models import Company
from django.contrib.auth.models import User
from django.contrib import auth
from django.conf import settings
import os
from .utils import password_is_valid, fields_empty, email_html
from .models import TokenUser, Company
from hashlib import sha256


sig = 'SIG SANLIS | '

## Database User
def register(request):
    title = 'Registrar'
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/auth/empresas')
        return render(request, 'user/user_register.html', {'title': title})

    elif request.method == "POST":
        cnpj = request.POST.get('cnpj')
        token_company = request.POST.get('token_company')
        companies = Company.objects.filter(cnpj=cnpj, token_company=token_company)
            
        if not companies.exists():
            messages.add_message(request, constants.ERROR, 'CNPJ e/ou Token Não Conferem !!!')
            return redirect('/auth/registrar/')

        company_id = companies[0].id     
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        users = User.objects.filter(username=username)

        if users.exists():
            messages.add_message(request, constants.ERROR, 'Existe um usuário cadastrado com este nome!!!')
            return redirect('/auth/registrar/')

        if not fields_empty(request, username, email):
            return redirect('/auth/registrar/')

        if not password_is_valid(request, password, confirm_password):
            return redirect('/auth/registrar')
        
        try:
            user = User.objects.create_user(    username=username,
                                                first_name=first_name,
                                                last_name=last_name,
                                                email=email,
                                                password=password,
                                                is_active=False)
            user.save()

            token = sha256(f'{username}{email}'.encode()).hexdigest()
            activation = TokenUser(token=token, user=user, company_id=company_id)
            activation.save()

            path_template = os.path.join(settings.BASE_DIR, 'activation/templates/user/active_account.html')
            email_html(path_template, 'Cadastro confirmado', [email,], username=username, link_activation=f"127.0.0.1:8000/auth/ativar_conta/{token}")
            
            messages.add_message(request, constants.SUCCESS, 'Usuário Cadastrado com Sucesso !!!')
            return redirect('/auth/login')
        except:
            messages.add_message(request, constants.DEBUG, 'Erro Interno do Sistema !!!')
            return redirect('/auth/registrar')


def login(request):
    title = 'Login'
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/empresas')
        return render(request, 'user/user_login.html', {'title': title})
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_filter = User.objects.filter(username=username)

        if not user_filter.exists():
            messages.add_message(request, constants.ERROR, 'Usuário Não Existe !!!')
            return redirect('/auth/login/')

        user_active = User.objects.filter(username=username, is_active=False)

        if user_active.exists():
            messages.add_message(request, constants.ERROR, 'Usuário Não Ativado !!!')
            return redirect('/auth/login/')

        user_auth = auth.authenticate(username=username, password=password)

        if not user_auth:
            messages.add_message(request, constants.ERROR, 'Senha Inválida !!!')
            return redirect('/auth/login')
        else:
            auth.login(request, user_auth)
            return redirect('/auth/empresas')


@login_required(login_url='/auth/login/')
def logout(request):
    auth.logout(request)
    return redirect('/auth/login')


def active_account(request, token):
    token = get_object_or_404(TokenUser, token=token)
    if token.active:
        messages.add_message(request, constants.WARNING, 'Você já ativou sua conta!')
        return redirect('/auth/login')
    user = User.objects.get(username=token.user.username)
    user.is_active = True
    user.save()
    token.active = True
    token.save()
    messages.add_message(request, constants.SUCCESS, 'Conta Ativada com Sucesso!')
    return redirect('/auth/login')


## Database Company
@login_required(login_url='/auth/login/')
def companies(request):
    title = sig + 'Listar Empresas'
    name_filtrar = request.GET.get('name')
    companies = Company.objects.all()
    users = User.objects.all()

    if name_filtrar:
        companies = companies.filter(name__icontains = name_filtrar)

    context =   {   'title': title,
                    'users': users,
                    'companies': companies}
    return render(request, 'company/company_list.html', context)


@login_required(login_url='/auth/login/')
def company_create(request):
    title = sig + 'Criar Empresa'
    if request.method == "GET":
        users = User.objects.all()
        context =   {   'title': title,
                        'users': users}
        return render(request, 'company/company_create.html', context)
    elif request.method == "POST":
        token_company = request.POST.get('token_company')
        name = request.POST.get('name').upper()
        full_name = request.POST.get('full_name').upper()

        start_data = request.POST.get('start_data')
        cnpj = request.POST.get('cnpj')
        insc_est = request.POST.get('insc_est')
        insc_mun = request.POST.get('insc_mun')

        street = request.POST.get('street').upper()
        number1 = request.POST.get('number')
        number = 0 if number1 == "" else request.POST.get('number')
        complement = request.POST.get('complement')
        district = request.POST.get('district').upper()
        city = request.POST.get('city').upper()
        state = request.POST.get('state').upper()
        zipcode = request.POST.get('zipcode')
        google_maps_link = request.POST.get('google_maps_link')

        email = request.POST.get('email').lower()
        phone = request.POST.get('phone')
        whatsapp_number = request.POST.get('whatsapp_number')
        whatsapp_link = request.POST.get('whatsapp_link').lower()

        site_link = request.POST.get('site_link').lower()
        instagram_link = request.POST.get('instagram_link').lower()
        linkedin_link = request.POST.get('linkedin_link').lower()
        facebook_link = request.POST.get('facebook_link').lower()

        if (len(name.strip()) == 0) or (len(full_name.strip()) == 0):
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos!!!')
            return redirect('/auth/nova_empresa/')

        companies = Company.objects.filter(name=name)

        if companies.exists():
            messages.add_message(request, constants.ERROR, 'Já existe uma empresa cadastrada com este nome!!!')
            return redirect('/auth/nova_empresa/')

        try:
            company = Company(  token_company=token_company,
                                name=name,
                                full_name=full_name,

                                start_data=start_data,
                                cnpj=cnpj,
                                insc_est=insc_est,
                                insc_mun=insc_mun,

                                street=street,
                                number=number,
                                complement=complement,
                                district=district,
                                city=city,
                                state=state,
                                zipcode=zipcode,
                                google_maps_link=google_maps_link,

                                email=email,
                                phone=phone,
                                whatsapp_number=whatsapp_number,
                                whatsapp_link=whatsapp_link,

                                site_link=site_link,
                                instagram_link=instagram_link,
                                linkedin_link=linkedin_link,
                                facebook_link=facebook_link,
                                user_company=request.user)
            company.save()

            messages.add_message(request, constants.SUCCESS, 'Empresa Cadastrada com Sucesso!!!')
            return redirect('/auth/nova_empresa/')
        except:
            messages.add_message(request, constants.ERROR, 'Erro Interno do Sistema!!!')
            return redirect('/auth/nova_empresa/')


@login_required(login_url='/auth/login/')
def company_view(request, id):
    title = sig + 'Visualizar Empresa'
    users = User.objects.all()
    company = get_object_or_404(Company, id=id)
    companies = Company.objects.all()
    return render(request, 'company/company_view.html', {   'title': title,
                                                            'users': users,
                                                            'company': company,
                                                            'companies': companies})


@login_required(login_url='/auth/login/')
def company_update(request, id):
    title = sig + 'Alterar Empresa'
    users = User.objects.all()
    company = get_object_or_404(Company, id=id)
    companies = Company.objects.all()
    
    if request.method == "GET":
        return render(request, 'company/company_update.html', { 'title': title,
                                                                'users': users,
                                                                'company': company,
                                                                'companies': companies})
    elif request.method == "POST":
        messages.add_message(request, constants.ERROR, 'Página em Construção!!!')
        return render(request, 'company/company_update.html', { 'title': title,
                                                                'users': users,
                                                                'company': company,
                                                                'companies': companies})


@login_required(login_url='/auth/login/')
def company_delete(request, id):
    company = Company.objects.get(id=id)
    company.delete()
    messages.add_message(request, constants.SUCCESS, 'Empresa Excluída com Sucesso!')
    return redirect('/auth/empresas')