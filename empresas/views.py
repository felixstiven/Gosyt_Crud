from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Empresa

class EmpresaListView(ListView):
    model = Empresa
    template_name = 'empresas/list.html'
    context_object_name = 'empresas'

class EmpresaDetailView(DetailView):
    model = Empresa
    template_name = 'empresas/detail.html'
    context_object_name = 'empresa'

class EmpresaCreateView(CreateView):
    model = Empresa
    template_name = 'empresas/form.html'
    fields = ['nombre_empresa', 'estado']
    success_url = reverse_lazy('empresas:list')

class EmpresaUpdateView(UpdateView):
    model = Empresa
    template_name = 'empresas/form.html'
    fields = ['nombre_empresa', 'estado']
    context_object_name = 'empresa'
    success_url = reverse_lazy('empresas:list')

class EmpresaDeleteView(DeleteView):
    model = Empresa
    template_name = 'empresas/confirm_delete.html'
    context_object_name = 'empresa'
    success_url = reverse_lazy('empresas:list')