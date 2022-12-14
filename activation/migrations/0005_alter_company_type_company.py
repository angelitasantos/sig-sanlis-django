# Generated by Django 4.1.3 on 2022-12-08 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activation', '0004_company_status_company_type_company_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='type_company',
            field=models.CharField(choices=[('MEI', 'MicroEmpreendedor Individual'), ('ME', 'Microempresa'), ('EPP', 'Empresa de Pequeno Porte')], default='MEI', max_length=3),
        ),
    ]