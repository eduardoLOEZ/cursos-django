# Generated by Django 5.1.3 on 2024-11-30 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
        ('users', '0002_customuser_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='cursos_comprados',
            field=models.ManyToManyField(blank=True, related_name='usuarios', to='cursos.curso', verbose_name='Cursos Comprados'),
        ),
    ]