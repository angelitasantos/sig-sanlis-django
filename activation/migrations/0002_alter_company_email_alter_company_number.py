# Generated by Django 4.1.3 on 2022-12-03 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='company',
            name='number',
            field=models.IntegerField(blank=True),
        ),
    ]
