# Generated by Django 4.2.1 on 2023-05-12 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empleado', '0004_alter_decorador_options_alter_pastelero_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Decoracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_inicio', models.DateTimeField(auto_now_add=True)),
                ('hora_fin', models.DateTimeField()),
                ('peso_final', models.FloatField()),
                ('decorador_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='empleado.decorador')),
            ],
            options={
                'verbose_name_plural': 'Decoraciones',
            },
        ),
    ]
