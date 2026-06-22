from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, unique=True, verbose_name='Código de Unidad')),
                ('chofer', models.CharField(max_length=100, verbose_name='Nombre del Chofer')),
                ('capacidad', models.IntegerField(verbose_name='Capacidad de Pasajeros')),
                ('estado', models.CharField(choices=[('activo', 'En Servicio'), ('mantenimiento', 'En Taller'), ('inactivo', 'Fuera de Servicio')], default='activo', max_length=20, verbose_name='Estado de la Unidad')),
            ],
            options={
                'verbose_name': 'Unidad',
                'verbose_name_plural': 'Unidades',
            },
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de la Ruta')),
                ('origen', models.CharField(max_length=100, verbose_name='Punto de Origen')),
                ('destino', models.CharField(max_length=100, verbose_name='Punto de Destino')),
                ('hora_salida', models.TimeField(verbose_name='Hora de Salida')),
                ('precio_pasaje', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Precio del Pasaje')),
                ('unidad_asignada', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rutas.Unidad', verbose_name='Unidad Asignada')),
            ],
            options={
                'verbose_name': 'Ruta',
                'verbose_name_plural': 'Rutas',
            },
        ),
    ]