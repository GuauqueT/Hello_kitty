# Generated by Django 4.2.1 on 2023-05-12 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ingrediente', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingrediente',
            old_name='cantidad5',
            new_name='unidad_medida',
        ),
    ]
