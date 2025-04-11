from laptop_business import Laptop_Business
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

class App:
    def __init__(self, root):
        self.root = root
        self.laptops = []
        self.imagenes = ["C:\\Users\\MARTIN\\Documents\\KrakeDev\\Modulo_5\\Ejercicios\\POO\\img\\1.jpg","C:\\Users\\MARTIN\\Documents\\KrakeDev\\Modulo_5\\Ejercicios\\POO\\img\\2.jpg","C:\\Users\\MARTIN\\Documents\\KrakeDev\\Modulo_5\\Ejercicios\\POO\\img\\3.jpg","C:\\Users\\MARTIN\\Documents\\KrakeDev\\Modulo_5\\Ejercicios\\POO\\img\\4.jpg","C:\\Users\\MARTIN\\Documents\\KrakeDev\\Modulo_5\\Ejercicios\\POO\\img\\5.jpg","C:\\Users\\MARTIN\\Documents\\KrakeDev\\Modulo_5\\Ejercicios\\POO\\img\\6.jpg"]
        root.title("Ingresar Datos")
        self.setup_ui()

    def setup_ui(self):
        ttk.Label(self.root, text="Marca").grid(row=0, column=0)
        self.marca= tk.StringVar()
        ttk.Entry(self.root, textvariable=self.marca).grid(row=0, column=1)

        ttk.Label(self.root, text="Procesador").grid(row=1, column=0)
        self.procesador= tk.StringVar()
        ttk.Entry(self.root, textvariable=self.procesador).grid(row=1, column=1)

        ttk.Label(self.root, text="Memoria").grid(row=2, column=0)
        self.memoria= tk.StringVar()
        ttk.Entry(self.root, textvariable=self.memoria).grid(row=2, column=1)

        ttk.Label(self.root, text="Almacenamiento").grid(row=3, column=0)
        self.almacenamiento= tk.StringVar()
        ttk.Entry(self.root, textvariable=self.almacenamiento).grid(row=3, column=1)

        ttk.Label(self.root, text="Duración de Batería").grid(row=4, column=0)
        self.duracion_bateria= tk.StringVar()
        ttk.Entry(self.root, textvariable=self.duracion_bateria).grid(row=4, column=1)

        ttk.Label(self.root, text="Precio").grid(row=5, column=0)
        self.precio= tk.StringVar()
        ttk.Entry(self.root, textvariable=self.precio).grid(row=5, column=1)

        ttk.Label(self.root, text="Impuesto").grid(row=6, column=0)
        self.impuesto= tk.StringVar()
        ttk.Entry(self.root, textvariable=10).grid(row=6, column=1)

        ttk.Button(self.root, text="Agregar", command=self.agregar_laptop).grid(row=7, column=0)

        self.mostrar_laptops = tk.Text(self.root, width=50, height=10)
        self.mostrar_laptops.grid(row=6, column=0, columnspan=2)
        self.canva = tk.Canvas(self.root, width=200, height=200)
        self.canva.grid(row=1, column=3, rowspan=6)
    
    def agregar_laptop(self):
        nueva_laptop = Laptop_Business(self.marca.get(), self.procesador.get(), self.memoria.get(), self.almacenamiento.get(), self.duracion_bateria.get(), self.precio.get(), self.impuesto.get())
        self.laptops.append(nueva_laptop)
        self.mostrar_laptops.insert(tk.END,f"{self.laptops[-1].__str__()}\n")

        self.motrar_imagen_aleatoria()

    def motrar_imagen_aleatoria(self):
        image_path = random.choice(self.imagenes)
        imagen = Image.open(image_path)
        imagen = imagen.resize((200, 200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(imagen)

        self.canva.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canva.image = photo
        pass

root = tk.Tk()
app=App(root)
root.mainloop()