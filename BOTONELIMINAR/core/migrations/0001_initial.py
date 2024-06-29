# Generated by Django 5.0.4 on 2024-06-29 17:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=3)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=3)),
                ('nombre', models.CharField(max_length=100)),
                ('planta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.planta')),
            ],
        ),
        migrations.CreateModel(
            name='Produccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Litros_producido', models.IntegerField()),
                ('fecha_produccion', models.DateField()),
                ('turno', models.CharField(choices=[('AM', 'Mañana'), ('PM', 'Tarde'), ('MM', 'Noche')], max_length=100)),
                ('operador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
            ],
        ),
    ]
