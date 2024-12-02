from django.db import models

class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    enlace_video = models.URLField()
    imagen_portada = models.ImageField(upload_to='cursos/portadas/', default='cursos/portadas/default.png')
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.titulo


class PDF(models.Model):
    titulo = models.CharField(max_length=255, help_text="Título del PDF (lectura o material del curso)")
    archivo = models.FileField(upload_to='pdfs/', help_text="Sube el archivo PDF")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='pdfs')  # Relaciona con el modelo Curso

    def __str__(self):
        return self.titulo
