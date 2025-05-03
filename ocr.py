import pytesseract
from PIL import Image

def extract_text(imagen_patch):
    imagen = Image.open(imagen_patch)
    texto = pytesseract.image_to_string(imagen)
    return texto