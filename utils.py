# utils.py
from docx import Document

def save_text(texto, nombre_archivo):
    doc = Document()
    doc.add_paragraph(texto)
    doc.save(nombre_archivo)  # Guarda el archivo con el nombre dinámico
    print(f"Archivo guardado como {nombre_archivo}")  # Muestra el nombre del archivo guardado
