# Generated by Django 2.2.13 on 2020-07-04 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('turnos', '0002_delete_paciente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('obra_social', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=80)),
                ('edad', models.IntegerField()),
                ('dni', models.BigIntegerField()),
                ('telefono', models.CharField(max_length=80)),
                ('direccion', models.CharField(max_length=150)),
                ('fecha_create', models.DateTimeField(auto_now_add=True)),
                ('fecha_update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
