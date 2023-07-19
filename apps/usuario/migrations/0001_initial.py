# Generated by Django 4.2.2 on 2023-07-19 04:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('apellido', models.CharField(max_length=80)),
                ('telefono', models.IntegerField(max_length=30)),
                ('username', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=250)),
                ('contraseña', models.CharField(max_length=50)),
                ('fecha_registro', models.DateTimeField(default=django.utils.timezone.now)),
                ('avatar', models.ImageField(blank=True, default='articulo/default.png', null=True, upload_to='usuario')),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('-nombre',),
            },
        ),
    ]
