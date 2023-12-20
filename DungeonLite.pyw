from tkinter import *

# Libreria para crear y manipular archivos externos .txt
from io import open

# La libreria abc permite crear clases y methodos abstractos
from abc import ABC, abstractmethod

from random import choice, choices, randint

# Libreria para la base de datos
from sqlite3 import *

# Libreria para manipular imagenes
from PIL import Image, ImageTk


# modulos
from gui.interfaz import Interfaz

# ULTIMA TAREA, YA ERREGLE EL PROBLEMA DE LOS MODULOS
# AHORA TENGO QUE ARREGLAR LA CLASE PARTIDA PARA QUE MUESTRE EL JUEGO

""" TAREAS
	- VER QUE PUEDO MODULARIZAR EN LA CLASE PARTIDA
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
	
	* clase tiempo: maneje las horas, los dias ,etc . ¿ que tambien controle el clima?

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

# ____________________________________ ROOT ___________________________________________

root = Tk()  # Creacion de la pantalla 
root.attributes("-fullscreen",True)
root.title("DUNGEON LITE") # Establece un titulo a la ventana
root.resizable(0,0) # Permite agrandar/redimencionar la pantalla 
root.config(bg="Black")

#____________________________________ VARIABLES GLOBALES______________________________

# SI SE AGREGA UN NUEVO MATERIAL, SE TIENE QUE AGREGAR A LA LISTA DE MATERIALES DEL PERSONAJE personaje.materiales={aqui}
materialesComunes=["Madera","Piedra","Cuero","Tela","Arcilla","Mineral de hierro","Mineral de oro","Hueso","Cristal"]
materialesRaros=["Hierro","Oro","Rubi","Zafiro","Esmeralda","Cuero refinado","Tela de calidad","Madera refinada","Piedra refinada","Ladrillo"]
materialesEpicos=["Alma","Polvo de estrellas","Diamante","Corazon de piedra","Escama de dragon","Flor de fuego","Runa"]

#_________________________________MAIN____________________________________

# personaje=Personaje("Krigerson","humano","Guerrero",100,100,5,5,5,5,5,5)

# mapa=Mapa()		

# partida=Partida(personaje, mapa)

# partida.comenzarPartida()


interfaz = Interfaz(root)

# interfaz.mostrarVentana("Menu Principal")
# interfaz.ocultarVentana("Menu Principal")

interfaz.root.mainloop()

