#interfaz.py 
import tkinter as tk 
from tkinter import filedialog
from ocr import extract_text

def abrir_archivo():
    archivo = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[("Imágenes", "*.png;*.jpg")])
    if archivo:
        texto = extract_text(archivo)
        mostrar_texto(texto)

def mostrar_texto(texto):
    texto_box.delete(1.0, tk.END)
    texto_box.insert(tk.END, texto)

def create_interfaz():
    root = tk.Tk()
    root.title("Gestión de Documentos Notariales")
    root.geometry("600x400")

    btn_abrir = tk.Button(root, text="Abrir Documento", command=abrir_archivo)
    btn_abrir.pack(pady=20)

    global texto_box
    texto_box = tk.Text(root, width=60, height=15)
    texto_box.pack(pady=10)

    root.mainloop()
