from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_vuelo, name='registrar_vuelo'),
    path('listar/', views.listar_vuelos, name='listar_vuelos'),
    path('estadisticas/', views.estadisticas_vuelos, name='estadisticas_vuelos'),
]