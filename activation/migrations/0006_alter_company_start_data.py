# Generated by Django 4.1.3 on 2022-12-08 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activation', '0005_alter_company_type_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='start_data',
            field=models.DateField(),
        ),
    ]
