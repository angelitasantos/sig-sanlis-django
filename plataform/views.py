from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from activation.models import TokenUser, Company
from .models import Partner

sig = 'SIG SANLIS | '


@login_required(login_url='/auth/login/')
def dashboard(request):
    title = sig + 'Painel'
    user_login = User.objects.filter(username=request.user)

    context =   {   'title': title,
                    'user_login': user_login[0]}

    return render(request, 'painel.html', context)


# Partners
@login_required(login_url='/auth/login/')
def partners(request):
    title = sig + 'Listar Parceiros'

    users = User.objects.all()
    user_login = User.objects.filter(username=request.user)
    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    
    if user_token_company.exists():
        nickname_filtrar = request.GET.get('nickname')
        user_token_company_id_value = user_token_company_id[0][0]
        partners = Partner.objects.filter(company_id=user_token_company_id_value)
        
        if nickname_filtrar:
            partners = partners.filter(nickname__icontains = nickname_filtrar)

        context =   {   'title': title,
                        'users': users,
                        'partners': partners,
                        'user_login': user_login[0]}
        render(request, 'partners/partner_list.html', context)

    elif user_token_company_id.count() == 0:
        messages.add_message(request, constants.ERROR, 'Não encontramos uma empresa para o seu usuário !!!')
        context =   {   'title': title,
                        'users': users,
                        'user_login': user_login[0]}
        return redirect('/painel/')

    return render(request, 'partners/partner_list.html', context)


@login_required(login_url='/auth/login/')
def partner_create(request):
    title = sig + 'Criar Parceiro'
    user_login = User.objects.filter(username=request.user)
    users = User.objects.all()

    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    company_id_value = user_token_company_id[0][0]
    
    context =   {   'title': title,
                    'user_login': user_login[0],
                    'company_id_value': company_id_value,
                    'users': users}
    if request.method == "GET":
        return render(request, 'partners/partner_create.html', context)
    elif request.method == "POST":
        nickname = request.POST.get('nickname').upper()
        first_name = request.POST.get('first_name').upper()
        last_name = request.POST.get('last_name').upper()
        document = request.POST.get('document')
        email = request.POST.get('email').lower()
        phone1 = request.POST.get('phone1')
        phone2 = request.POST.get('phone2')

        company = request.POST.get('company')
        type_partners = request.POST.get('type_partners')
        type_person = request.POST.get('type_person')
        gender = request.POST.get('gender')
        status = "A"

        if (len(nickname.strip()) == 0):
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos!!!')
            return render(request, 'partners/partner_create.html', context)

        partners = Partner.objects.filter(nickname=nickname)

        if partners.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um parceiro cadastrado com este nome!!!')
            return render(request, 'partners/partner_create.html', context)

        partner = Partner(  nickname=nickname,
                            first_name=first_name,
                            last_name=last_name,

                            document=document,
                            phone1=phone1,
                            phone2=phone2,
                            email=email,

                            company_id=company,
                            type_partners=type_partners,
                            type_person=type_person,
                            gender=gender,
                            status=status
                            )
        partner.save()

        messages.add_message(request, constants.SUCCESS, 'Parceiro Cadastrado com Sucesso!!!')
        return render(request, 'partners/partner_create.html', context)


@login_required(login_url='/auth/login/')
def partner_view(request, id):
    title = sig + 'Visualizar Parceiro'
    user_login = User.objects.filter(username=request.user)

    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    company_id_value = user_token_company_id[0][0]

    partners_exists = Partner.objects.filter(id=id, company_id=company_id_value)
    if not partners_exists.exists():
        messages.add_message(request, constants.ERROR, 'Você não tem acesso a este identificador !!!')
        return redirect('/painel/parceiros')

    users = User.objects.all()
    partner = get_object_or_404(Partner, id=id)
    partners = Partner.objects.filter(company_id=company_id_value)

    return render(request, 'partners/partner_update.html', { 'title': title,
                                                            'users': users,
                                                            'user_login': user_login[0],
                                                            'company_id_value': company_id_value,
                                                            'partner': partner,
                                                            'partners': partners})


@login_required(login_url='/auth/login/')
def partner_update(request, id):
    title = sig + 'Alterar Parceiro'
    
    nickname = request.POST.get('nickname')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    document = request.POST.get('document')
    email = request.POST.get('email')
    phone1 = request.POST.get('phone1')
    phone2 = request.POST.get('phone2')

    company = request.POST.get('company')
    type_partners = request.POST.get('type_partners')
    type_person = request.POST.get('type_person')
    gender = request.POST.get('gender')
    status = request.POST.get('status')

    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    company_id_value = user_token_company_id[0][0]

    partners_exists = Partner.objects.filter(id=id, company_id=company_id_value)
    if not partners_exists.exists():
        messages.add_message(request, constants.ERROR, 'Você não tem acesso a este identificador !!!')
        return redirect('/painel/parceiros')
    
    users = User.objects.all()
    partner = Partner.objects.get(id=id)
    partners = Partner.objects.filter(id=id)
    context =   {   'title': title,
                    'users': users,
                    'partner': partner,
                    'partners': partners}

    if (len(nickname.strip()) == 0):
        messages.add_message(request, constants.ERROR, 'Preencha todos os campos !!!')
        return render(request, 'partners/partner_update.html', context)

    if partners.exists():
        try:    
            partner.status = status

            partner.nickname = nickname
            partner.first_name = first_name
            partner.last_name = last_name
            partner.document = document
            partner.email = email
            partner.phone1 = phone1
            partner.phone2 = phone2

            partner.company_id = company
            partner.type_partners = type_partners
            partner.type_person = type_person
            partner.gender = gender
            partner.status = status

            partner.save()

            messages.add_message(request, constants.SUCCESS, 'Alteração Efetuada com Sucesso!')
            return redirect('/painel/parceiros')
        except:
            messages.add_message(request, constants.ERROR, 'Erro Interno do Sistema!!!')
            return redirect('/painel/parceiros')

    return render(request, 'partners/partner_list.html')


@login_required(login_url='/auth/login/')
def partner_delete(request, id):
    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    company_id_value = user_token_company_id[0][0]

    partners_exists = Partner.objects.filter(id=id, company_id=company_id_value)
    if not partners_exists.exists():
        messages.add_message(request, constants.ERROR, 'Você não tem acesso a este identificador !!!')
        return redirect('/painel/parceiros')
    else: 
        partner = Partner.objects.get(id=id)
        partner.delete()
        messages.add_message(request, constants.SUCCESS, 'Parceiro Excluído com Sucesso!')
        return redirect('/painel/parceiros')


# Items
