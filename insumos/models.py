from django.db import models
from tareas.models import Tarea
from usuarios.models import Usuario

class SolicitudInsumo(models.Model):
    tarea = models.ForeignKey(
        Tarea,
        on_delete=models.CASCADE
    )
    tecnico = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    nombre_material = models.CharField(max_length=100)
    cantidad = models.IntegerField(blank=True, null=True)
    justificacion = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=9, blank=True, null=True)
    fecha_solicitud = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return self.nombre_material

    class Meta:
        managed = False
        db_table = 'solicitud_insumo'