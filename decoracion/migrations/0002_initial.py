# Generated by Django 4.2.1 on 2023-05-12 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('decoracion', '0001_initial'),
        ('produccion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='decoracion',
            name='produccion_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='produccion.produccion'),
        ),
    ]
