# Generated by Django 4.1.3 on 2023-01-11 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataform', '0008_item_created_item_modified_partner_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='email',
            field=models.EmailField(default='', max_length=254, null=True),
        ),
    ]
