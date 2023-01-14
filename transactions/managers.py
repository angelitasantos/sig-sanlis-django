from django.db import models


class SaleManager(models.Manager):

    def get_queryset(self):
        return super(SaleManager, self).get_queryset().filter(type_moviment='V')


class ServiceManager(models.Manager):

    def get_queryset(self):
        return super(ServiceManager, self).get_queryset().filter(type_moviment='S')
    

class ShoppingManager(models.Manager):

    def get_queryset(self):
        return super(ShoppingManager, self).get_queryset().filter(type_moviment='C')


class ProductionManager(models.Manager):

    def get_queryset(self):
        return super(ProductionManager, self).get_queryset().filter(type_moviment='P')


class InventaryManager(models.Manager):

    def get_queryset(self):
        return super(InventaryManager, self).get_queryset().filter(type_moviment='I')