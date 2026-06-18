from django.urls import path
from . import views

app_name = 'tareas'

urlpatterns = [
    path('', views.TareaListView.as_view(), name='list'),
    path('crear/', views.TareaCreateView.as_view(), name='create'),
    path('<int:pk>/', views.TareaDetailView.as_view(), name='detail'),
    path('<int:pk>/editar/', views.TareaUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.TareaDeleteView.as_view(), name='delete'),
    path('<int:tarea_id>/asignaciones/', views.asignaciones_view, name='asignaciones'),
]