from django.db import models
from activation.models import Company


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
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type_partners = models.CharField(max_length=1, choices=choices_type_partners, default="1")
    type_person = models.CharField(max_length=1, choices=choices_type_person, default="J")
    gender = models.CharField(max_length=1, choices=choices_gender, default="M")
    status = models.CharField(max_length=1, choices=choices_status, default="A")

    def __str__(self):
        return self.nickname