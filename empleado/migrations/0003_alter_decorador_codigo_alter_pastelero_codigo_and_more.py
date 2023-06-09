# Generated by Django 4.2.1 on 2023-05-12 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0002_alter_decorador_codigo_alter_pastelero_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decorador',
            name='codigo',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='pastelero',
            name='codigo',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='pastelero',
            name='pasaporte',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
