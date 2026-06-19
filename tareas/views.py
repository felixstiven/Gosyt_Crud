from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from .models import Tarea, AsignacionTarea
from usuarios.models import Usuario
from empresas.models import Empresa

from .forms import TareaForm

class TareaListView(ListView):
    model = Tarea
    template_name = 'tareas/list.html'
    context_object_name = 'tareas'

    def get_queryset(self):
        usuario = get_object_or_404(Usuario, pk=self.kwargs['usuario_id'])
        if usuario.es_admin_o_coordinador():
            return Tarea.objects.filter(empresa_id=self.kwargs['empresa_id'])
        else:
            return Tarea.objects.filter(
                asignaciontarea__tecnico_id=self.kwargs['usuario_id']
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empresa'] = get_object_or_404(Empresa, pk=self.kwargs['empresa_id'])
        context['usuario'] = get_object_or_404(Usuario, pk=self.kwargs['usuario_id'])
        return context

class TareaDetailView(DetailView):
    model = Tarea
    template_name = 'tareas/detail.html'
    context_object_name = 'tarea'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empresa'] = get_object_or_404(Empresa, pk=self.kwargs['empresa_id'])
        context['usuario'] = get_object_or_404(Usuario, pk=self.kwargs['usuario_id'])
        context['es_lider'] = self.object.asignaciontarea_set.filter(
            tecnico_id=self.kwargs['usuario_id'],
            es_lider=True
        ).exists()
        return context

class TareaCreateView(CreateView):
    model = Tarea
    template_name = 'tareas/form.html'
    form_class = TareaForm

    def form_valid(self, form):
        usuario = get_object_or_404(Usuario, pk=self.kwargs['usuario_id'])
        form.instance.empresa_id = self.kwargs['empresa_id']
        form.instance.coordinador = usuario
        return super().form_valid(form) 

    def get_success_url(self):
        return f"/empresas/{self.kwargs['empresa_id']}/usuarios/{self.kwargs['usuario_id']}/tareas/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empresa'] = get_object_or_404(Empresa, pk=self.kwargs['empresa_id'])
        context['usuario'] = get_object_or_404(Usuario, pk=self.kwargs['usuario_id'])
        return context

class TareaUpdateView(UpdateView):
    model = Tarea
    template_name = 'tareas/form.html'
    form_class = TareaForm
    context_object_name = 'tarea'

    def get_success_url(self):
        return f"/empresas/{self.kwargs['empresa_id']}/usuarios/{self.kwargs['usuario_id']}/tareas/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empresa'] = get_object_or_404(Empresa, pk=self.kwargs['empresa_id'])
        context['usuario'] = get_object_or_404(Usuario, pk=self.kwargs['usuario_id'])
        return context

class TareaDeleteView(DeleteView):
    model = Tarea
    template_name = 'tareas/confirm_delete.html'
    context_object_name = 'tarea'

    def get_success_url(self):
        return f"/empresas/{self.kwargs['empresa_id']}/usuarios/{self.kwargs['usuario_id']}/tareas/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empresa'] = get_object_or_404(Empresa, pk=self.kwargs['empresa_id'])
        context['usuario'] = get_object_or_404(Usuario, pk=self.kwargs['usuario_id'])
        return context

def asignaciones_view(request, empresa_id: int, usuario_id: int, tarea_id: int):
    empresa = get_object_or_404(Empresa, pk=empresa_id)
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    tarea = get_object_or_404(Tarea, pk=tarea_id)

    tecnicos = Usuario.objects.filter(empresa_id=empresa_id, rol='tecnico')
    asignaciones_actuales = AsignacionTarea.objects.filter(tarea_id=tarea_id)
    asignados_ids = list(asignaciones_actuales.values_list('tecnico_id', flat=True))
    lider_id = asignaciones_actuales.filter(es_lider=True).values_list('tecnico_id', flat=True).first()

    if request.method == 'POST':
        asignados = request.POST.getlist('asignados')
        lider = request.POST.get('lider')

        AsignacionTarea.objects.filter(tarea_id=tarea_id).delete()

        for tecnico_id in asignados:
            AsignacionTarea.objects.create(
                tarea_id=tarea_id,
                tecnico_id=tecnico_id,
                es_lider=(str(tecnico_id) == str(lider))
            )

        return redirect(f"/empresas/{empresa_id}/usuarios/{usuario_id}/tareas/{tarea_id}/")

    return render(request, 'tareas/asignaciones.html', {
        'empresa': empresa,
        'usuario': usuario,
        'tarea': tarea,
        'tecnicos': tecnicos,
        'asignados_ids': asignados_ids,
        'lider_id': lider_id,
    })