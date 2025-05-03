#utils
def save_text(texto, nombre_archivo="documento_extraido.txt"):
    with open(nombre_archivo, "w") as f:
        f.write(texto)