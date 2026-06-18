from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.UsuarioListView.as_view(), name='list'),
    path('crear/', views.UsuarioCreateView.as_view(), name='create'),
    path('<int:pk>/', views.UsuarioDetailView.as_view(), name='detail'),
    path('<int:pk>/editar/', views.UsuarioUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.UsuarioDeleteView.as_view(), name='delete'),
]