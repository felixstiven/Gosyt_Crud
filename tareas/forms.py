from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    fecha_limite = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(
            attrs={'type': 'datetime-local'},
            format='%Y-%m-%dT%H:%M'
        ),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'prioridad', 'fecha_limite', 'ubicacion', 'estado']