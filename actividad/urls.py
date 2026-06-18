from django.urls import path
from . import views

app_name = 'actividad'

urlpatterns = [
    path('', views.ActividadListView.as_view(), name='list'),
    path('crear/', views.ActividadCreateView.as_view(), name='create'),
    path('<int:pk>/', views.ActividadDetailView.as_view(), name='detail'),
]