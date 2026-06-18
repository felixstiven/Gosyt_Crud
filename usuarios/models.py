from django.db import models
from empresas.models import Empresa

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.CharField(unique=True, max_length=100)
    contraseña = models.CharField(max_length=255)
    rol = models.CharField(max_length=13)
    area = models.CharField(max_length=50, blank=True, null=True)
    cargo = models.CharField(max_length=50, blank=True, null=True)
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,
        blank=True, null=True
    )

    def __str__(self) -> str:
        return self.nombre

    def es_admin_o_coordinador(self) -> bool:
        return self.rol in ['admin_empresa', 'coordinador']

    def es_tecnico(self) -> bool:
        return self.rol == 'tecnico'

    def es_lider_en_tarea(self, tarea_id: int) -> bool:
        return self.asignaciontarea_set.filter(
            tarea_id=tarea_id,
            es_lider=True
        ).exists()

    class Meta:
        managed = False
        db_table = 'usuario'