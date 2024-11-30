from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_cursos, name='listar_cursos'),  # Ruta para la lista de cursos
    path('<int:curso_id>/', views.detalle_curso, name='detalle_curso'),  # Ruta para ver el detalle de un curso


]
