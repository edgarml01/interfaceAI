from AIService import AIService
from OrderManager import exect_order
import tkinter as tk
import threading
import time


def test1():
    print("Ejecutando orden 1")
def test2():
    print("Ejecutando orden 2")
def test3():
    print("Ejecutando orden 3")

# Frases a comparar
oraciones = {
    "Presiona el botón continuar":test1,
    "Presiona el botón para retroceder":test2,
    "Cierra el programa":test3
}

def tarea_en_bucle():
    while True:
        exect_order(oraciones)
        time.sleep(1)

def iniciar_hilo():
    hilo = threading.Thread(target=tarea_en_bucle, daemon=True)
    hilo.start()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi interfaz simple")
ventana.geometry("300x150")

# Crear botones
boton1 = tk.Button(ventana, text="Botón 1", command=test1)
boton1.pack(pady=10)

boton2 = tk.Button(ventana, text="Botón 2", command=test2)
boton2.pack(pady=10)

# Ejecutar la app
iniciar_hilo()

ventana.mainloop()






