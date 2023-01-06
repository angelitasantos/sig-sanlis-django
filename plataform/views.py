from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from activation.models import TokenUser, Company
from .models import Partner, Category, UnMed, Item

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
        company_id_value = user_token_company_id[0][0]
        partners = Partner.objects.filter(company_id=company_id_value)
        
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
@login_required(login_url='/auth/login/')
def items(request):
    title = sig + 'Listar Items'

    users = User.objects.all()
    user_login = User.objects.filter(username=request.user)
    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    
    if user_token_company.exists():
        title_filtrar = request.GET.get('title')
        company_id_value = user_token_company_id[0][0]
        items = Item.objects.filter(company_id=company_id_value)

        categories_filtrar = request.GET.get('categories')
        if categories_filtrar:
            items = items.filter(category = categories_filtrar)

        categories = Category.objects.filter(company_id=company_id_value)
        un_meds = UnMed.objects.filter(company_id=company_id_value)
        
        if title_filtrar:
            items = items.filter(title__icontains = title_filtrar)

        context =   {   'title': title,
                        'users': users,
                        'items': items,
                        'categories': categories,
                        'un_meds': un_meds,
                        'user_login': user_login[0]}
        render(request, 'items/item_list.html', context)

    elif user_token_company_id.count() == 0:
        messages.add_message(request, constants.ERROR, 'Não encontramos uma empresa para o seu usuário !!!')
        context =   {   'title': title,
                        'users': users,
                        'user_login': user_login[0]}
        return redirect('/painel/')

    return render(request, 'items/item_list.html', context)


@login_required(login_url='/auth/login/')
def item_create(request):
    title = sig + 'Criar Item'
    user_login = User.objects.filter(username=request.user)
    users = User.objects.all()

    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    company_id_value = user_token_company_id[0][0]

    categories = Category.objects.filter(company_id=company_id_value)
    un_meds = UnMed.objects.filter(company_id=company_id_value)
    
    context =   {   'title': title,
                    'user_login': user_login[0],
                    'company_id_value': company_id_value,
                    'categories': categories,
                    'un_meds': un_meds,
                    'users': users}
    if request.method == "GET":
        return render(request, 'items/item_create.html', context)
    elif request.method == "POST":
        title = request.POST.get('title').upper()
        description = request.POST.get('description')
        location = request.POST.get('location')
        reference = request.POST.get('reference')

        open_balance1 = request.POST.get('open_balance')
        open_balance = 0 if open_balance1 == "" else request.POST.get('open_balance').replace(',', '.')

        custom1 = request.POST.get('custom')
        custom = 0 if custom1 == "" else request.POST.get('custom').replace(',', '.')

        price_in_cash1 = request.POST.get('price_in_cash')
        price_in_cash = 0 if price_in_cash1 == "" else request.POST.get('price_in_cash').replace(',', '.')
        
        price_term1 = request.POST.get('price_term')
        price_term = 0 if price_term1 == "" else request.POST.get('price_term').replace(',', '.')

        price_promotion1 = request.POST.get('price_promotion')
        price_promotion = 0 if price_promotion1 == "" else request.POST.get('price_promotion').replace(',', '.')

        company_id = request.POST.get('company')
        stock_control = request.POST.get('stock_control')
        type_item = request.POST.get('type_item')
        un_med_id = request.POST.get('un_med')
        category_id = request.POST.get('category')
        status = "A"

        if (len(title.strip()) == 0):
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos!!!')
            return render(request, 'items/item_create.html', context)

        items = Item.objects.filter(title=title)

        if items.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um item cadastrado com este nome!!!')

        item = Item(    title=title,
                        description=description,
                        location=location,
                        reference=reference,

                        open_balance=open_balance,
                        custom=custom,
                        price_in_cash=price_in_cash,
                        price_term=price_term,
                        price_promotion=price_promotion,

                        company_id=company_id,
                        stock_control=stock_control,
                        type_item=type_item,
                        un_med_id=un_med_id,
                        category_id=category_id,
                        status=status
                        )
        item.save()

        messages.add_message(request, constants.SUCCESS, 'Item Cadastrado com Sucesso!!!')
        return render(request, 'items/item_create.html', context)


@login_required(login_url='/auth/login/')
def item_view(request, id):
    title = sig + 'Visualizar Item'
    user_login = User.objects.filter(username=request.user)

    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    company_id_value = user_token_company_id[0][0]

    items_exists = Item.objects.filter(id=id, company_id=company_id_value)
    if not items_exists.exists():
        messages.add_message(request, constants.ERROR, 'Você não tem acesso a este identificador !!!')
        return redirect('/painel/itens')

    users = User.objects.all()
    item = get_object_or_404(Item, id=id)
    items = Item.objects.filter(company_id=company_id_value)

    categories = Category.objects.filter(company_id=company_id_value)
    un_meds = UnMed.objects.filter(company_id=company_id_value)

    return render(request, 'items/item_update.html', { 'title': title,
                                                        'users': users,
                                                        'user_login': user_login[0],
                                                        'company_id_value': company_id_value,
                                                        'categories': categories,
                                                        'un_meds': un_meds,
                                                        'item': item,
                                                        'items': items})


@login_required(login_url='/auth/login/')
def item_update(request, id):
    title = sig + 'Alterar Item'
    
    title = request.POST.get('title')
    description = request.POST.get('description')
    location = request.POST.get('location')
    reference = request.POST.get('reference')

    open_balance1 = request.POST.get('open_balance')
    open_balance = 0 if open_balance1 == "" else request.POST.get('open_balance').replace(',', '.')

    custom1 = request.POST.get('custom')
    custom = 0 if custom1 == "" else request.POST.get('custom').replace(',', '.')

    price_in_cash1 = request.POST.get('price_in_cash')
    price_in_cash = 0 if price_in_cash1 == "" else request.POST.get('price_in_cash').replace(',', '.')

    price_term1 = request.POST.get('price_term')
    price_term = 0 if price_term1 == "" else request.POST.get('price_term').replace(',', '.')

    price_promotion1 = request.POST.get('price_promotion')
    price_promotion = 0 if price_promotion1 == "" else request.POST.get('price_promotion').replace(',', '.')

    company_id = request.POST.get('company')
    stock_control = request.POST.get('stock_control')
    type_item = request.POST.get('type_item')
    un_med_id = request.POST.get('un_med')
    category_id = request.POST.get('category')
    status = request.POST.get('status')

    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    company_id_value = user_token_company_id[0][0]

    items_exists = Item.objects.filter(id=id, company_id=company_id_value)
    if not items_exists.exists():
        messages.add_message(request, constants.ERROR, 'Você não tem acesso a este identificador !!!')
        return redirect('/painel/itens')

    categories = Category.objects.filter(company_id=company_id_value)
    un_meds = UnMed.objects.filter(company_id=company_id_value)
    
    users = User.objects.all()
    item = Item.objects.get(id=id)
    items = Item.objects.filter(id=id)
    context =   {   'title': title,
                    'users': users,
                    'categories': categories,
                    'un_meds': un_meds,
                    'item': item,
                    'items': items}

    if (len(title.strip()) == 0):
        messages.add_message(request, constants.ERROR, 'Preencha todos os campos !!!')
        return render(request, 'items/item_update.html', context)

    if items.exists():
            item.title = title
            item.description = description
            item.location = location
            item.reference = reference

            item.open_balance = open_balance
            item.custom = custom
            item.price_in_cash = price_in_cash
            item.price_term = price_term
            item.price_promotion = price_promotion

            item.company_id = company_id
            item.stock_control = stock_control
            item.type_item = type_item
            item.un_med_id = un_med_id
            item.category_id = category_id
            item.status = status

            item.save()

            messages.add_message(request, constants.SUCCESS, 'Alteração Efetuada com Sucesso!')
            return redirect('/painel/itens')
        

    return render(request, 'itens/item_list.html')


@login_required(login_url='/auth/login/')
def item_delete(request, id):
    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    company_id_value = user_token_company_id[0][0]

    items_exists = Item.objects.filter(id=id, company_id=company_id_value)
    if not items_exists.exists():
        messages.add_message(request, constants.ERROR, 'Você não tem acesso a este identificador !!!')
        return redirect('/painel/itens')
    else: 
        item = Item.objects.get(id=id)
        item.delete()
        messages.add_message(request, constants.SUCCESS, 'Item Excluído com Sucesso!')
        return redirect('/painel/itens')


# UnMed / Category
@login_required(login_url='/auth/login/')
def un_med_create(request):
    title = sig + 'Criar Item'
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
        return render(request, 'items/item_create.html', context)
    elif request.method == "POST":
        return render(request, 'items/item_create.html', context)


@login_required(login_url='/auth/login/')
def category_create(request):
    title = sig + 'Criar Item'
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
        return render(request, 'items/item_create.html', context)
    elif request.method == "POST":
        return render(request, 'items/item_create.html', context)
