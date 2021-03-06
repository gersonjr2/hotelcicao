# Generated by Django 3.1.7 on 2021-03-04 21:00

import apps.users.validate
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cpf',
            field=models.CharField(blank=True, max_length=11, validators=[apps.users.validate.validate_CPF], verbose_name='CPF'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=11, validators=[apps.users.validate.validate_Telefone], verbose_name='Telefone'),
        ),
    ]
