from django.db import models
from tareas.models import Tarea
from usuarios.models import Usuario

class Evidencia(models.Model):
    tarea = models.ForeignKey(
        Tarea,
        on_delete=models.CASCADE
    )
    tecnico = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    ruta_archivo = models.CharField(max_length=255, blank=True, null=True)
    tipo_archivo = models.CharField(max_length=50, blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)
    fecha_subida = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return f"Evidencia {self.id} - Tarea {self.tarea_id}"

    class Meta:
        managed = False
        db_table = 'evidencia'