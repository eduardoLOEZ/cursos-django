# Generated by Django 5.1.3 on 2024-12-04 03:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cursos', '0003_alter_pdf_archivo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.FileField(help_text='Certificado en PDF', upload_to='certificados/')),
                ('generado', models.DateTimeField(auto_now_add=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificados', to='cursos.curso')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificados', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cuestionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text='Título del cuestionario', max_length=255)),
                ('descripcion', models.TextField(blank=True, help_text='Descripción del cuestionario', null=True)),
                ('curso', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cuestionario', to='cursos.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(help_text='Texto de la pregunta')),
                ('cuestionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preguntas', to='cuestionarios.cuestionario')),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(help_text='Texto de la respuesta', max_length=255)),
                ('es_correcta', models.BooleanField(default=False, help_text='Marcar si esta respuesta es correcta')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respuestas', to='cuestionarios.pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='RespuestaUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respuestas_usuario', to='cuestionarios.pregunta')),
                ('respuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respuestas_usuario', to='cuestionarios.respuesta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respuestas_usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
