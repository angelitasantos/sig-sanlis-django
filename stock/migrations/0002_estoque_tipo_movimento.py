# Generated by Django 4.1.3 on 2023-01-14 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estoque',
            name='tipo_movimento',
            field=models.CharField(choices=[('V', 'VENDA'), ('S', 'SERVIÇO'), ('C', 'COMPRA'), ('P', 'PRODUÇÃO'), ('I', 'INVENTÁRIO')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
