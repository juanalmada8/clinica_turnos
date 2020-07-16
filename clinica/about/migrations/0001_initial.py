# Generated by Django 2.2.13 on 2020-07-16 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('subtitulo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=255)),
                ('ruta_imagen', models.FileField(blank=True, default='defecto/defecto.jpg', null=True, upload_to='fotos/%Y/%m/%d')),
                ('fecha_create', models.DateTimeField(auto_now_add=True)),
                ('fecha_update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
