# Generated by Django 4.2.1 on 2023-05-12 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Decorador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('salario', models.FloatField(max_length=10)),
                ('codigo', models.IntegerField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pastelero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('salario', models.FloatField(max_length=10)),
                ('codigo', models.IntegerField(max_length=20)),
                ('pasaporte', models.CharField(max_length=20)),
                ('pais', models.CharField(max_length=20)),
                ('exp', models.CharField(max_length=10)),
            ],
        ),
    ]