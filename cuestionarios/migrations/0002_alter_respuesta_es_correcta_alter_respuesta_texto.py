# Generated by Django 5.1.3 on 2024-12-04 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuestionarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuesta',
            name='es_correcta',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='respuesta',
            name='texto',
            field=models.TextField(),
        ),
    ]