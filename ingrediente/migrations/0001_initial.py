# Generated by Django 4.2.1 on 2023-05-12 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('cantidad5', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Ingredientes',
            },
        ),
    ]