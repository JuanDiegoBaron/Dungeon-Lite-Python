from tkinter import *
from .ventana import Ventana

class CreacionPersonaje(Ventana):

	def __init__(self,interfaz,padre,nombre):

		super().__init__(interfaz,padre, nombre)

	# IMAGENES

		# CLASES

		self.img_Guerrero=PhotoImage(file="assets/images/clases/guerrero.png")
		self.img_Mago=PhotoImage(file="assets/images/clases/mago.png")
		self.img_Picaro=PhotoImage(file="assets/images/clases/picaro.png")

		# RAZAS
		self.img_Humano=PhotoImage(file="assets/images/razas/Humano.png")
		self.img_Humana=PhotoImage(file="assets/images/razas/Humana.png")
		self.img_Enano=PhotoImage(file="assets/images/razas/Enano.png")
		self.img_Enana=PhotoImage(file="assets/images/razas/Enana.png")
		self.img_Orco=PhotoImage(file="assets/images/razas/Orco.png")
		self.img_Orca=PhotoImage(file="assets/images/razas/Orca.png")
		self.img_Elfo=PhotoImage(file="assets/images/razas/Elfo.png")
		self.img_Elfa=PhotoImage(file="assets/images/razas/Elfa.png")
		self.img_HumanoMini=PhotoImage(file="assets/images/razas/miniaturas/miniaturaHumano.png")
		self.img_HumanaMini=PhotoImage(file="assets/images/razas/miniaturas/miniaturaHumana.png")
		self.img_EnanoMini=PhotoImage(file="assets/images/razas/miniaturas/miniaturaEnano.png")
		self.img_EnanaMini=PhotoImage(file="assets/images/razas/miniaturas/miniaturaEnana.png")
		self.img_OrcoMini=PhotoImage(file="assets/images/razas/miniaturas/miniaturaOrco.png")
		self.img_OrcaMini=PhotoImage(file="assets/images/razas/miniaturas/miniaturaOrca.png")
		self.img_ElfoMini=PhotoImage(file="assets/images/razas/miniaturas/miniaturaElfo.png")
		self.img_ElfaMini=PhotoImage(file="assets/images/razas/miniaturas/miniaturaElfa.png")

		# FONDO
		self.img_fondo=PhotoImage(file="assets/images/fondo.png")
		self.fondo=Label(self.frame,image=self.img_fondo)
		self.fondo.place(x=-5,y=-50)

	# IMAGEN CLASE

		self.retratoClase=Label(self.frame,image=self.img_Guerrero)
		self.retratoClase.place(x=350,y=0)

	# IMAGEN PERSONAJE
		self.retratoPersonaje=Label(self.frame,image=self.img_Humano)
		self.retratoPersonaje.place(x=950,y=50)

		self.retratoMiniatura=self.img_HumanoMini

	# BOTON VOLVER MENU

		self.bt_volverMenu=Button(self.frame,text="←",font=("Arial",15),command=self.volverMenu)
		self.bt_volverMenu.place(x=0,y=0)

	# BOTON COMENZAR PARTIDA

		self.bt_comenzarPartida= Button(self.frame,width=21,text="Empezar",font=("Arial",20),command=self.comenzarPartida)
		self.bt_comenzarPartida.place(x=950,y=680)

	# SEXO

		self.genero=StringVar()
		self.genero.set("Hombre")

		Label(self.frame,text="Genero:",font=("Arial",15)).place(x=100,y=10)
		self.et_genero=Entry(self.frame,textvariable=self.genero,font=("Arial",15),width=8,justify="center")
		self.et_genero.place(x=100,y=50)
		self.bt_cambiarGenero=Button(self.frame,text="o",font=("Arial",10),command=self.cambiarGenero)
		self.bt_cambiarGenero.place(x=195,y=50)

	# NOMBRE PERSONAJE
		self.nombrePersonaje=StringVar()

		Label(self.frame,text="Nombre del personaje: ",font=("Arial",15),border=1).place(x=100,y=100)
		self.et_nombrePersonaje=Entry(self.frame,width=19,textvariable=self.nombrePersonaje,font=("Arial",15),justify="center")
		self.et_nombrePersonaje.place(x=100,y=130)

	# RAZA
		self.indiceRaza=0
		self.listaRazas=["Humano","Enano","Orco","Elfo"]
		self.razaPersonaje=StringVar()
		self.razaPersonaje.set(self.listaRazas[self.indiceRaza])

		Label(self.frame,text="Raza del personaje:",font=("Arial",15),border=1).place(x=100,y=200)

		self.bt_cambiarRazaI=Button(self.frame,text="<",command=lambda:self.cambiarRaza("I"))
		self.bt_cambiarRazaI.place(x=100,y=240)

		self.et_razaPersonaje=Entry(self.frame,width=17,textvariable=self.razaPersonaje,font=("Aril",12),justify="center")
		self.et_razaPersonaje.place(x=120,y=240)

		self.bt_cambiarRazaD=Button(self.frame,text=">",command=lambda:self.cambiarRaza("D"))
		self.bt_cambiarRazaD.place(x=280,y=240)

	# Clase
		self.indiceClase=0
		self.listaClases=["Guerrero","Mago","Picaro"]
		self.clasePersonaje=StringVar()
		self.clasePersonaje.set(self.listaClases[self.indiceClase])

		Label(self.frame,text="Clase del personaje:",font=("Arial",15),border=1).place(x=100,y=300)

		self.bt_cambiarClaseI=Button(self.frame,text="<",command=lambda:self.cambiarClase("I"))
		self.bt_cambiarClaseI.place(x=100,y=340)

		self.et_ClasePersonaje=Entry(self.frame,width=17,textvariable=self.clasePersonaje,font=("Aril",12),justify="center")
		self.et_ClasePersonaje.place(x=120,y=340)

		self.bt_cambiarClaseD=Button(self.frame,text=">",command=lambda:self.cambiarClase("D"))
		self.bt_cambiarClaseD.place(x=280,y=340)

	# Estadisticas

		self.puntosDisponibles=StringVar()
		self.puntosDisponibles.set(10)

		self.fuerza=StringVar()
		self.fuerza.set(0)

		self.aguante=StringVar()
		self.aguante.set(0)

		self.agilidad=StringVar()
		self.agilidad.set(0)

		self.inteligencia=StringVar()
		self.inteligencia.set(0)

		self.magia=StringVar()
		self.magia.set(0)

		self.persepcion=StringVar()
		self.persepcion.set(0)

		Label(self.frame,text="Atributos:",font=("Arial",15),border=1).place(x=100,y=400)
		et_puntos=Entry(self.frame,width=2,textvariable=self.puntosDisponibles,font=("Arial",15),justify="center").place(x=200,y=400)

	# fuerza
		self.bt_bajarfuerza=Button(self.frame,text="<",command=lambda:self.modificarAtributo("bajar","fuerza"))
		self.bt_bajarfuerza.place(x=100,y=440)

		self.et_fuerza=Entry(self.frame,width=3,textvariable=self.fuerza,font=("Aril",12),justify="center")
		self.et_fuerza.place(x=120,y=440)

		self.bt_subirfuerza=Button(self.frame,text=">",command=lambda:self.modificarAtributo("subir","fuerza"))
		self.bt_subirfuerza.place(x=155,y=440)

		Label(self.frame,text="Fuerza").place(x=180,y=440)

	# aguante
		self.bt_bajaraguante=Button(self.frame,text="<",command=lambda:self.modificarAtributo("bajar","aguante"))
		self.bt_bajaraguante.place(x=100,y=480)

		self.et_aguante=Entry(self.frame,width=3,textvariable=self.aguante,font=("Aril",12),justify="center")
		self.et_aguante.place(x=120,y=480)

		self.bt_subiraguante=Button(self.frame,text=">",command=lambda:self.modificarAtributo("subir","aguante"))
		self.bt_subiraguante.place(x=155,y=480)

		Label(self.frame,text="Aguante").place(x=180,y=480)

	# agilidad
		self.bt_bajaragilidad=Button(self.frame,text="<",command=lambda:self.modificarAtributo("bajar","agilidad"))
		self.bt_bajaragilidad.place(x=100,y=520)

		self.et_agilidad=Entry(self.frame,width=3,textvariable=self.agilidad,font=("Aril",12),justify="center")
		self.et_agilidad.place(x=120,y=520)

		self.bt_subiragilidad=Button(self.frame,text=">",command=lambda:self.modificarAtributo("subir","agilidad"))
		self.bt_subiragilidad.place(x=155,y=520)

		Label(self.frame,text="Agilidad").place(x=180,y=520)

	# inteligencia
		self.bt_bajarinteligencia=Button(self.frame,text="<",command=lambda:self.modificarAtributo("bajar","inteligencia"))
		self.bt_bajarinteligencia.place(x=100,y=560)

		self.et_inteligencia=Entry(self.frame,width=3,textvariable=self.inteligencia,font=("Aril",12),justify="center")
		self.et_inteligencia.place(x=120,y=560)

		self.bt_subir=Button(self.frame,text=">",command=lambda:self.modificarAtributo("subir","inteligencia"))
		self.bt_subir.place(x=155,y=560)

		Label(self.frame,text="Inteligencia").place(x=180,y=560)

	# magia
		self.bt_bajarmagia=Button(self.frame,text="<",command=lambda:self.modificarAtributo("bajar","magia"))
		self.bt_bajarmagia.place(x=100,y=600)

		self.et_magia=Entry(self.frame,width=3,textvariable=self.magia,font=("Aril",12),justify="center")
		self.et_magia.place(x=120,y=600)

		self.bt_subirmagia=Button(self.frame,text=">",command=lambda:self.modificarAtributo("subir","magia"))
		self.bt_subirmagia.place(x=155,y=600)

		Label(self.frame,text="Magia").place(x=180,y=600)
		
	# persepcion
		self.bt_bajarpersepcion=Button(self.frame,text="<",command=lambda:self.modificarAtributo("bajar","persepcion"))
		self.bt_bajarpersepcion.place(x=100,y=640)

		self.et_persepcion=Entry(self.frame,width=3,textvariable=self.persepcion,font=("Aril",12),justify="center")
		self.et_persepcion.place(x=120,y=640)

		self.bt_subirpersepcion=Button(self.frame,text=">",command=lambda:self.modificarAtributo("subir","persepcion"))
		self.bt_subirpersepcion.place(x=155,y=640)	

		Label(self.frame,text="Persepcion").place(x=180,y=640)				

	def recibirInformacion(self,informacion):
		pass

	def comenzarPartida(self):

		vida=int(self.aguante.get())*5+100
		# print(vida)
		mana=int(self.magia.get())*5+100
		# print(mana)

		datosPersonaje = {
			"Mensaje":"Datos Personaje",
			"Genero": self.genero.get(),
			"Nombre":self.nombrePersonaje.get(),
			"Raza":self.razaPersonaje.get(),
			"Clase":self.clasePersonaje.get(),
			"Vida":vida,
			"Mana":mana,
			"Fuerza":int(self.fuerza.get()),
			"Aguante":int(self.aguante.get()),
			"Agilidad":int(self.agilidad.get()),
			"Inteligencia":int(self.inteligencia.get()),
			"Magia":int(self.magia.get()),
			"Persepcion":int(self.persepcion.get())
		}

		# print(datosPersonaje)

		self.interfaz.enviarInformacion("Partida",datosPersonaje)

	def cambiarGenero(self):

		if self.genero.get() == "Hombre":

			self.genero.set("Mujer")

		else:
		
			self.genero.set("Hombre")

		self.cambiarRetrato()	

	def cambiarRetrato(self):

		if(self.genero.get() == "Hombre"):

			if(self.razaPersonaje.get() == "Humano"):

				self.retratoPersonaje.config(image=self.img_Humano)
				self.retratoMiniatura = self.img_HumanoMini

			elif(self.razaPersonaje.get() == "Orco"):
				
				self.retratoPersonaje.config(image=self.img_Orco)
				self.retratoMiniatura = self.img_OrcoMini

			elif(self.razaPersonaje.get() == "Enano"):
				
				self.retratoPersonaje.config(image=self.img_Enano)
				self.retratoMiniatura = self.img_EnanoMini

			elif(self.razaPersonaje.get() == "Elfo"):
				
				self.retratoPersonaje.config(image=self.img_Elfo)
				self.retratoMiniatura = self.img_ElfoMini

		elif(self.genero.get() == "Mujer"):

			if(self.razaPersonaje.get() == "Humano"):

				self.retratoPersonaje.config(image=self.img_Humana)
				self.retratoMiniatura = self.img_HumanaMini

			elif(self.razaPersonaje.get() == "Orco"):
				
				self.retratoPersonaje.config(image=self.img_Orca)
				self.retratoMiniatura = self.img_OrcaMini

			elif(self.razaPersonaje.get() == "Enano"):
				
				self.retratoPersonaje.config(image=self.img_Enana)
				self.retratoMiniatura = self.img_EnanaMini

			elif(self.razaPersonaje.get() == "Elfo"):
				
				self.retratoPersonaje.config(image=self.img_Elfa)
				self.retratoMiniatura = self.img_ElfaMini

	def modificarAtributo(self,mod,atributo):

		if(self.puntosDisponibles.get()=="0" and mod == "subir" or self.puntosDisponibles.get()=="10" and mod == "bajar"):

			return

		# Verificar que los atributos no bajen de 0
		if(atributo == "fuerza" and int(self.fuerza.get()) == 0 and mod == "bajar"):

			return

		elif(atributo == "aguante" and int(self.aguante.get()) == 0 and mod == "bajar"):
		
			return	

		elif(atributo == "agilidad" and int(self.agilidad.get()) == 0 and mod == "bajar"):
		
			return

		elif(atributo == "inteligencia" and int(self.inteligencia.get()) == 0 and mod == "bajar"):
		
			return
			
		elif(atributo == "magia" and int(self.magia.get()) == 0 and mod == "bajar"):
		
			return

		elif(atributo == "persepcion" and int(self.persepcion.get()) == 0 and mod == "bajar"):
		
			return				

		# Modificacion
		if atributo == "fuerza":

			if mod == "subir":

				self.fuerza.set(int(self.fuerza.get())+1)
				self.puntosDisponibles.set(int(self.puntosDisponibles.get())-1)

			elif mod == "bajar":
			
				self.fuerza.set(int(self.fuerza.get())-1)
				self.puntosDisponibles.set(int(self.puntosDisponibles.get())+1)

		if atributo == "aguante":

			if mod == "subir":

				self.aguante.set(int(self.aguante.get())+1)
				self.puntosDisponibles.set(int(self.puntosDisponibles.get())-1)

			elif mod == "bajar":
			
				self.aguante.set(int(self.aguante.get())-1)
				self.puntosDisponibles.set(int(self.puntosDisponibles.get())+1)
				
		if atributo == "agilidad":

			if mod == "subir":

				self.agilidad.set(int(self.agilidad.get())+1)
				self.puntosDisponibles.set(int(self.puntosDisponibles.get())-1)

			elif mod == "bajar":
			
				self.agilidad.set(int(self.agilidad.get())-1)
				self.puntosDisponibles.set(int(self.puntosDisponibles.get())+1)
		
		if atributo == "inteligencia":

			if mod == "subir":

				self.inteligencia.set(int(self.inteligencia.get())+1)
				self.puntosDisponibles.set(int(self.puntosDisponibles.get())-1)

			elif mod == "bajar":
			
				self.inteligencia.set(int(self.inteligencia.get())-1)
				self.puntosDisponibles.set(int(self.puntosDisponibles.get())+1)

		if atributo == "magia":

			if mod == "subir":

				self.magia.set(int(self.magia.get())+1)
				self.puntosDisponibles.set(int(self.puntosDisponibles.get())-1)

			elif mod == "bajar":
			
				self.magia.set(int(self.magia.get())-1)
				self.puntosDisponibles.set(int(self.puntosDisponibles.get())+1)
				
		if atributo == "persepcion":

			if mod == "subir":

				self.persepcion.set(int(self.persepcion.get())+1)
				self.puntosDisponibles.set(int(self.puntosDisponibles.get())-1)

			elif mod == "bajar":
			
				self.persepcion.set(int(self.persepcion.get())-1)
				self.puntosDisponibles.set(int(self.puntosDisponibles.get())+1)										

	def cambiarClase(self,direccion):

		if direccion=="D" and self.indiceClase==len(self.listaClases)-1:

			self.indiceClase=0
			self.clasePersonaje.set(self.listaClases[self.indiceClase])

		elif direccion=="I" and self.indiceClase==0:

			self.indiceClase=len(self.listaClases)-1
			self.clasePersonaje.set(self.listaClases[self.indiceClase])

		elif direccion=="D":

			self.indiceClase+=1

			self.clasePersonaje.set(self.listaClases[self.indiceClase])

		elif direccion=="I":
		
			self.indiceClase-=1	
			self.clasePersonaje.set(self.listaClases[self.indiceClase])

		if self.clasePersonaje.get()=="Guerrero":
		
			self.retratoClase.config(image=self.img_Guerrero)

		elif self.clasePersonaje.get()=="Mago":
		
			self.retratoClase.config(image=self.img_Mago)

		elif self.clasePersonaje.get()=="Picaro":
		
			self.retratoClase.config(image=self.img_Picaro)			

	def cambiarRaza(self,direccion):

		# print(self.indiceRaza)
		# print(len(self.listaRazas)-1)

		if direccion=="D" and self.indiceRaza==len(self.listaRazas)-1:

			self.indiceRaza=0
			self.razaPersonaje.set(self.listaRazas[self.indiceRaza])

		elif direccion=="I" and self.indiceRaza==0:

			self.indiceRaza=len(self.listaRazas)-1
			self.razaPersonaje.set(self.listaRazas[self.indiceRaza])

		elif direccion=="D":

			self.indiceRaza+=1

			self.razaPersonaje.set(self.listaRazas[self.indiceRaza])

		elif direccion=="I":
		
			self.indiceRaza-=1	
			self.razaPersonaje.set(self.listaRazas[self.indiceRaza])

		self.cambiarRetrato()		

	def resetearEntrys(self):

		self.fuerza.set(0)
		self.aguante.set(0)
		self.agilidad.set(0)
		self.inteligencia.set(0)
		self.magia.set(0)
		self.persepcion.set(0)

		self.puntosDisponibles.set(10)
		self.nombrePersonaje.set("")

	def volverMenu(self):
	
		self.resetearEntrys()
		self.interfaz.cambiarVentana("Menu Principal")