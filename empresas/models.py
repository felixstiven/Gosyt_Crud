from django.db import models

class Empresa(models.Model):
    nombre_empresa = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=8, blank=True, null=True)

    def __str__(self) -> str:
        return self.nombre_empresa

    class Meta:
        managed = False
        db_table = 'empresa'