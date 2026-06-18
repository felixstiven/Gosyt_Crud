from django.urls import path
from . import views

app_name = 'insumos'

urlpatterns = [
    path('', views.InsumoListView.as_view(), name='list'),
    path('crear/', views.InsumoCreateView.as_view(), name='create'),
    path('<int:pk>/', views.InsumoDetailView.as_view(), name='detail'),
    path('<int:pk>/editar/', views.InsumoUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.InsumoDeleteView.as_view(), name='delete'),
]