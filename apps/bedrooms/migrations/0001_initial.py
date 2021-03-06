# Generated by Django 3.1.7 on 2021-03-16 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bedrooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('de', 'Deluxe'), ('hi', 'Higher'), ('st', 'Standard')], max_length=2)),
                ('size', models.CharField(choices=[('m1', '30 M²'), ('m2', '60 M²'), ('m3', '90 M²')], max_length=2)),
                ('value', models.CharField(choices=[('v1', 'R$ 100'), ('v2', 'R$ 200'), ('v3', 'R$ 500')], max_length=2)),
                ('capacity', models.CharField(choices=[('c1', '1 Pessoa'), ('c2', '2 Pessoas'), ('c3', '5 Pessoas')], max_length=2)),
                ('service', models.CharField(choices=[('s1', 'Wi-Fi'), ('s2', 'Wi-Fi, Café'), ('s3', 'Wi-Fi, Café, Frigobar')], max_length=2)),
            ],
        ),
    ]
