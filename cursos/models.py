from django.db import models

class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    enlace_video = models.URLField()
    imagen_portada = models.ImageField(upload_to='cursos/portadas/', default='cursos/portadas/default.png')
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Nuevo campo

    def __str__(self):
        return self.titulo
