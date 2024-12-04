from django.urls import path
from . import views

app_name = 'cuestionarios'

urlpatterns = [
    path('<int:curso_id>/', views.cuestionario_fijo, name='mostrar_cuestionario'),
]
