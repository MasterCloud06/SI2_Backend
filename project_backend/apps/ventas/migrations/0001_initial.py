# Generated by Django 5.2 on 2025-04-19 21:27

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('total', models.DecimalField(decimal_places=2, help_text='Importe total de la venta', max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('status', models.CharField(choices=[('pendiente', 'Pendiente'), ('completada', 'Completada'), ('cancelada', 'Cancelada')], db_index=True, default='pendiente', max_length=20)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ventas', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'ventas',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='VentaDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cantidad', models.PositiveIntegerField(help_text='Cantidad de unidades vendidas', validators=[django.core.validators.MinValueValidator(1)])),
                ('precio', models.DecimalField(decimal_places=2, help_text='Precio unitario al momento de la venta', max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ventas_detalle', to='productos.product')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='ventas.venta')),
            ],
            options={
                'db_table': 'venta_detalle',
            },
        ),
        migrations.AddIndex(
            model_name='venta',
            index=models.Index(fields=['status', 'created_at'], name='ventas_status_ba9782_idx'),
        ),
    ]
