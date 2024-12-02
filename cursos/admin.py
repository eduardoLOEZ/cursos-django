from django.contrib import admin
from .models import Curso, PDF

class PDFInline(admin.TabularInline):
    """Permite gestionar los PDFs relacionados directamente desde el curso."""
    model = PDF
    extra = 1  # Número de formularios adicionales vacíos para añadir nuevos PDFs
    verbose_name = "Material PDF"
    verbose_name_plural = "Materiales PDF"

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    """Admin para el modelo Curso."""
    list_display = ('titulo', 'precio', 'descripcion')  # Muestra estos campos en la lista de cursos
    search_fields = ('titulo', 'descripcion')  # Permite buscar cursos por título y descripción
    list_filter = ('precio',)  # Filtros por precio
    inlines = [PDFInline]  # Añade la gestión de PDFs al formulario de cursos

@admin.register(PDF)
class PDFAdmin(admin.ModelAdmin):
    """Admin para el modelo PDF."""
    list_display = ('titulo', 'curso')  # Muestra el título del PDF y el curso relacionado
    search_fields = ('titulo',)  # Permite buscar PDFs por título
    list_filter = ('curso',)  # Filtro por curso
