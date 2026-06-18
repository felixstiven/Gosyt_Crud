
from django.urls import path
from . import views

app_name = 'evidencias'

urlpatterns = [
    path('', views.EvidenciaListView.as_view(), name='list'),
    path('crear/', views.EvidenciaCreateView.as_view(), name='create'),
    path('<int:pk>/', views.EvidenciaDetailView.as_view(), name='detail'),
    path('<int:pk>/eliminar/', views.EvidenciaDeleteView.as_view(), name='delete'),
]