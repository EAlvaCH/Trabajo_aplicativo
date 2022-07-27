# Generated by Django 4.0.6 on 2022-07-27 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.TextField(max_length=10)),
                ('dni', models.TextField(max_length=8)),
                ('nombre', models.TextField()),
                ('apepat', models.TextField()),
                ('apemat', models.TextField()),
                ('direccion', models.TextField()),
                ('telefono', models.TextField()),
                ('estado', models.CharField(max_length=1)),
            ],
        ),
    ]
