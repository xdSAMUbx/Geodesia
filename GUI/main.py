import tkinter as tk
from tkinter import ttk

class Ventana:

    def __init__(self):
        self.window = tk.Tk()
        self.interfaz()

    def interfaz(self):
        #Titulo
        self.window.title("Geodesia")
        
        # Centrar la ventana en la mitad del monitor
        self.window.update_idletasks()
        width = 1000
        height = 800
        x = (self.window.winfo_screenwidth() - width) // 2
        y = (self.window.winfo_screenheight() - height) // 2
        self.window.geometry(f"{width}x{height}+{x}+{y}")
        
    def main(self):
        self.window.mainloop()

# Crear una instancia de la clase Ventana
ventana = Ventana()
ventana.main()
