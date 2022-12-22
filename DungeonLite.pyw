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

framePrincipal=Frame(root,width=1366,height=768) # Creacion del frame principal
framePrincipal.config(bg="#33373A")

framePrincipal.place(x="0",y="0")

# ---------------- Widgets frame principal ------------------------

def salirApp():

	root.destroy()	

bt_Salir = Button(framePrincipal,text="X",fg="white",bg="#390606",bd="0",width="3",height="1",command=salirApp).place(x="1336",y="1")

imagenMenu = PhotoImage(file="imagenes/colo.png")

# _____________________________________________ IMAGENES JUEGO DE MESA ___________________________________________________

# Otros
imagenOro=PhotoImage(file="imagenes/oro.png")
imagenCofre=PhotoImage(file="imagenes/cofre.png")
imagenCuadradoBlanco=PhotoImage(file="imagenes/noEmenRecom.png")

# iconos estadisticas
imagenCorazon = PhotoImage(file="imagenes/cora.png")
imagenEspada = PhotoImage(file="imagenes/espada.png")
imagenBarrera = PhotoImage(file="imagenes/barrera.png")
imagenArmadura = PhotoImage(file="imagenes/armadura.png")
imagenMana = PhotoImage(file="imagenes/mana.png")
imagenSuerte =PhotoImage(file="imagenes/suerte.png")

# partes del inventario
imagenCabeza = PhotoImage(file="imagenes/cabeza.png")
imagenPecho = PhotoImage(file="imagenes/pecho.png")
imagenPiernas = PhotoImage(file="imagenes/piernas.png")
imagenPies = PhotoImage(file="imagenes/pies.png")
imagenArma = PhotoImage(file="imagenes/arma.png")

# dados
img_dado1= PhotoImage(file="imagenes/dado1.png")
img_dado2= PhotoImage(file="imagenes/dado2.png")
img_dado3= PhotoImage(file="imagenes/dado3.png")
img_dado4= PhotoImage(file="imagenes/dado4.png")
img_dado5= PhotoImage(file="imagenes/dado5.png")
img_dado6= PhotoImage(file="imagenes/dado6.png")

# Estrellas
e0=PhotoImage(file="imagenes/noEstrellas.png")
e1=PhotoImage(file="imagenes/1s.png")
e2=PhotoImage(file="imagenes/2s.png")
e3=PhotoImage(file="imagenes/3s.png")

# Enemigos
enem1=PhotoImage(file="imagenes/zombie.png")
enem2=PhotoImage(file="imagenes/esqueleto.png")
enem3=PhotoImage(file="imagenes/araña.png")
enem4=PhotoImage(file="imagenes/serpiente.png")
enem5=PhotoImage(file="imagenes/slime.png")


# Creacion del frame del juego
frame_JuegoDeMesa = Frame(framePrincipal,width="1366",height="758",bg="#5F0A0A")
frame_JuegoDeMesa.place(x=0,y=25)

def salir():
					
	frame_JuegoDeMesa.destroy()

def guardar_salir():    
				
	pass

bt_salir=Button(frame_JuegoDeMesa,text="Salir",bg="#390606",width=20,height=1,bd=0,fg="white",command=salir).place(x=1200,y=700)
bt_guardar_salir=Button(frame_JuegoDeMesa,text="Guardar y Salir",bg="#390606",width=20,height=1,bd=0,fg="white",command=guardar_salir).place(x=1050,y=700)



root.mainloop()