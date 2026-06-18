from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Usuario
from empresas.models import Empresa

class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuarios/list.html'
    context_object_name = 'usuarios'

    def get_queryset(self):
        return Usuario.objects.filter(empresa_id=self.kwargs['empresa_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empresa'] = Empresa.objects.get(pk=self.kwargs['empresa_id'])
        return context

class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = 'usuarios/detail.html'
    context_object_name = 'usuario'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empresa'] = Empresa.objects.get(pk=self.kwargs['empresa_id'])
        return context

class UsuarioCreateView(CreateView):
    model = Usuario
    template_name = 'usuarios/form.html'
    fields = ['nombre', 'correo', 'contraseña', 'rol', 'area', 'cargo']

    def form_valid(self, form):
        form.instance.empresa_id = self.kwargs['empresa_id']
        return super().form_valid(form)

    def get_success_url(self):
        return f"/empresas/{self.kwargs['empresa_id']}/usuarios/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empresa'] = Empresa.objects.get(pk=self.kwargs['empresa_id'])
        return context

class UsuarioUpdateView(UpdateView):
    model = Usuario
    template_name = 'usuarios/form.html'
    fields = ['nombre', 'correo', 'contraseña', 'rol', 'area', 'cargo']
    context_object_name = 'usuario'

    def get_success_url(self):
        return f"/empresas/{self.kwargs['empresa_id']}/usuarios/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empresa'] = Empresa.objects.get(pk=self.kwargs['empresa_id'])
        return context

class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'usuarios/confirm_delete.html'
    context_object_name = 'usuario'

    def get_success_url(self):
        return f"/empresas/{self.kwargs['empresa_id']}/usuarios/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empresa'] = Empresa.objects.get(pk=self.kwargs['empresa_id'])
        return context