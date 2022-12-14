# Generated by Django 4.1.3 on 2022-12-04 20:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activation', '0002_alter_company_email_alter_company_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='TokenUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=64)),
                ('active', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='activation.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]