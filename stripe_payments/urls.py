from django.urls import path
from . import views
from .views import eliminar_curso


urlpatterns = [
    path('<int:curso_id>/pago/', views.iniciar_pago, name='iniciar_pago'),
    path('success/', views.pago_exitoso, name='pago_exitoso'),
    path('cancel/', views.pago_cancelado, name='pago_cancelado'),
    path('eliminar-curso/<int:curso_id>/', eliminar_curso, name='eliminar_curso'),

    
]
