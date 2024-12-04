from django.shortcuts import render

def cuestionario_fijo(request, curso_id):
    # Puedes agregar aquí lógica adicional si deseas personalizar algo según el curso.
    return render(request, 'mostrar_cuestionario.html', {'curso_id': curso_id})
