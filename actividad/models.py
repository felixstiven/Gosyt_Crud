from django.db import models
from tareas.models import Tarea
from usuarios.models import Usuario

class RegistroActividad(models.Model):
    tarea = models.ForeignKey(
        Tarea,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    accion = models.CharField(max_length=100, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.accion} - {self.fecha}"

    class Meta:
        managed = False
        db_table = 'registro_actividad'