from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.shortcuts import get_object_or_404
from .models import Evidencia
from tareas.models import Tarea
from usuarios.models import Usuario
from empresas.models import Empresa

class EvidenciaListView(ListView):
    model = Evidencia
    template_name = 'evidencias/list.html'
    context_object_name = 'evidencias'

    def get_queryset(self):
        return Evidencia.objects.filter(tarea_id=self.kwargs['tarea_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empresa'] = get_object_or_404(Empresa, pk=self.kwargs['empresa_id'])
        context['usuario'] = get_object_or_404(Usuario, pk=self.kwargs['usuario_id'])
        context['tarea'] = get_object_or_404(Tarea, pk=self.kwargs['tarea_id'])
        return context

class EvidenciaDetailView(DetailView):
    model = Evidencia
    template_name = 'evidencias/detail.html'
    context_object_name = 'evidencia'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empresa'] = get_object_or_404(Empresa, pk=self.kwargs['empresa_id'])
        context['usuario'] = get_object_or_404(Usuario, pk=self.kwargs['usuario_id'])
        context['tarea'] = get_object_or_404(Tarea, pk=self.kwargs['tarea_id'])
        return context

class EvidenciaCreateView(CreateView):
    model = Evidencia
    template_name = 'evidencias/form.html'
    fields = ['ruta_archivo', 'tipo_archivo', 'comentario']

    def form_valid(self, form):
        form.instance.tarea_id = self.kwargs['tarea_id']
        form.instance.tecnico_id = self.kwargs['usuario_id']
        return super().form_valid(form)

    def get_success_url(self):
        return f"/empresas/{self.kwargs['empresa_id']}/usuarios/{self.kwargs['usuario_id']}/tareas/{self.kwargs['tarea_id']}/evidencias/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empresa'] = get_object_or_404(Empresa, pk=self.kwargs['empresa_id'])
        context['usuario'] = get_object_or_404(Usuario, pk=self.kwargs['usuario_id'])
        context['tarea'] = get_object_or_404(Tarea, pk=self.kwargs['tarea_id'])
        return context

class EvidenciaDeleteView(DeleteView):
    model = Evidencia
    template_name = 'evidencias/confirm_delete.html'
    context_object_name = 'evidencia'

    def get_success_url(self):
        return f"/empresas/{self.kwargs['empresa_id']}/usuarios/{self.kwargs['usuario_id']}/tareas/{self.kwargs['tarea_id']}/evidencias/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empresa'] = get_object_or_404(Empresa, pk=self.kwargs['empresa_id'])
        context['usuario'] = get_object_or_404(Usuario, pk=self.kwargs['usuario_id'])
        context['tarea'] = get_object_or_404(Tarea, pk=self.kwargs['tarea_id'])
        return context