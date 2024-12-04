from django.shortcuts import render, get_object_or_404
from .models import Curso

def listar_cursos(request):
    cursos = Curso.objects.all()  # Obtener todos los cursos
    return render(request, 'listar_cursos.html', {'cursos': cursos})


def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    is_purchased = hasattr(request.user, 'cursos_comprados') and curso in request.user.cursos_comprados.all()

    
    # Transformar URL al formato embebible si es necesario
    if curso.enlace_video.startswith("https://www.youtube.com/watch?v="):
        video_id = curso.enlace_video.split('=')[1]
        curso.enlace_video = f"https://www.youtube.com/embed/{video_id}"

    return render(request, 'detalle_curso.html', {'curso': curso, 'is_purchased': is_purchased})


