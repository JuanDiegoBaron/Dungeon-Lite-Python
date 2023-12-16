# from tkinter import *
# from random import choice,randint

# raiz = Tk()

## BUSCAR COMO HACER UNA ANIMACION





# ventana=Frame(raiz,width=500,height=500,bg="black").pack()

# class pj:

# 	def __init__(self):

# 		self.vida=StringVar()
# 		self.mana=StringVar()
# 		self.fuerza=StringVar()
# 		self.aguante=StringVar()
# 		self.agilidad=StringVar()
# 		self.inteligencia=StringVar()
# 		self.magia=StringVar()

# 		self.habilidades={"slot1":"Quemar","slot2":"Congelar","slot3":"Sacudir"}

# 		self.dañoMin=StringVar()
# 		self.dañoMax=StringVar()

# 		et_vida=Entry(ventana,textvariable=self.vida,width=4).place(x=0,y=0)
# 		lb_vida=Label(ventana,text="vida").place(x=50,y=0)
		
# 		et_mana=Entry(ventana,textvariable=self.mana,width=4).place(x=0,y=50)
# 		lb_mana=Label(ventana,text="mana").place(x=50,y=50)
		
# 		et_fuerza=Entry(ventana,textvariable=self.fuerza,width=4).place(x=0,y=100)
# 		lb_fuerza=Label(ventana,text="fuerza").place(x=50,y=100)
		
# 		et_aguante=Entry(ventana,textvariable=self.aguante,width=4).place(x=0,y=150)
# 		lb_aguante=Label(ventana,text="aguante").place(x=50,y=150)
		
# 		et_agilidad=Entry(ventana,textvariable=self.agilidad,width=4).place(x=0,y=200)
# 		lb_agilidad=Label(ventana,text="agilidad").place(x=50,y=200)
		
# 		et_inteligencia=Entry(ventana,textvariable=self.inteligencia,width=4).place(x=0,y=250)
# 		lb_inteligenia=Label(ventana,text="inteligencia").place(x=50,y=250)
		
# 		et_magia=Entry(ventana,textvariable=self.magia,width=4).place(x=0,y=300)
# 		lb_magia=Label(ventana,text="magia").place(x=50,y=300)
		
# 		et_dañoMin=Entry(ventana,textvariable=self.dañoMin,width=4).place(x=0,y=350)
# 		lb_dañoMin=Label(ventana,text="dañoMin").place(x=50,y=350)
		
# 		et_dañoMax=Entry(ventana,textvariable=self.dañoMax,width=4).place(x=0,y=400)
# 		lb_dañoMin=Label(ventana,text="et_dañoMax").place(x=50,y=400)

# 	def actualizar(self):
	
# 		self.vida.set(int(vida+))	


# class enem:

# 	def __init__(self):

# 		pass		

# pj=pj()
#______________________________________________________________________________________


# raiz.mainloop()


import tkinter as tk

class InventarioApp:
	
    def __init__(self, root):
        self.root = root
        self.root.title("Inventario")

        # Crear un diccionario para almacenar las posiciones de los ítems en el inventario
        self.inventario_posiciones = {
            "mano_derecha": (50, 50),
            "mano_izquierda": (150, 50),
            "cabeza": (100, 150),
            "pecho": (50, 250),
            "piernas": (150, 250),
        }

        # Crear una etiqueta para cada posición del inventario
        self.etiquetas = {}
        for posicion, (x, y) in self.inventario_posiciones.items():

            etiqueta = tk.Label(root, text=posicion, borderwidth=2, relief="solid")
            etiqueta.place(x=x, y=y, width=50, height=50)
            etiqueta.bind("<ButtonPress-1>", lambda event, pos=posicion: self.on_drag_start(event, pos))
            etiqueta.bind("<B1-Motion>", self.on_drag_motion)
            etiqueta.bind("<ButtonRelease-1>", self.on_drag_release)
            self.etiquetas[posicion] = etiqueta

        # Crear una etiqueta para cada ítem
        self.items = {
            "espada": tk.PhotoImage(file="imagenes/cofre.png"),
            "escudo": tk.PhotoImage(file="imagenes/esqueleto.png"),
            # Agrega más ítems según sea necesario
        }

        # Crear un diccionario para rastrear la posición actual de cada ítem
        self.items_posiciones = {}

    def on_drag_start(self, event, posicion):
        # Guardar la posición inicial del ítem y la posición del ratón
        self.dragged_item = self.items_posiciones.get(posicion)
        self.start_x = event.x_root
        self.start_y = event.y_root

    def on_drag_motion(self, event):
        if hasattr(self, "dragged_item"):
            # Mover el ítem mientras el ratón se arrastra
            delta_x = event.x_root - self.start_x
            delta_y = event.y_root - self.start_y
            self.root.geometry("+{}+{}".format(event.x_root - delta_x, event.y_root - delta_y))

    def on_drag_release(self, event):
        if hasattr(self, "dragged_item"):
            # Encontrar la posición más cercana en el inventario y mover el ítem allí
            x, y = self.root.winfo_pointerxy()
            nearest_position = self.find_nearest_position(x, y)
            if nearest_position:
                self.items_posiciones[nearest_position] = self.dragged_item
                x, y = self.inventario_posiciones[nearest_position]
                self.etiquetas[nearest_position].place(x=x, y=y)
            delattr(self, "dragged_item")

    def find_nearest_position(self, x, y):
        # Encontrar la posición más cercana en el inventario
        for posicion, (px, py) in self.inventario_posiciones.items():
            distance = ((x - px) ** 2 + (y - py) ** 2) ** 0.5
            if distance < 30:  # Considerar solo las posiciones dentro de un radio específico
                return posicion
        return None

if __name__ == "__main__":
    root = tk.Tk()
    app = InventarioApp(root)
    root.geometry("300x400")
    root.mainloop()
