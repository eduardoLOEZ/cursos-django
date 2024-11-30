import logging
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from cursos.models import Curso  # Importa el modelo Curso



# Configurar el logger
logger = logging.getLogger('users')

# Vista para registrar un nuevo usuario
def register_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name_paternal = request.POST.get('last_name_paternal')
        last_name_maternal = request.POST.get('last_name_maternal')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')

        # Log de los datos recibidos
        logger.debug(f"Intentando registrar usuario: {email}, rol: {role}")

        if not all([first_name, last_name_paternal, email, password, role]):
            logger.warning("Campos incompletos en el registro.")
            messages.error(request, "Todos los campos son obligatorios.")
            return redirect('register')

        try:
            user = CustomUser.objects.create_user(
                email=email,
                password=password,
                first_name=first_name,
                last_name_paternal=last_name_paternal,
                last_name_maternal=last_name_maternal,
                role=role,
            )
            logger.info(f"Usuario registrado exitosamente: {email}")
            messages.success(request, "Usuario registrado exitosamente. Inicia sesión.")
            return redirect('login')
        except Exception as e:
            logger.error(f"Error al registrar el usuario {email}: {e}")
            messages.error(request, f"Error al registrar el usuario: {e}")
            return redirect('register')

    return render(request, 'users/register.html')

@csrf_exempt
# Vista para iniciar sesión
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Log de los datos recibidos
        logger.debug(f"Intentando iniciar sesión con el correo: {email}")

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            logger.info(f"Inicio de sesión exitoso para el usuario: {email}")
            messages.success(request, f"Bienvenido, {user.first_name}!")
            return redirect('home')  # Redirigir a la página de inicio
        else:
            logger.warning(f"Fallo en el inicio de sesión para el usuario: {email}")
            messages.error(request, "Credenciales incorrectas. Verifica tu correo y contraseña.")
            return redirect('login')

    return render(request, 'users/login.html')

# Vista para cerrar sesión
def logout_user(request):
    if request.user.is_authenticated:
        logger.info(f"Usuario {request.user.email} cerró sesión.")
    else:
        logger.warning("Intento de cerrar sesión sin estar autenticado.")
    logout(request)
    messages.success(request, "Sesión cerrada exitosamente.")
    return redirect('login')


@login_required
def upload_profile_picture(request):
    if request.method == 'POST' and request.FILES.get('profile_picture'):
        user = request.user
        profile_picture = request.FILES['profile_picture']
        
        # Actualiza la foto de perfil del usuario
        user.profile_picture = profile_picture
        user.save()
        
        return JsonResponse({'message': 'Foto de perfil actualizada con éxito'}, status=200)
    return JsonResponse({'error': 'No se subió ningún archivo'}, status=400)


# Vista para la página de inicio
@login_required
def home(request):
    cursos = Curso.objects.all()  # Obtiene todos los cursos
    return render(request, 'home.html', {'cursos': cursos})

@login_required
def cursos(request):
    return render(request, 'cursos.html')

@login_required
def contacto(request):
    return render(request, 'contacto.html')

@login_required
def user_profile(request):
    user = request.user  # Obtiene al usuario autenticado
    return render(request, 'profile.html')