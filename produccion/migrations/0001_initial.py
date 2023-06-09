# Generated by Django 4.2.1 on 2023-05-12 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('junta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('valor', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Hornos',
            },
        ),
        migrations.CreateModel(
            name='Produccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperatura', models.FloatField()),
                ('hora_inicio', models.DateTimeField(auto_now_add=True)),
                ('hora_fin', models.DateTimeField()),
                ('horno_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='produccion.horno')),
                ('junta_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='junta.junta')),
            ],
            options={
                'verbose_name_plural': 'Producciones',
            },
        ),
    ]
