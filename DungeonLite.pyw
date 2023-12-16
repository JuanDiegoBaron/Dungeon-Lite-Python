from tkinter import *
from io import open
from random import choice,choices
from random import randint
from sqlite3 import *
from PIL import Image, ImageTk   # ver si existe esta libreria

# modulos
from src.mapa import Mapa
from src.personaje import Personaje
from src.partida import Partida

from gui.interfaz import *
from gui.ventana import *
from gui.interfaz import *



""" TAREAS
	* TERMINAR EL SISTEMA DE RECOMPENZA 
	* continuar con las zonas
	* continuar con ver objeto
	* agregar una barra de informacion mas
	* hacer mas espacio para los widgets
	* ocultal los botones de movimiento(LISTO)
	"""

""" IDEAS PARA AGREGAR ,
	¡¡ ojo pueden  ser complicadas !!

	* AGREGAR ANIMACIONES
		pueden haber muchas animaciones en el juego, tengo que buscar como se hacen

	* Agregar un mercado real, por ejemplo, los precios sueben y bajan, y en cada reino tienen un mercado diferente ?? 

	* CONOCIMIENTO EN NPC: Si el npc tiene conocimiento sobre eso,
		te contara lo que sabe. (para controlar el conocimiento de un npc, abra una variale que sera un array,
		que contendra diccionarios con los diferentes temas,y si los conoces o no)

		ejemplo
			conocimientos=[
			{"Rey malvado":False},
			{"Bandidos del Bosque":True},
			{"Lago contaminado":True}]

"""

""" CLASES

	NPCS: Los npcs pueden dar misiones al jugador, vender objetos y dar informacion.
		tipos de npcs: aldeano, herrero, vendedor, tabernero, guarida, rey o realeza.
		Le puedes preguntar a los npcs,sobre temas en particular. 

	misiones:
		se puden conseguir de npcs, las misiones consisten en ir a un lugar o mas lugares y,
		matar un enemigo o un jefe, buscar un objeto, Hablar con un npc. las misiones pueden tener mas de 
		una fase.Las Misiones secundarias no tendran mucho dialogo porque seran creadas procedularmente. Por lo tanto,
		solo se dara la informacion especifica de lo que se requiere, y la recompenza.
	
		por ejemplo.

		Fase 1: ir a x lugar a buscar un objeto
		Fase 2: ir a otro lugar x y hablar con un npc
		Fase final: volver al npc que dio la mision para recoger la recompenza.

	ZONAS:

		*PACIVAS: (0% DE BATALLA) REINOS, BOSQUES VERDES, MARES
		*NEUTRALES: (50% DE BATALLA) BOSQUES PROFUNDOS, PANTANOS, Ruinas
		*HOSTILES : (100% DE BATALLA) CEMENTERIOS, BOSQUES OSCUROS,Cementerios

	EDIFICIOS: 
		CASAS:TIENEN DE 0 A N NPCS, O FAMILIA.
		CUEVAS: tiene animales enemigos. y tesoros.
		mazmorras: tienen enemigos y tesoros. tienen niveles.
		CASTILLOS: DONDE VIVEN LOS REYES, TIENDAS/COMERCIOS,
		Tumbas:

"""

#________________________ ROOT ____________________________

root = Tk()  # Creacion de la pantalla 
root.attributes("-fullscreen",True)
root.title("DUNGEON LITE") # Establece un titulo a la ventana
root.resizable(0,0) # Permite agrandar/redimencionar la pantalla 
root.config(bg="blue")

#__________________________  FRAME MENU _______________________________

def crearFrameNuevaPartida():

	def crearPartida():

		global partidas

		#creacion del objeto del personaje
		if(nombre.get()=="" or razaSeleccionada.get()=="" or claseSeleccionada.get()==""):

			return

		vidaAux=100+int(aguante.get())*5
		manaAux=100+int(inteligencia.get())*5
		personaje=Personaje(nombre.get(),razaSeleccionada.get(),claseSeleccionada.get(),vidaAux,manaAux,int(fuerza.get()),int(aguante.get()),int(inteligencia.get()),int(magia.get()),int(agilidad.get()),int(percepcion.get()))
		# personaje.registrarPersonaje()
		
		# enemigo=Enemigo()
		# enemigo.registrarEnemigo()
		# creacion del objeto de la partida 
		partida=Partida(personaje)

		partida.comenzarPartida()

		# agrego la partida a la coleccion
		# partida.registrarPartida()

		salirNuevaPartida()

	def salirNuevaPartida():

		frameNuevaPartida.destroy()

	# ESTADISTICAS JUGADOR
	
	def subirFuerza():
		global puntosDisponibles
			
		if(puntosDisponibles-1<0):
			return
		else:	
			puntosDisponibles-=1
			fuerza.set(int(fuerza.get())+1)
			Label(frameEstadisticas,text=f"pts disponibles: {puntosDisponibles}").place(x=5,y=5)

	def bajarFuerza():
		global puntosDisponibles

		if(int(fuerza.get())==0):
			return
		else:
			puntosDisponibles+=1
			fuerza.set(int(fuerza.get())-1)	
			Label(frameEstadisticas,text=f"pts disponibles: {puntosDisponibles}").place(x=5,y=5)

	def subirAguante():
		global puntosDisponibles
			
		if(puntosDisponibles-1<0):
			return
		else:	
			puntosDisponibles-=1
			aguante.set(int(aguante.get())+1)
			Label(frameEstadisticas,text=f"pts disponibles: {puntosDisponibles}").place(x=5,y=5)

	def bajarAguante():
		global puntosDisponibles

		if(int(aguante.get())==0):
			return
		else:
			puntosDisponibles+=1
			aguante.set(int(aguante.get())-1)	
			Label(frameEstadisticas,text=f"pts disponibles: {puntosDisponibles}").place(x=5,y=5)

	def subirInteligencia():
		global puntosDisponibles
			
		if(puntosDisponibles-1<0):
			return
		else:	
			puntosDisponibles-=1
			inteligencia.set(int(inteligencia.get())+1)
			Label(frameEstadisticas,text=f"pts disponibles: {puntosDisponibles}").place(x=5,y=5)

	def bajarInteligencia():
		global puntosDisponibles

		if(int(inteligencia.get())==0):
			return
		else:
			puntosDisponibles+=1
			inteligencia.set(int(inteligencia.get())-1)	
			Label(frameEstadisticas,text=f"pts disponibles: {puntosDisponibles}").place(x=5,y=5)

	def subirMagia():
		global puntosDisponibles
			
		if(puntosDisponibles-1<0):
			return
		else:	
			puntosDisponibles-=1
			magia.set(int(magia.get())+1)
			Label(frameEstadisticas,text=f"pts disponibles: {puntosDisponibles}").place(x=5,y=5)
			
	def bajarMagia():

		global puntosDisponibles

		if(int(magia.get())==0):
			return
		else:
			puntosDisponibles+=1
			magia.set(int(magia.get())-1)	
			Label(frameEstadisticas,text=f"pts disponibles: {puntosDisponibles}").place(x=5,y=5)

	def subirAgilidad():
		global puntosDisponibles
			
		if(puntosDisponibles-1<0):
			return
		else:	
			puntosDisponibles-=1
			agilidad.set(int(agilidad.get())+1)
			Label(frameEstadisticas,text=f"pts disponibles: {puntosDisponibles}").place(x=5,y=5)

	def bajarAgilidad():
		global puntosDisponibles

		if(int(agilidad.get())==0):
			return
		else:
			puntosDisponibles+=1
			agilidad.set(int(agilidad.get())-1)	
			Label(frameEstadisticas,text=f"pts disponibles: {puntosDisponibles}").place(x=5,y=5)

	def subirPercepcion():
		global puntosDisponibles
			
		if(puntosDisponibles-1<0):
			return
		else:	
			puntosDisponibles-=1
			percepcion.set(int(percepcion.get())+1)	
			Label(frameEstadisticas,text=f"pts disponibles: {puntosDisponibles}").place(x=5,y=5)			

	def bajarPercepcion():

		global puntosDisponibles

		if(int(percepcion.get())==0):
			return
		else:
			puntosDisponibles+=1
			percepcion.set(int(percepcion.get())-1)	
			Label(frameEstadisticas,text=f"pts disponibles: {puntosDisponibles}").place(x=5,y=5)

	# Radio-Buttons CLASE

	def seleccionarGuerrero():

		global puntosDisponibles
		puntosDisponibles=5
		Label(frameEstadisticas,text=f"pts disponibles: {puntosDisponibles}").place(x=5,y=5)

		fuerza.set(2)
		aguante.set(2)
		inteligencia.set(0)
		magia.set(0)
		agilidad.set(0)
		percepcion.set(0)

		claseSeleccionada.set("Guerrero")

	def seleccionarMago():	

		global puntosDisponibles
		puntosDisponibles=5
		Label(frameEstadisticas,text=f"pts disponibles: {puntosDisponibles}").place(x=5,y=5)

		fuerza.set(0)
		aguante.set(0)
		inteligencia.set(2)
		magia.set(2)
		agilidad.set(0)
		percepcion.set(0)

		claseSeleccionada.set("Mago")

	def seleccionarPicaro():

		global puntosDisponibles
		puntosDisponibles=5
		Label(frameEstadisticas,text=f"pts disponibles: {puntosDisponibles}").place(x=5,y=5)

		fuerza.set(0)
		aguante.set(0)
		inteligencia.set(0)
		magia.set(0)
		agilidad.set(2)
		percepcion.set(2)

		claseSeleccionada.set("Picaro")	

	# Radio-Buttons RAZA
	


	nombre=StringVar()
	razaSeleccionada=StringVar()
	claseSeleccionada=StringVar()

	frameNuevaPartida=Frame(root,width=1366,height=768)
	frameNuevaPartida.place(x=0,y=0)

	fondo=Label(frameNuevaPartida,image=fondoMenu)
	fondo.place(x=-5,y=-50)

	bt_SalirFrameNuevaPartida=Button(frameNuevaPartida,text="X",command=salirNuevaPartida).place(x=1350,y=0)
	
	Label(frameNuevaPartida,text="Personaje",font=("Calibri",30)).place(x=100,y=100)
	
	Label(frameNuevaPartida,text="nombre:",font=("Arial",12)).place(x=100,y=200)
	et_nombre=Entry(frameNuevaPartida,width=10,textvariable=nombre).place(x=180,y=200)

	Label(frameNuevaPartida,text="Elija una raza ([1] Humano, [2] Enano, [3] Elfo, [4] Orco)").place(x=100,y=350)
	et_raza=Entry(frameNuevaPartida,width=10,textvariable=razaSeleccionada).place(x=100,y=400)


	Label(frameNuevaPartida,text="Elija una clase (Guerrero,Mago,Picaro)").place(x=100,y=250)
	rb_Guerrero=Radiobutton(frameNuevaPartida,text="Guerrero",variable="claseSeleccionada",value="Guerrero",command=seleccionarGuerrero).place(x=100,y=280)
	rb_Mago=Radiobutton(frameNuevaPartida,text="Mago",variable="claseSeleccionada",value="Mago",command=seleccionarMago).place(x=180,y=280)
	rb_Picaro=Radiobutton(frameNuevaPartida,text="Picaro",variable="claseSeleccionada",value="Picaro",command=seleccionarPicaro).place(x=250,y=280)
	# et_clase=Entry(frameNuevaPartida,width=10,textvariable=clase).place(x=100,y=280)
	# bt_selec=Button(frameNuevaPartida,text="seleccionar",command=selecClass).place(x=230,y=280)

	frameEstadisticas=Frame(frameNuevaPartida,width=200,height=300)
	frameEstadisticas.place(x=100,y=500)

	global puntosDisponibles
	puntosDisponibles=5

	Label(frameEstadisticas,text=f"pts disponibles: {puntosDisponibles}").place(x=5,y=5)
	
	fuerza=StringVar()
	fuerza.set(0)
	aguante=StringVar()
	aguante.set(0)
	inteligencia=StringVar()
	inteligencia.set(0)
	magia=StringVar()
	magia.set(0)
	agilidad=StringVar()
	agilidad.set(0)
	percepcion=StringVar()
	percepcion.set(0)

	et_fuerza=Entry(frameEstadisticas,textvariable=fuerza,width=3,font=("Arial",15))
	et_fuerza.place(x=30,y=30)
	Label(frameEstadisticas,text="Fuerza",font=("Arial",15),fg="black").place(x=60,y=30)
	bt_SubirFuerza=Button(frameEstadisticas,text="+",command=subirFuerza).place(x=10,y=30)
	bt_BajarFuerza=Button(frameEstadisticas,text="-",command=bajarFuerza).place(x=0,y=30)

	et_aguante=Entry(frameEstadisticas,textvariable=aguante,width=3,font=("Arial",15))
	et_aguante.place(x=30,y=60)
	Label(frameEstadisticas,text="Aguante",font=("Arial",15),fg="black").place(x=60,y=60)
	bt_aguante=Button(frameEstadisticas,text="+",command=subirAguante).place(x=10,y=60)
	bt_BajarAguante=Button(frameEstadisticas,text="-",command=bajarAguante).place(x=0,y=60)

	et_inteligencia=Entry(frameEstadisticas,textvariable=inteligencia,width=3,font=("Arial",15))
	et_inteligencia.place(x=30,y=90)
	Label(frameEstadisticas,text="Inteligencia",font=("Arial",15),fg="black").place(x=60,y=90)
	bt_inteligencia=Button(frameEstadisticas,text="+",command=subirInteligencia).place(x=10,y=90)
	bt_BajarInteligencia=Button(frameEstadisticas,text="-",command=bajarInteligencia).place(x=0,y=90)

	et_Magia=Entry(frameEstadisticas,textvariable=magia,width=3,font=("Arial",15))
	et_Magia.place(x=30,y=120)
	Label(frameEstadisticas,text="magia",font=("Arial",15),fg="black").place(x=60,y=120)
	bt_magia=Button(frameEstadisticas,text="+",command=subirMagia).place(x=10,y=120)
	bt_BajarMagia=Button(frameEstadisticas,text="-",command=bajarMagia).place(x=0,y=120)

	et_agilidad=Entry(frameEstadisticas,textvariable=agilidad,width=3,font=("Arial",15))
	et_agilidad.place(x=30,y=150)
	Label(frameEstadisticas,text="Agilidad",font=("Arial",15),fg="black").place(x=60,y=150)
	bt_agilidad=Button(frameEstadisticas,text="+",command=subirAgilidad).place(x=10,y=150)
	bt_BajarAgilidad=Button(frameEstadisticas,text="-",command=bajarAgilidad).place(x=0,y=150)

	et_percepcion=Entry(frameEstadisticas,textvariable=percepcion,width=3,font=("Arial",15))
	et_percepcion.place(x=30,y=180)
	Label(frameEstadisticas,text="Percepcion",font=("Arial",15),fg="black").place(x=60,y=180)
	bt_percepcion=Button(frameEstadisticas,text="+",command=subirPercepcion).place(x=10,y=180)
	bt_BajarPercepcion=Button(frameEstadisticas,text="-",command=bajarPercepcion).place(x=0,y=180)


	bt_CrearPartida=Button(frameNuevaPartida,width=10,text="Crear Personaje",font=("Arial",15),command=crearPartida).place(x=500,y=100)
	

 # CREACION DEL FRAME DEL MENU

def salir():

	frameMenu.destroy()
	root.destroy()

frameMenu=Frame(root,width=1366,height=768,bg="red")
frameMenu.place(x=0,y=0)

fondoMenu=PhotoImage(file="assets/images/fondo.png")
fondo=Label(frameMenu,image=fondoMenu)
fondo.place(x=-5,y=-50)

bt_SalirMenu=Button(frameMenu,text="X",command=salir).place(x=1350,y=0)

bt_NuevaPartida=Button(frameMenu,text="Nueva Partida",font=("Arial",20),fg="black",border=0,bg="#EACB95",command=crearFrameNuevaPartida)
bt_NuevaPartida.place(x=600,y=400)

#____________________________________ VARIABLES GLOBALES______________________________

# SI SE AGREGA UN NUEVO MATERIAL, SE TIENE QUE AGREGAR A LA LISTA DE MATERIALES DEL PERSONAJE personaje.materiales={aqui}
materialesComunes=["Madera","Piedra","Cuero","Tela","Arcilla","Mineral de hierro","Mineral de oro","Hueso","Cristal"]
materialesRaros=["Hierro","Oro","Rubi","Zafiro","Esmeralda","Cuero refinado","Tela de calidad","Madera refinada","Piedra refinada","Ladrillo"]
materialesEpicos=["Alma","Polvo de estrellas","Diamante","Corazon de piedra","Escama de dragon","Flor de fuego","Runa"]

# _____________________________________________ IMAGENES ___________________________________________________

imagenOro=PhotoImage(file="assets/images/oro.png")
imagenCofre=PhotoImage(file="assets/images/cofre.png")
imagenCofreAbierto=PhotoImage(file="assets/images/cofreAbierto.png")
imagenCuadradoBlanco=PhotoImage(file="assets/images/noEmenRecom.png")

IMG_DADO1= PhotoImage(file="assets/images/dado1.png")
IMG_DADO2= PhotoImage(file="assets/images/dado2.png")
IMG_DADO3= PhotoImage(file="assets/images/dado3.png")
IMG_DADO4= PhotoImage(file="assets/images/dado4.png")
IMG_DADO5= PhotoImage(file="assets/images/dado5.png")
IMG_DADO6= PhotoImage(file="assets/images/dado6.png")

# iconos estadisticas
imagenCorazon = PhotoImage(file="assets/images/cora.png")
imagenEspada = PhotoImage(file="assets/images/espada.png")
imagenBarrera = PhotoImage(file="assets/images/barrera.png")
imagenArmadura = PhotoImage(file="assets/images/armadura.png")
imagenMana = PhotoImage(file="assets/images/mana.png")

# Estrellas
e0=PhotoImage(file="assets/images/noEstrellas.png")
e1=PhotoImage(file="assets/images/1s.png")
e2=PhotoImage(file="assets/images/2s.png")
e3=PhotoImage(file="assets/images/3s.png")

# Enemigos
enem2=PhotoImage(file="assets/images/esqueleto.png")


#_________________________________MAIN____________________________________

personaje=Personaje("Krigerson","humano","Guerrero",100,100,5,5,5,5,5,5)

mapa=Mapa()		 

partida=Partida(personaje, mapa)

# partida.comenzarPartida()

root.mainloop()

