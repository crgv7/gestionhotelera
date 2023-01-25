# Generated by Django 4.1.5 on 2023-01-13 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('capacidad', models.IntegerField(verbose_name='Capacidad del Hotel')),
                ('precio', models.IntegerField(verbose_name='Precio')),
                ('estrellas', models.IntegerField(verbose_name='Estrellas')),
                ('estado', models.BooleanField(default=True, verbose_name='Activo/No Activo')),
                ('imagen', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Hotel',
                'verbose_name_plural': 'Hoteles',
            },
        ),
    ]