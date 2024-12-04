from django.db import models
from django.conf import settings
from cursos.models import Curso
from django.db import models
from django.core.exceptions import ValidationError

# Modelo para el Cuestionario
class Cuestionario(models.Model):
    curso = models.OneToOneField(Curso, on_delete=models.CASCADE, related_name='cuestionario')
    titulo = models.CharField(max_length=255, help_text="Título del cuestionario")
    descripcion = models.TextField(blank=True, null=True, help_text="Descripción del cuestionario")

    def __str__(self):
        return f"Cuestionario para {self.curso.titulo}"

# Modelo para las Preguntas
class Pregunta(models.Model):
    cuestionario = models.ForeignKey(Cuestionario, on_delete=models.CASCADE, related_name='preguntas')
    texto = models.TextField(help_text="Texto de la pregunta")

    def __str__(self):
        return self.texto

# Modelo para las Opciones de Respuesta


from django.core.exceptions import ValidationError

class Respuesta(models.Model):
    texto = models.CharField(max_length=255)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='respuestas')
    es_correcta = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Verifica si ya hay una respuesta correcta
        if self.es_correcta:
            respuestas_correctas = Respuesta.objects.filter(pregunta=self.pregunta, es_correcta=True)
            if self.pk:
                respuestas_correctas = respuestas_correctas.exclude(pk=self.pk)
            if respuestas_correctas.exists():
                raise ValidationError("Solo puede haber una respuesta correcta por pregunta.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.texto


# Modelo para las Respuestas del Usuario
class RespuestaUsuario(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='respuestas_usuario')
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='respuestas_usuario')
    respuesta = models.ForeignKey(Respuesta, on_delete=models.CASCADE, related_name='respuestas_usuario')
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.email} - {self.pregunta.texto}"

# Modelo para los Certificados
class Certificado(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='certificados')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='certificados')
    archivo = models.FileField(upload_to='certificados/', help_text="Certificado en PDF")
    generado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Certificado de {self.usuario.email} para {self.curso.titulo}"
