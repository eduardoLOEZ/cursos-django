from django.db import models
from django.contrib.auth import get_user_model
from cursos.models import Curso

User = get_user_model()

class StripePayment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='payments', verbose_name="Usuario"
    )
    curso = models.ForeignKey(
        Curso, on_delete=models.CASCADE, related_name='payments', verbose_name="Curso"
    )
    stripe_payment_id = models.CharField(
        max_length=100, verbose_name="ID de Pago en Stripe"
    )
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Monto Pagado"
    )
    status = models.CharField(
        max_length=50, default='pending', verbose_name="Estado del Pago"
    )  # 'pending', 'completed', 'failed'
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de Creación"
    )

    def __str__(self):
        return f"{self.user.email} - {self.curso.titulo} - {self.status}"
