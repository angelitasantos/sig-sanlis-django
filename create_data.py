import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sig_sanlis.settings")
django.setup()

import string
import timeit
from random import choice, randint, random

from plataform.models import PartnerGroup, PartnerSubGroup, Partner, Category, UnMed, Brand, Item


class Utils:
    ''' Métodos genéricos. '''
    @staticmethod
    def gen_digits(max_length):
        return str(''.join(choice(string.digits) for i in range(max_length)))


class PartnerGroupClass:

    @staticmethod
    def create_partner_group(partner_group):
        PartnerGroup.objects.all().delete()
        aux = []
        for partner in partner_group:
            data = dict(
                group=partner,
                company_id=3,
            )
            obj = PartnerGroup(**data)
            aux.append(obj)
        PartnerGroup.objects.bulk_create(aux)


partner_group = (
    'Atacadista',
    'Varejista',
    'Distribuidora',
    'Consumidor Final',
    'Revendedor',
)


class PartnerSubGroupClass:

    @staticmethod
    def create_partner_subgroup(partner_subgroup):
        PartnerSubGroup.objects.all().delete()
        aux = []
        for partner in partner_subgroup:
            data = dict(
                subgroup=partner,
                company_id=3,
            )
            obj = PartnerSubGroup(**data)
            aux.append(obj)
        PartnerSubGroup.objects.bulk_create(aux)


partner_subgroup = (
    'Mercearia',
    'Supermercado',
    'Açougue',
    'Sacolão',
    'Padaria',
)


class PartnerClass:

    @staticmethod
    def create_partners(produtos):
        Partner.objects.all().delete()
        aux = []
        for partner in partners:
            data = dict(
                nickname=partner,
                first_name="",
                last_name="",
                document="",
                phone1="",
                phone2="",
                email="",
                type_partners=choice((1, 2, 3, 4, 5)),
                type_person=choice(("F", "J")),
                gender=choice(("F", "M")),
                status=choice(("A", "I")),
                company_id=3,
            )
            obj = Partner(**data)
            aux.append(obj)
        Partner.objects.bulk_create(aux)


partners = (
    'Sacolão ABC',
    'Papelaria 123',
    'Mercearia XYZ',
    'Supermercado do Bão',
    'Padaria do Rolê',
    'Restaurante da Vó',
)


class CategoryClass:

    @staticmethod
    def create_categories(categories):
        Category.objects.all().delete()
        aux = []
        for category in categories:
            data = dict(
                category=category,
                markup=random() * randint(1, 10),
                commission=random() * randint(1, 10),
                company_id=3,
            )
            obj = Category(**data)
            aux.append(obj)
        Category.objects.bulk_create(aux)


categories = (
    'Produto para Revenda',
    'Serviço Prestado',
    'Consumo e Utilização',
    'Ativo Imobilizado',
)


class UnMedClass:

    @staticmethod
    def create_un_med(un_meds):
        UnMed.objects.all().delete()
        aux = []
        for un_med in un_meds:
            data = dict(
                un_med=un_med,
                description=un_med,
                company_id=3,
            )
            obj = UnMed(**data)
            aux.append(obj)
        UnMed.objects.bulk_create(aux)


un_meds = (
    'un',
    'pc',
    'kg',
    'cx',
    'hr',
)


class BrandClass:

    @staticmethod
    def create_brands(brands):
        Brand.objects.all().delete()
        aux = []
        for brand in brands:
            data = dict(
                brand=brand,
                markup=random() * randint(1, 10),
                commission=random() * randint(1, 10),
                company_id=3,
            )
            obj = Brand(**data)
            aux.append(obj)
        Brand.objects.bulk_create(aux)


brands = (
    'Fiat',
    'Volkswagen',
    'Chevrolet',
    'Ford',
    'Outro',
)


class ItemClass:

    @staticmethod
    def create_products(items):
        Item.objects.all().delete()
        aux = []
        for item in items:
            data = dict(
                title=item,
                description=item,
                status=choice(("A", "I")),
                location="GERAL",
                stock_control=True,
                type_item="1",
                reference=Utils.gen_digits(8),
                price_in_cash=random() * randint(10.0, 50.0),
                price_term=random() * randint(10.0, 50.0),
                price_promotion=random() * randint(10.0, 50.0),
                price_custom=random() * randint(10.0, 50.0),
                stock_qtd=randint(10, 200),
                company_id=3,
            )
            obj = Item(**data)
            aux.append(obj)
        Item.objects.bulk_create(aux)


items = (
    'Apontador',
    'Caderno 100 folhas',
    'Caneta azul',
    'Caneta preta',
    'Durex',
    'Giz de cera 12 cores',
    'Lapiseira 0.5 mm',
    'Lapiseira 0.7 mm',
    'Lápis de cor 24 cores',
    'Lápis',
    'Papel A4 com 100 folhas',
    'Pasta elástica',
    'Tesoura',
)



tic = timeit.default_timer()

PartnerGroupClass.create_partner_group(partner_group)
PartnerSubGroupClass.create_partner_subgroup(partner_subgroup)
PartnerClass.create_partners(partners)
CategoryClass.create_categories(categories)
UnMedClass.create_un_med(un_meds)
BrandClass.create_brands(brands)
ItemClass.create_products(items)



toc = timeit.default_timer()

print('Tempo:', toc - tic)