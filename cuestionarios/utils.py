from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse
import io

def generar_certificado(usuario, curso):
    # Crear un buffer para almacenar el PDF
    buffer = io.BytesIO()

    # Crear un canvas para el PDF
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.setTitle("Certificado de Curso")

    # Escribir el contenido del PDF
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawCentredString(300, 750, "Certificado de Finalización")

    pdf.setFont("Helvetica", 14)
    texto = f"Certificamos que {usuario.get_full_name()} ha completado satisfactoriamente"
    pdf.drawCentredString(300, 700, texto)

    texto_curso = f"el curso: {curso.titulo}."
    pdf.drawCentredString(300, 675, texto_curso)

    pdf.setFont("Helvetica", 12)
    pdf.drawCentredString(300, 625, "Fecha de emisión: ____________")
    pdf.drawCentredString(300, 600, "Firma del instructor: ______________________")

    # Finalizar el PDF
    pdf.showPage()
    pdf.save()

    # Obtener el contenido del PDF
    buffer.seek(0)
    return buffer
