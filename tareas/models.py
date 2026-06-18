from django.db import models
from empresas.models import Empresa
from usuarios.models import Usuario

class Tarea(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    prioridad = models.CharField(max_length=5, blank=True, null=True)
    fecha_limite = models.DateTimeField(blank=True, null=True)
    ubicacion = models.CharField(max_length=150, blank=True, null=True)
    estado = models.CharField(max_length=10, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    coordinador = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    def __str__(self) -> str:
        return self.titulo

    def get_tecnicos_asignados(self):
        return Usuario.objects.filter(
            asignaciontarea__tarea=self
        )

    class Meta:
        managed = False
        db_table = 'tarea'


class AsignacionTarea(models.Model):
    pk = models.CompositePrimaryKey('tarea_id', 'tecnico_id')
    tarea = models.ForeignKey(
        Tarea,
        on_delete=models.CASCADE
    )
    tecnico = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE
    )
    es_lider = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asignacion_tarea'