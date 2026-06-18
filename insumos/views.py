from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from .models import SolicitudInsumo
from tareas.models import Tarea
from usuarios.models import Usuario
from empresas.models import Empresa

class InsumoListView(ListView):
    model = SolicitudInsumo
    template_name = 'insumos/list.html'
    context_object_name = 'insumos'

    def get_queryset(self):
        return SolicitudInsumo.objects.filter(tarea_id=self.kwargs['tarea_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empresa'] = get_object_or_404(Empresa, pk=self.kwargs['empresa_id'])
        context['usuario'] = get_object_or_404(Usuario, pk=self.kwargs['usuario_id'])
        context['tarea'] = get_object_or_404(Tarea, pk=self.kwargs['tarea_id'])
        return context

class InsumoDetailView(DetailView):
    model = SolicitudInsumo
    template_name = 'insumos/detail.html'
    context_object_name = 'insumo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empresa'] = get_object_or_404(Empresa, pk=self.kwargs['empresa_id'])
        context['usuario'] = get_object_or_404(Usuario, pk=self.kwargs['usuario_id'])
        context['tarea'] = get_object_or_404(Tarea, pk=self.kwargs['tarea_id'])
        return context

class InsumoCreateView(CreateView):
    model = SolicitudInsumo
    template_name = 'insumos/form.html'
    fields = ['nombre_material', 'cantidad', 'justificacion', 'estado']

    def form_valid(self, form):
        form.instance.tarea_id = self.kwargs['tarea_id']
        form.instance.tecnico_id = self.kwargs['usuario_id']
        return super().form_valid(form)

    def get_success_url(self):
        return f"/empresas/{self.kwargs['empresa_id']}/usuarios/{self.kwargs['usuario_id']}/tareas/{self.kwargs['tarea_id']}/insumos/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empresa'] = get_object_or_404(Empresa, pk=self.kwargs['empresa_id'])
        context['usuario'] = get_object_or_404(Usuario, pk=self.kwargs['usuario_id'])
        context['tarea'] = get_object_or_404(Tarea, pk=self.kwargs['tarea_id'])
        return context

class InsumoUpdateView(UpdateView):
    model = SolicitudInsumo
    template_name = 'insumos/form.html'
    fields = ['estado']
    context_object_name = 'insumo'

    def get_success_url(self):
        return f"/empresas/{self.kwargs['empresa_id']}/usuarios/{self.kwargs['usuario_id']}/tareas/{self.kwargs['tarea_id']}/insumos/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empresa'] = get_object_or_404(Empresa, pk=self.kwargs['empresa_id'])
        context['usuario'] = get_object_or_404(Usuario, pk=self.kwargs['usuario_id'])
        context['tarea'] = get_object_or_404(Tarea, pk=self.kwargs['tarea_id'])
        return context

class InsumoDeleteView(DeleteView):
    model = SolicitudInsumo
    template_name = 'insumos/confirm_delete.html'
    context_object_name = 'insumo'

    def get_success_url(self):
        return f"/empresas/{self.kwargs['empresa_id']}/usuarios/{self.kwargs['usuario_id']}/tareas/{self.kwargs['tarea_id']}/insumos/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empresa'] = get_object_or_404(Empresa, pk=self.kwargs['empresa_id'])
        context['usuario'] = get_object_or_404(Usuario, pk=self.kwargs['usuario_id'])
        context['tarea'] = get_object_or_404(Tarea, pk=self.kwargs['tarea_id'])
        return context