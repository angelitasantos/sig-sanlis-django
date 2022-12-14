# Generated by Django 4.1.3 on 2023-01-10 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataform', '0007_rename_dun_item_code_dun_rename_ean_item_code_ean_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default='2023-01-10 08:00:00', verbose_name='criado em'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modificado em'),
        ),
        migrations.AddField(
            model_name='partner',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default='2023-01-10 08:00:00', verbose_name='criado em'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='partner',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modificado em'),
        ),
    ]
