# Generated by Django 4.2.1 on 2023-05-12 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0003_alter_decorador_codigo_alter_pastelero_codigo_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='decorador',
            options={'verbose_name_plural': 'Decoradores'},
        ),
        migrations.AlterModelOptions(
            name='pastelero',
            options={'verbose_name_plural': 'Pasteleros'},
        ),
    ]
