from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy
from home.models import TimeStampedModel
from plataform.models import Item
from .managers import   (
                            StockSaleManager, 
                            StockServiceManager,
                            StockShoppingManager,
                            StockProductionManager,
                            StockInventaryManager
                        )


MOVIMENTO = (
    ('E', 'entrada'),
    ('S', 'saida'),
)

TIPO_MOVIMENTO = (
    ('V', 'VENDA'),
    ('S', 'SERVIÇO'),
    ('C', 'COMPRA'),
    ('P', 'PRODUÇÃO'),
    ('I', 'INVENTÁRIO'),
)


class Estoque(TimeStampedModel):
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE)
    nf = models.PositiveIntegerField('nota fiscal', null=True, blank=True)
    movimento = models.CharField(max_length=1, choices=MOVIMENTO)
    tipo_movimento = models.CharField(max_length=1, choices=TIPO_MOVIMENTO)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.nf, self.created.strftime('%d-%m-%Y'))
    
    def nf_formated(self):
        return str(self.nf).zfill(3)


class StockSale(Estoque):

    objects = StockSaleManager()

    class Meta:
        proxy = True
        verbose_name = 'registro de venda'
        verbose_name_plural = 'registros de vendas'
    
    def get_absolute_url(self):
        return reverse_lazy('stock:stock_sale_detail', kwargs={'pk': self.pk})


class StockService(Estoque):

    objects = StockServiceManager()

    class Meta:
        proxy = True
        verbose_name = 'registro de serviço'
        verbose_name_plural = 'registros de serviços'

    def get_absolute_url(self):
        return reverse_lazy('stock:stock_service_detail', kwargs={'pk': self.pk})


class StockShopping(Estoque):

    objects = StockShoppingManager()

    class Meta:
        proxy = True
        verbose_name = 'registro de compra'
        verbose_name_plural = 'registros de compras'

    def get_absolute_url(self):
        return reverse_lazy('stock:stock_shopping_detail', kwargs={'pk': self.pk})


class StockProduction(Estoque):

    objects = StockProductionManager()

    class Meta:
        proxy = True
        verbose_name = 'registro de produção'
        verbose_name_plural = 'registros de produção'

    def get_absolute_url(self):
        return reverse_lazy('stock:stock_production_detail', kwargs={'pk': self.pk})


class StockInventary(Estoque):

    objects = StockInventaryManager()

    class Meta:
        proxy = True
        verbose_name = 'registro de inventário'
        verbose_name_plural = 'registros de inventário'

    def get_absolute_url(self):
        return reverse_lazy('stock:stock_inventary_detail', kwargs={'pk': self.pk})


class EstoqueItens(models.Model):
    estoque = models.ForeignKey(
        Estoque,
        on_delete=models.CASCADE,
        related_name='estoques'
    )
    produto = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField()

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.estoque.pk, self.produto)
