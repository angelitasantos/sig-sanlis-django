# Generated by Django 4.1.3 on 2023-01-17 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plataform', '0011_alter_item_type_item'),
        ('activation', '0006_alter_company_start_data'),
        ('stock', '0004_delete_estoqueentrada_delete_estoquesaida_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='estoque',
            name='company',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='activation.company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estoque',
            name='partner',
            field=models.ForeignKey(default=1299, on_delete=django.db.models.deletion.CASCADE, to='plataform.partner'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estoque',
            name='status',
            field=models.CharField(choices=[('1', 'Não Iniciado'), ('2', 'Em Aberto'), ('3', 'Finalizado')], default='2', max_length=1),
        ),
        migrations.AddField(
            model_name='estoque',
            name='tipo_registro',
            field=models.CharField(choices=[('1', 'Não Autorizado'), ('2', 'Pedido'), ('3', 'Troca'), ('4', 'Devolução'), ('5', 'Garantia'), ('6', 'Consignado')], default='2', max_length=1),
        ),
    ]