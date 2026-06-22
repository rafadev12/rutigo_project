from django.db import models

class Unidad(models.Model):
    ESTADOS = [
        ('activo', 'En Servicio'),
        ('mantenimiento', 'En Taller'),
        ('inactivo', 'Fuera de Servicio'),
    ]

    codigo = models.CharField(max_length=10, unique=True, verbose_name="Código de Unidad")
    chofer = models.CharField(max_length=100, verbose_name="Nombre del Chofer")
    capacidad = models.IntegerField(verbose_name="Capacidad de Pasajeros")
    estado = models.CharField(max_length=20, choices=ESTADOS, default='activo', verbose_name="Estado de la Unidad")

    class Meta:
        verbose_name = "Unidad"
        verbose_name_plural = "Unidades"

    def __str__(self):
        return f"{self.codigo} - {self.chofer} ({self.get_estado_display()})"


class Ruta(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la Ruta")
    origen = models.CharField(max_length=100, verbose_name="Punto de Origen")
    destino = models.CharField(max_length=100, verbose_name="Punto de Destino")
    hora_salida = models.TimeField(verbose_name="Hora de Salida")
    precio_pasaje = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Precio del Pasaje")
    unidad_asignada = models.ForeignKey(Unidad, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Unidad Asignada")

    class Meta:
        verbose_name = "Ruta"
        verbose_name_plural = "Rutas"

    def __str__(self):
        return f"{self.nombre}: {self.origen} -> {self.destino}"