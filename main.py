from AIService import AIService
from OrderManager import exect_order
import tkinter as tk
import threading
import time


def test1():
    print("Ejecutando orden 1")

def test2():
    print("Ejecutando orden 2")

# Frases a comparar
oraciones = {
    "Presiona el botón continuar":test1,
    "Cierra el programa":test2
}

def tarea_en_bucle():
    while True:
        exect_order(oraciones)
        time.sleep(1)

def iniciar_hilo():
    hilo = threading.Thread(target=tarea_en_bucle, daemon=True)
    hilo.start()

def shortcut (event = None):
    print("Ejecutando shortcut")
    exect_order(oraciones)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi interfaz simple")
ventana.geometry("500x450")


# Crear botones
boton1 = tk.Button(ventana, text="Continuar", command=test1)
boton1.pack(pady=10)

boton2 = tk.Button(ventana, text="Cerrar programa", command=test2)
boton2.pack(pady=10)

# Ejecutar la app
ventana.bind('<Control-o>', shortcut)

ventana.mainloop()






