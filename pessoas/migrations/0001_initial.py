# Generated by Django 5.2.4 on 2025-07-23 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('cpf_cnpj', models.CharField(max_length=11)),
                ('data_nascimento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
