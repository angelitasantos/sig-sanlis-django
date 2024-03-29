# Generated by Django 4.1.3 on 2023-01-02 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('activation', '0006_alter_company_start_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
                ('markup', models.FloatField(null=True)),
                ('commission', models.FloatField(null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activation.company')),
            ],
        ),
        migrations.CreateModel(
            name='UnMed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('un_med', models.CharField(max_length=5)),
                ('description', models.CharField(max_length=30)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activation.company')),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('document', models.CharField(max_length=30, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone1', models.CharField(max_length=20, null=True)),
                ('phone2', models.CharField(max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('type_partners', models.CharField(choices=[('1', 'Cliente'), ('2', 'Fornecedor'), ('3', 'Transportadora'), ('4', 'Vendedor'), ('5', 'Funcionário')], default='1', max_length=1)),
                ('type_person', models.CharField(choices=[('F', 'Física'), ('J', 'Jurídica')], default='J', max_length=1)),
                ('gender', models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino')], default='M', max_length=1)),
                ('status', models.CharField(choices=[('A', 'Ativo'), ('I', 'Inativo')], default='A', max_length=1)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activation.company')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250, null=True)),
                ('location', models.CharField(max_length=20)),
                ('reference', models.CharField(max_length=20)),
                ('open_balance', models.FloatField(null=True)),
                ('price_in_cash', models.FloatField(null=True)),
                ('price_term', models.FloatField(null=True)),
                ('price_promotion', models.FloatField(null=True)),
                ('custom', models.FloatField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('stock_control', models.BooleanField()),
                ('status', models.CharField(choices=[('A', 'Ativo'), ('I', 'Inativo')], default='A', max_length=1)),
                ('type_item', models.CharField(choices=[('S', 'Serviço'), ('P', 'Produto')], default='S', max_length=1)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataform.category')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activation.company')),
                ('un_med', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataform.unmed')),
            ],
        ),
    ]
