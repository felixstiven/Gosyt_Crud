from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404
from .models import RegistroActividad
from tareas.models import Tarea
from usuarios.models import Usuario
from empresas.models import Empresa

class ActividadListView(ListView):
    model = RegistroActividad
    template_name = 'actividad/list.html'
    context_object_name = 'registros'

    def get_queryset(self):
        return RegistroActividad.objects.filter(tarea_id=self.kwargs['tarea_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empresa'] = get_object_or_404(Empresa, pk=self.kwargs['empresa_id'])
        context['usuario'] = get_object_or_404(Usuario, pk=self.kwargs['usuario_id'])
        context['tarea'] = get_object_or_404(Tarea, pk=self.kwargs['tarea_id'])
        return context

class ActividadDetailView(DetailView):
    model = RegistroActividad
    template_name = 'actividad/detail.html'
    context_object_name = 'registro'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empresa'] = get_object_or_404(Empresa, pk=self.kwargs['empresa_id'])
        context['usuario'] = get_object_or_404(Usuario, pk=self.kwargs['usuario_id'])
        context['tarea'] = get_object_or_404(Tarea, pk=self.kwargs['tarea_id'])
        return context

class ActividadCreateView(CreateView):
    model = RegistroActividad
    template_name = 'actividad/form.html'
    fields = ['accion']

    def form_valid(self, form):
        from django.utils import timezone
        form.instance.tarea_id = self.kwargs['tarea_id']
        form.instance.usuario_id = self.kwargs['usuario_id']
        form.instance.fecha = timezone.now()
        return super().form_valid(form)

    def get_success_url(self):
        return f"/empresas/{self.kwargs['empresa_id']}/usuarios/{self.kwargs['usuario_id']}/tareas/{self.kwargs['tarea_id']}/actividad/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empresa'] = get_object_or_404(Empresa, pk=self.kwargs['empresa_id'])
        context['usuario'] = get_object_or_404(Usuario, pk=self.kwargs['usuario_id'])
        context['tarea'] = get_object_or_404(Tarea, pk=self.kwargs['tarea_id'])
        return context