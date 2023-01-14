from django.db import models
from home.models import TimeStampedModel

from activation.models import Company
from plataform.models import Partner, Item
from .managers import SaleManager, ServiceManager, ShoppingManager, ProductionManager, InventaryManager



MOVIMENT = (
    ('E', 'ENTRADA'),
    ('S', 'SAIDA'),
)


TYPE_TRANSACTION = (
    ('V', 'VENDA'),
    ('S', 'SERVIÇO'),
    ('C', 'COMPRA'),
    ('P', 'PRODUÇÃO'),
    ('I', 'INVENTÁRIO'),
)


class Transaction(TimeStampedModel):
    choices_type_register = (   ('1', 'Não Autorizado'),
                                ('2', 'Pedido'),
                                ('3', 'Troca'),
                                ('4', 'Devolução'),
                                ('5', 'Garantia'),
                                ('6', 'Consignado'))
    choices_status = (  ('1', 'Não Iniciado'),
                        ('2', 'Em Aberto'),
                        ('3', 'Finalizado'))
    moviment = models.CharField(max_length=1, choices=MOVIMENT, blank=True)
    type_moviment = models.CharField(max_length=1, choices=TYPE_TRANSACTION, blank=True)
    type_register = models.CharField(max_length=1, choices=choices_type_register, default="2")
    status = models.CharField(max_length=1, choices=choices_status, default="2")
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    document = models.PositiveIntegerField('documento', null=True, blank=True)
    identify = models.PositiveIntegerField('identificador', null=True, blank=True)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)

    car = models.CharField('veiculo', max_length=20, null=True, blank=True)
    car_sign = models.CharField('placa', max_length=20, null=True, blank=True)
    car_chassis = models.CharField('chassi', max_length=20, null=True, blank=True)
    car_model = models.CharField('modelo', max_length=20, null=True, blank=True)
    car_fabricator = models.CharField('fabricante', max_length=20, null=True, blank=True)

    sector = models.CharField('setor', max_length=20, null=True, blank=True)
    machine = models.CharField('maquina', max_length=20, null=True, blank=True)
    shift = models.CharField('turno', max_length=20, null=True, blank=True)
    responsible = models.CharField('responsavel', max_length=20, null=True, blank=True)
    place = models.CharField('local', max_length=20, null=True, blank=True)
    shipping_company = models.CharField('transportadora', max_length=20, null=True, blank=True)

    value_amount = models.FloatField('valor total', null=True, blank=True)
    value_liquid = models.FloatField('valor liquido', null=True, blank=True)
    value_discount = models.FloatField('valor desconto', null=True, blank=True)
    value_add = models.FloatField('valor acrescimo', null=True, blank=True)    

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        if self.identify:
            return '{} - {} - {}'.format(self.identify, self.created.strftime('%d-%m-%Y', self.id))
        return '{} --- {}'.format(self.created.strftime('%d-%m-%Y'), self.id)

    def identify_formated(self):
        if self.identify:
            return str(self.identify).zfill(9)
        return '---'


class TransactionSale(Transaction):

    objects = SaleManager()

    class Meta:
        proxy = True
        verbose_name = 'registro venda'
        verbose_name_plural = 'registro venda'


class TransactionService(Transaction):

    objects = ServiceManager()

    class Meta:
        proxy = True
        verbose_name = 'registro serviço'
        verbose_name_plural = 'registro serviço'


class TransactionShopping(Transaction):

    objects = ShoppingManager()

    class Meta:
        proxy = True
        verbose_name = 'registro compra'
        verbose_name_plural = 'registro compra'


class TransactionProduction(Transaction):

    objects = ProductionManager()

    class Meta:
        proxy = True
        verbose_name = 'registro produção'
        verbose_name_plural = 'registro produção'


class TransactionInventary(Transaction):

    objects = InventaryManager()

    class Meta:
        proxy = True
        verbose_name = 'registro inventário'
        verbose_name_plural = 'registro inventário'


class TransactionItems(models.Model):
    transaction = models.ForeignKey(
        Transaction,
        on_delete=models.CASCADE,
        related_name='registros'
    )
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    qtd = models.PositiveIntegerField()
    price_term = models.FloatField('preço', null=True, blank=True)
    price_custom = models.FloatField('custo', null=True, blank=True)
    balance = models.PositiveIntegerField('saldo', null=True, blank=True)
    account = models.CharField('conta contabil', max_length=20, null=True, blank=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return '{} - {} - {}'.format(self.id, self.stock_qtd.id, self.item)
    
