# Generated by Django 4.1.3 on 2023-01-12 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataform', '0010_alter_partner_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='type_item',
            field=models.CharField(choices=[('1', 'Produto para Revenda'), ('2', 'Produção Própria'), ('3', 'Serviço Prestado'), ('4', 'Matéria-Prima'), ('5', 'Consumo e Utilização'), ('6', 'Ativo Patrimonial')], default='S', max_length=1),
        ),
    ]
