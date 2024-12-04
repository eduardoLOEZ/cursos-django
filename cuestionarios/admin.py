from django.contrib import admin
from .models import Cuestionario, Pregunta, Respuesta, RespuestaUsuario, Certificado

class RespuestaInline(admin.TabularInline):
    model = Respuesta
    extra = 3

class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('texto', 'cuestionario')
    inlines = [RespuestaInline]

class CuestionarioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'curso')

admin.site.register(Cuestionario, CuestionarioAdmin)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(RespuestaUsuario)
admin.site.register(Certificado)
