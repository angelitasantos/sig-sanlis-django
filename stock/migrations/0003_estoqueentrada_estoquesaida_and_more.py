# Generated by Django 4.1.3 on 2023-01-15 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_estoque_tipo_movimento'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstoqueEntrada',
            fields=[
            ],
            options={
                'verbose_name': 'estoque entrada',
                'verbose_name_plural': 'estoque entrada',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('stock.estoque',),
        ),
        migrations.CreateModel(
            name='EstoqueSaida',
            fields=[
            ],
            options={
                'verbose_name': 'estoque saída',
                'verbose_name_plural': 'estoque saída',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('stock.estoque',),
        ),
        migrations.AlterField(
            model_name='estoqueitens',
            name='estoque',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estoques', to='stock.estoque'),
        ),
    ]
