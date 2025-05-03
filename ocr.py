#ocr.py
import pytesseract
from PIL import Image
from pdf2image import convert_from_path

def extract_text(archivo):
    if archivo.lower().endswith('.pdf'):
        # Convertir el PDF en imágenes
        paginas = convert_from_path(archivo, 300)  # Convierte el PDF a imágenes a 300 DPI
        texto = ""
        for pagina in paginas:
            # Extraer texto de cada página usando pytesseract
            texto += pytesseract.image_to_string(pagina)
        return texto
    else:
        # Si no es un PDF, procesar la imagen
        imagen = Image.open(archivo)
        texto = pytesseract.image_to_string(imagen)
        return texto
