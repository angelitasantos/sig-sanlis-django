from django.db import models
from home.models import TimeStampedModel

from activation.models import Company
from django.utils import timezone


class PartnerGroup(models.Model):
    group = models.CharField(max_length=30)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        ordering = ('group',)

    def __str__(self):
        return self.group


class PartnerSubGroup(models.Model):
    subgroup = models.CharField(max_length=30)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        ordering = ('subgroup',)

    def __str__(self):
        return self.subgroup


class Partner(models.Model):
    choices_type_partners = (   ('1', 'Cliente'),
                                ('2', 'Fornecedor'),
                                ('3', 'Transportadora'),
                                ('4', 'Vendedor'),
                                ('5', 'Funcionário'))
    choices_gender = (  ('F', 'Feminino'),
                        ('M', 'Masculino'))
    choices_type_person = ( ('F', 'Física'),
                            ('J', 'Jurídica'))
    choices_status = (  ('A', 'Ativo'),
                        ('I', 'Inativo'))

    nickname = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    document = models.CharField(max_length=30, null=True)
    email = models.EmailField(null=True)
    phone1 = models.CharField(max_length=20, null=True)
    phone2 = models.CharField(max_length=20, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    address = models.CharField(max_length=100, null=True)
    number = models.CharField(max_length=10, null=True)
    compl = models.CharField(max_length=20, null=True)
    district = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=30, null=True)
    country = models.CharField(max_length=30, null=True)
    zipcode = models.CharField(max_length=20, null=True)

    cnpj = models.CharField(max_length=30, null=True)
    insc_est = models.CharField(max_length=30, null=True)
    insc_mun = models.CharField(max_length=30, null=True)
    rg = models.CharField(max_length=30, null=True)
    cpf = models.CharField(max_length=30, null=True)
    tit_eleitor = models.CharField(max_length=30, null=True)
    zona = models.CharField(max_length=10, null=True)
    secao = models.CharField(max_length=10, null=True)
    ctps = models.CharField(max_length=30, null=True)
    pis = models.CharField(max_length=30, null=True)
    cert_reservista = models.CharField(max_length=30, null=True)
    cnh = models.CharField(max_length=30, null=True)

    data_nasc = models.DateField(default=timezone.now)
    data_admissao = models.DateField(default=timezone.now)
    data_demissao = models.DateField(default=timezone.now)

    banco = models.CharField(max_length=30, null=True)
    agencia = models.CharField(max_length=30, null=True)
    tipo_conta = models.CharField(max_length=30, null=True)
    conta = models.CharField(max_length=30, null=True)
    pix = models.CharField(max_length=30, null=True)

    group = models.ForeignKey(PartnerGroup, on_delete=models.CASCADE, null=True, blank=True, default=None)
    subgroup = models.ForeignKey(PartnerSubGroup, on_delete=models.CASCADE, null=True, blank=True, default=None)
    
    type_partners = models.CharField(max_length=1, choices=choices_type_partners, default="1")
    type_person = models.CharField(max_length=1, choices=choices_type_person, default="J")
    gender = models.CharField(max_length=1, choices=choices_gender, default="M")
    status = models.CharField(max_length=1, choices=choices_status, default="A")

    class Meta:
        ordering = ('nickname',)

    def __str__(self):
        return self.nickname


class Category(models.Model):
    category = models.CharField(max_length=30)
    markup = models.FloatField(null=True)
    commission = models.FloatField(null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        ordering = ('category',)

    def __str__(self):
        return self.category


class UnMed(models.Model):
    un_med = models.CharField(max_length=5)
    description = models.CharField(max_length=30)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        ordering = ('description',)

    def __str__(self):
        return self.un_med


class Item(models.Model):
    choices_status = (  ('A', 'Ativo'),
                        ('I', 'Inativo'))
    choices_type_item = (   ('S', 'Serviço'),
                            ('P', 'Produto'))
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250, null=True)
    location = models.CharField(max_length=20)
    reference = models.CharField(max_length=20)

    open_balance = models.FloatField(null=True)
    price_in_cash = models.FloatField(null=True)
    price_term = models.FloatField(null=True)
    price_promotion = models.FloatField(null=True)
    custom = models.FloatField(null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    stock_control = models.BooleanField()
    status = models.CharField(max_length=1, choices=choices_status, default="A")
    type_item = models.CharField(max_length=1, choices=choices_type_item, default="S")
    un_med = models.ForeignKey(UnMed, on_delete=models.CASCADE, null=True, blank=True, default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, default=None)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title