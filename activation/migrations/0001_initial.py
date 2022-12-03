# Generated by Django 4.1.3 on 2022-12-03 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_company', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('full_name', models.CharField(max_length=250)),
                ('start_data', models.DateTimeField()),
                ('cnpj', models.CharField(blank=True, max_length=20)),
                ('insc_est', models.CharField(blank=True, max_length=20)),
                ('insc_mun', models.CharField(blank=True, max_length=20)),
                ('street', models.CharField(blank=True, max_length=100)),
                ('number', models.IntegerField()),
                ('complement', models.CharField(blank=True, max_length=20)),
                ('district', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('state', models.CharField(blank=True, max_length=2)),
                ('zipcode', models.CharField(blank=True, max_length=15)),
                ('google_maps_link', models.TextField(blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=25)),
                ('whatsapp_number', models.CharField(blank=True, max_length=25)),
                ('whatsapp_link', models.CharField(blank=True, max_length=250)),
                ('site_link', models.CharField(blank=True, max_length=250)),
                ('instagram_link', models.CharField(blank=True, max_length=250)),
                ('linkedin_link', models.CharField(blank=True, max_length=250)),
                ('facebook_link', models.CharField(blank=True, max_length=250)),
                ('user_company', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]