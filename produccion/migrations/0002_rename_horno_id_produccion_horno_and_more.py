# Generated by Django 4.2.1 on 2023-05-12 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produccion',
            old_name='horno_id',
            new_name='horno',
        ),
        migrations.RenameField(
            model_name='produccion',
            old_name='junta_id',
            new_name='junta',
        ),
    ]
