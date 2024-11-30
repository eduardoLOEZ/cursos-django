from django.shortcuts import render, get_object_or_404
from .models import Curso

def listar_cursos(request):
    cursos = Curso.objects.all()  # Obtener todos los cursos
    return render(request, 'listar_cursos.html', {'cursos': cursos})




def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)  # Obtener el curso o devolver 404
    return render(request, 'detalle_curso.html', {'curso': curso})
