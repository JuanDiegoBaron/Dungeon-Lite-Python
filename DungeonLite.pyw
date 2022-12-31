from tkinter import *
from io import open
from random import choice

root = Tk()  # Creacion de la pantalla 

# root.iconbitmap("krigergames.ico")    # Establece un icono para la ventana
root.attributes("-fullscreen",True)
root.title("Kriger Interface") # Establece un titulo a la ventana
#root.geometry("800x600") # Establese las dimenciones de la ventana
root.resizable(0,0) # Permite agrandar/redimencionar la pantalla 
root.config(bg="blue")


# ---------------- Configuracion del frame principal -------------------

framePrincipal=Frame(root,width=1360,height=768) # Creacion del frame principal
framePrincipal.config(bg="#33373A")

framePrincipal.place(x="0",y="0")

# ---------------- Widgets frame principal ------------------------

def salirApp():

	root.destroy()	

bt_Salir = Button(framePrincipal,text="X",fg="red",bg="#390606",bd="0",width="3",height="1",command=salirApp).place(x="1328",y="1")

imagenMenu = PhotoImage(file="colo.png")

# _____________________________________________ IMAGENES JUEGO DE MESA ___________________________________________________

# Otros
imagenOro=PhotoImage(file="oro.png")
imagenCofre=PhotoImage(file="cofre.png")
imagenCuadradoBlanco=PhotoImage(file="noEmenRecom.png")

# iconos estadisticas
imagenCorazon = PhotoImage(file="cora.png")
imagenEspada = PhotoImage(file="espada.png")
imagenBarrera = PhotoImage(file="barrera.png")
imagenArmadura = PhotoImage(file="armadura.png")
imagenMana = PhotoImage(file="mana.png")
imagenSuerte =PhotoImage(file="suerte.png")

# partes del inventario
imagenCabeza = PhotoImage(file="cabeza.png")
imagenPecho = PhotoImage(file="pecho.png")
imagenPiernas = PhotoImage(file="piernas.png")
imagenPies = PhotoImage(file="pies.png")
imagenArma = PhotoImage(file="arma.png")

# dados
img_dado1= PhotoImage(file="dado1.png")
img_dado2= PhotoImage(file="dado2.png")
img_dado3= PhotoImage(file="dado3.png")
img_dado4= PhotoImage(file="dado4.png")
img_dado5= PhotoImage(file="dado5.png")
img_dado6= PhotoImage(file="dado6.png")

# Estrellas
e0=PhotoImage(file="noEstrellas.png")
e1=PhotoImage(file="1s.png")
e2=PhotoImage(file="2s.png")
e3=PhotoImage(file="3s.png")

# Enemigos
enem1=PhotoImage(file="zombie.png")
enem2=PhotoImage(file="esqueleto.png")
enem3=PhotoImage(file="araña.png")
enem4=PhotoImage(file="serpiente.png")
enem5=PhotoImage(file="slime.png")


root.mainloop()