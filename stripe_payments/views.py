import stripe
from django.conf import settings
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from cursos.models import Curso
from .models import StripePayment
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib import messages


stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def iniciar_pago(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    user = request.user

    if request.method == 'POST':
        # Crear un registro de pago preliminar
        payment = StripePayment.objects.create(
            user=user,
            curso=curso,
            amount=curso.precio,
            status='pending'
        )

        # Crear la sesión de pago de Stripe
        try:
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'mxn',
                        'product_data': {
                            'name': curso.titulo,
                            'description': curso.descripcion,
                        },
                        'unit_amount': int(curso.precio * 100),  # Precio en centavos
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=request.build_absolute_uri(
                    f'/stripe/success/?payment_id={payment.id}'
                ),
                cancel_url=request.build_absolute_uri('/stripe/cancel/'),
            )
            return redirect(session.url, code=303)
        except Exception as e:
            return render(request, 'error.html', {'message': str(e)})

    return render(request, 'stripe_payments/iniciar_pago.html', {'curso': curso})


@login_required
def pago_exitoso(request):
    payment_id = request.GET.get('payment_id')
    payment = get_object_or_404(StripePayment, id=payment_id, user=request.user)

    # Actualizar el estado del pago
    payment.status = 'completed'
    payment.save()

    # Agregar el curso al usuario
    user = request.user
    curso = payment.curso  # Obtenemos el curso desde el pago
    user.cursos_comprados.add(curso)
    user.save()

    # Enviar correo de agradecimiento
    enviar_correo_agradecimiento(user, curso)

    return render(request, 'success.html', {'curso': curso})



@login_required
def pago_cancelado(request):
    return render(request, 'cancel.html', {'message': 'El pago fue cancelado. Inténtalo nuevamente.'})



def enviar_correo_agradecimiento(user, curso):
    """Envía un correo de agradecimiento al usuario."""
    subject = f"¡Gracias por tu compra, {user.first_name}!"
    from_email = settings.EMAIL_HOST_USER
    recipient = [user.email]

    # Renderizar la plantilla del correo
    html_content = render_to_string('agradecimiento_compra.html', {'user': user, 'curso': curso})

    # Crear el correo con HTML
    email = EmailMultiAlternatives(subject, "", from_email, recipient)
    email.attach_alternative(html_content, "text/html")
    email.send()


@login_required
def eliminar_curso(request, curso_id):
    user = request.user
    curso = get_object_or_404(Curso, id=curso_id)

    # Verificar que el curso está en la lista de cursos comprados
    if curso in user.cursos_comprados.all():
        user.cursos_comprados.remove(curso)
        messages.success(request, f"El curso '{curso.titulo}' ha sido eliminado de tu lista de cursos comprados.")
    else:
        messages.error(request, "No tienes este curso en tu lista de cursos comprados.")

    return redirect('user_profile')