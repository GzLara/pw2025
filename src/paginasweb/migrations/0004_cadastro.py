# Generated by Django 3.2.25 on 2025-05-28 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginasweb', '0003_tiposensor_numero_serial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='Nome')),
                ('email', models.CharField(max_length=255, verbose_name='E-mail')),
                ('senha', models.CharField(max_length=255, verbose_name='Senha')),
            ],
        ),
    ]
