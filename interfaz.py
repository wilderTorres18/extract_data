import tkinter as tk
from tkinter import filedialog
from ocr import extract_text
from utils import save_text
import pyperclip  # Para copiar al portapapeles
from datetime import datetime  # Para obtener la fecha y hora

def abrir_archivo():
    archivo = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[("Archivos PDF", "*.pdf"), ("Imágenes", "*.png;*.jpg")])
    if archivo:
        texto = extract_text(archivo)  # Llama a la función de extracción de texto
        mostrar_texto(texto)          # Muestra el texto extraído
        # Obtener la fecha y hora actuales para generar un nombre único
        fecha_actual = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f"documento_extraido_{fecha_actual}.docx"
        save_text(texto, nombre_archivo)  # Guardamos el texto en Word con el nombre dinámico

def mostrar_texto(texto):
    texto_box.delete(1.0, tk.END)
    texto_box.insert(tk.END, texto)

def copiar_al_portapapeles():
    texto = texto_box.get(1.0, tk.END)
    pyperclip.copy(texto)  # Copia el texto al portapapeles
    print("Texto copiado al portapapeles")

def buscar_texto():
    buscar = entry_buscar.get()  # Obtiene el texto de la entrada de búsqueda
    contenido = texto_box.get(1.0, tk.END)
    if buscar in contenido:
        print(f"'{buscar}' encontrado.")
    else:
        print(f"'{buscar}' no encontrado.")

def create_interfaz():
    root = tk.Tk()
    root.title("Gestión de Documentos Notariales")
    root.geometry("600x400")

    # Crear un Frame para los botones
    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)

    # Botones en una sola fila con colores
    btn_abrir = tk.Button(button_frame, text="Abrir Documento", command=abrir_archivo, bg="blue", fg="white", relief="raised")
    btn_abrir.pack(side=tk.LEFT, padx=10)

    btn_salir = tk.Button(button_frame, text="Salir", command=root.quit, bg="red", fg="white", relief="raised")
    btn_salir.pack(side=tk.LEFT, padx=10)

    btn_copiar = tk.Button(button_frame, text="Copiar al Portapapeles", command=copiar_al_portapapeles, bg="green", fg="white", relief="raised")
    btn_copiar.pack(side=tk.LEFT, padx=10)

    btn_buscar = tk.Button(button_frame, text="Buscar", command=buscar_texto, bg="orange", fg="white", relief="raised")
    btn_buscar.pack(side=tk.LEFT, padx=10)

    btn_ayuda = tk.Button(button_frame, text="Ayuda", bg="purple", fg="white", relief="raised")
    btn_ayuda.pack(side=tk.LEFT, padx=10)

    # Crear la entrada de búsqueda
    global entry_buscar
    entry_buscar = tk.Entry(root, width=40)
    entry_buscar.pack(pady=10)

    # Crear el Textbox para mostrar el texto
    global texto_box
    texto_box = tk.Text(root, width=80, height=40)
    texto_box.pack(pady=10)

    root.mainloop()

