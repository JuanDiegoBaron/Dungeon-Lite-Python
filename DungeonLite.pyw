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

# cris claro "#33373A"


# ---------------- Configuracion del frame principal -------------------

framePrincipal=Frame(root,width=1366,height=768,bg="#33373A").place(x="0",y="0")
frameMapa=Frame(framePrincipal,width=220,height=220,bg="yellow")
frameMapa.place(x=1135,y=200)

# ---------------- Widgets frame principal ------------------------

def salirApp():

	root.destroy()	

bt_Salir = Button(framePrincipal,text="X",fg="white",bg="#390606",bd="0",width="3",height="1",command=salirApp).place(x="1336",y="1")


# _____________________________________________ IMAGENES JUEGO DE MESA ___________________________________________________

# Otros
imagenOro=PhotoImage(file="imagenes/oro.png")
imagenCofre=PhotoImage(file="imagenes/cofre.png")
imagenCuadradoBlanco=PhotoImage(file="imagenes/noEmenRecom.png")
pj=PhotoImage(file="imagenes/pj.png")
mapa=PhotoImage(file="imagenes/mapaDungeonLite.png")
fondoMapa=PhotoImage(file="imagenes/fondoMapa.png")

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
# framePrincipal = Frame(framePrincipal,width="1366",height="758")
# framePrincipal.place(x=0,y=25)

def salir():
					
	framePrincipal.destroy()

def guardar_salir():    
				
	pass

# Funciones botones

def EDUA():
	pass
def mejorarObjeto():
	pass
def tirarDados():
	
	aux1=choice([1,2,3,4,5,6])

	valorDado1.set(aux1)

	if(aux1==1):
		Label(framePrincipal,image=img_dado1).place(x=890,y=360)
	elif(aux1==2):
		Label(framePrincipal,image=img_dado2).place(x=890,y=360)	
	elif(aux1==3):
		Label(framePrincipal,image=img_dado3).place(x=890,y=360)
	elif(aux1==4):
		Label(framePrincipal,image=img_dado4).place(x=890,y=360)
	elif(aux1==5):
		Label(framePrincipal,image=img_dado5).place(x=890,y=360)
	elif(aux1==6):
		Label(framePrincipal,image=img_dado6).place(x=890,y=360)

	aux2=choice([1,2,3,4,5,6])

	valorDado2.set(aux2)

	if(aux2==1):
		Label(framePrincipal,image=img_dado1).place(x=950,y=360)
	elif(aux2==2):
		Label(framePrincipal,image=img_dado2).place(x=950,y=360)	
	elif(aux2==3):
		Label(framePrincipal,image=img_dado3).place(x=950,y=360)
	elif(aux2==4):
		Label(framePrincipal,image=img_dado4).place(x=950,y=360)
	elif(aux2==5):
		Label(framePrincipal,image=img_dado5).place(x=950,y=360)
	elif(aux2==6):
		Label(framePrincipal,image=img_dado6).place(x=950,y=360)

	suma=int(valorDado1.get())+int(valorDado2.get())
	celdasDisponibles.set(suma)		

def moverArriba():

	if(celdasDisponibles.get()=="" or int(celdasDisponibles.get())<1):
		return
	else:
		total=int(celdasDisponibles.get())-1
		celdasDisponibles.set(total)
		total=int(celda.get())+1
		celda.set(total)
	
	x=int(mapa_x.get())
	y=int(mapa_y.get())
	if(y>80):
		return
	else:	
		print(y)
		y=y+20
		print(y)
		mapa_y.set(y)
		Label(frameMapa,image=fondoMapa).place(x=0,y=0)
		Label(frameMapa,image=mapa).place(x=x,y=y)
		Label(frameMapa,image=pj).place(x=100,y=100)
def moverAbajo():

	if(celdasDisponibles.get()=="" or int(celdasDisponibles.get())<1):
		return
	else:
		total=int(celdasDisponibles.get())-1
		celdasDisponibles.set(total)

	x=int(mapa_x.get())
	y=int(mapa_y.get())
	if(y<-1060):
		return
	else:
		print(y)
		y=y-20
		print(y)
		mapa_y.set(y)
		Label(frameMapa,image=fondoMapa).place(x=0,y=0)
		Label(frameMapa,image=mapa).place(x=x,y=y)
		Label(frameMapa,image=pj).place(x=100,y=100)
def moverDerecha():

	if(celdasDisponibles.get()=="" or int(celdasDisponibles.get())<1):
		return
	else:
		total=int(celdasDisponibles.get())-1
		celdasDisponibles.set(total)

	x=int(mapa_x.get())
	y=int(mapa_y.get())
	if(x<-1060):
		return
	else:
		
		print(x)
		x=x-20
		print(x)
		mapa_x.set(x)
		Label(frameMapa,image=fondoMapa).place(x=0,y=0)
		Label(frameMapa,image=mapa).place(x=x,y=y)
		Label(frameMapa,image=pj).place(x=100,y=100)
def moverIzquierda():

	if(celdasDisponibles.get()=="" or int(celdasDisponibles.get())<1):
		return
	else:
		total=int(celdasDisponibles.get())-1
		celdasDisponibles.set(total)

	x=int(mapa_x.get())
	y=int(mapa_y.get())
	if(x>80):
		return
	else:
		print(x)
		x=x+20
		print(x)
		mapa_x.set(x)
		Label(frameMapa,image=fondoMapa).place(x=0,y=0)
		Label(frameMapa,image=mapa).place(x=x,y=y)
		Label(frameMapa,image=pj).place(x=100,y=100)
def accion():
	pass				
def preBatalla():
	pass
def abrirCofre():
	pass	
def huir():
	pass	



# VARIABLES DE LOS ENTRY ----------

precaucion=StringVar()
precaucionRecom=StringVar()

objetoEDUA=StringVar()
infoObjeto=StringVar()

dañoEnemigo=StringVar()
vidaEnemigo=StringVar()
nombreEnemigo=StringVar()
nivelEnemigo=StringVar()
expEnemigo=StringVar()

valorDado1=StringVar()
valorDado1.set(0)
valorDado2=StringVar()
valorDado2.set(0)

mapa_x=StringVar()
mapa_y=StringVar()
mapa_x.set(0)
mapa_y.set(0)

celdasDisponibles=StringVar()

obj1=StringVar()
obj2=StringVar()
obj3=StringVar()

inventario = []
indice = []          

exp=StringVar()
exp.set(0)
nivel=StringVar()
nivel.set(1)

celda=StringVar()
celda.set(0)	
turno=StringVar()
turno.set(0)

vida=StringVar()
vida.set(100)
barrera=StringVar()
barrera.set(0)
armadura=StringVar()
armadura.set(0)

daño=StringVar()
daño.set(2)	
suerte=StringVar()
suerte.set(0)
mana=StringVar()
mana.set(100)

oro=StringVar()
oro.set(0)

# Mapa
Mapa=Label(frameMapa,image=mapa).place(x=0,y=0)
Label(frameMapa,image=pj).place(x=100,y=100)

et_mapaX=Entry(framePrincipal,textvariable=mapa_x,font=("Arial",10),state="readonly",width=6,justify="center").place(x=1150,y=430)
et_mapaY=Entry(framePrincipal,textvariable=mapa_y,font=("Arial",10),state="readonly",width=6,justify="center").place(x=1300,y=430)
Label(text="x",bg="grey",font=("Arial",12),fg="white").place(x=1200,y=430)
Label(text="y",bg="grey",font=("Arial",12),fg="white").place(x=1280,y=430)


bt_accion=Button(framePrincipal,text="X",width=5,command=accion).place(x=1225,y=465)

bt_moverArriba=Button(framePrincipal,width=5,text="⇧",command=moverArriba).place(x=1225,y=430)
bt_moverAbajo=Button(framePrincipal,width=5,text="⇩",command=moverAbajo).place(x=1225,y=500)
bt_moverDerecha=Button(framePrincipal,width=5,text="⇨",command=moverDerecha).place(x=1285,y=465)
bt_moverIzquierda=Button(framePrincipal,width=5,text="⇦",command=moverIzquierda).place(x=1165,y=465)


# BOTONES SALIR JUEGO
bt_salir=Button(framePrincipal,text="Salir",bg="#390606",width=20,height=1,bd=0,fg="white",command=salir).place(x=1200,y=700)
bt_guardar_salir=Button(framePrincipal,text="Guardar y Salir",bg="#390606",width=20,height=1,bd=0,fg="white",command=guardar_salir).place(x=1050,y=700)

# WIDGETS del juego

# nivel
Label(framePrincipal,text="Nivel",font=("Arial",15),bg="#33373A",fg="white",bd=0).place(x=840,y=15)
et_nivel=Entry(framePrincipal,textvariable=nivel,width=5,justify="center",state="readonly",font=("Arial",15),bd=0).place(x=900,y=15)
# oro
Label(framePrincipal,image=imagenOro,bg="#33373A").place(x=700,y=10)
et_oro=Entry(framePrincipal,textvariable=oro,width=6,state="readonly",font=("Arial",15),bd=0).place(x=740,y=15)
# exp
Label(framePrincipal,text="XP",font=("Arial",15),bg="#33373A",bd=0,fg="white").place(x=1060,y=15)
et_exp=Entry(framePrincipal,textvariable=exp,width=5,font=("Arial",15),bd=0,justify="center",state="readonly").place(x=1000,y=15)
# celda
Label(framePrincipal,text="Celdas",font=("Arial",15),bg="#33373A",bd=0,fg="white").place(x=1230,y=15)
et_celda=Entry(framePrincipal,textvariable=celda,width=5,justify="center",state="readonly",font=("Arial",15),bd=0).place(x=1290,y=15)
# turno
Label(framePrincipal,text="Turno",font=("Arial",15),bg="#33373A",bd=0,fg="white").place(x=1110,y=15)
et_turno=Entry(framePrincipal,textvariable=turno,width=3,justify="center",state="readonly",font=("Arial",15),bd=0)
et_turno.place(x=1170,y=15)
# Columna 1

Label(framePrincipal,image=imagenCorazon,bg="#33373A").place(x=0,y=10)
et_vida=Entry(framePrincipal,textvariable=vida,width=4,justify="center",state="readonly",font=("Arial",15),bd=0).place(x=80,y=20)
								
Label(framePrincipal,image=imagenBarrera,bg="#33373A").place(x=18,y=70)
et_barrera=Entry(framePrincipal,textvariable=barrera,width=4,justify="center",state="readonly",font=("Arial",15),bd=0).place(x=80,y=80)

Label(framePrincipal,image=imagenArmadura,bg="#33373A").place(x=23,y=130)
et_armadura=Entry(framePrincipal,textvariable=armadura,width=4,justify="center",state="readonly",font=("Arial",15),bd=0).place(x=80,y=140)
# Columna 2

Label(framePrincipal,image=imagenEspada,bg="#33373A").place(x=160,y=10)
et_daño=Entry(framePrincipal,textvariable=daño,width=4,justify="center",state="readonly",font=("Arial",15),bd=0).place(x=220,y=20)

Label(framePrincipal,image=imagenMana,bg="#33373A").place(x=150,y=60)
et_mana=Entry(framePrincipal,textvariable=mana,width=4,justify="center",state="readonly",font=("Arial",15),bd=0).place(x=220,y=80)

Label(framePrincipal,image=imagenSuerte,bg="#33373A").place(x=150,y=125)
et_suerte=Entry(framePrincipal,textvariable=suerte,width=4,justify="center",state="readonly",font=("Arial",15),bd=0).place(x=220,y=140)

# IMAGENES DE LAS PARTES DEL EQUIPAMIENTO
# Label(framePrincipal,image=imagenCabeza).place(x=20,y=200)
# Label(framePrincipal,image=imagenPecho).place(x=20,y=260)
# Label(framePrincipal,image=imagenPiernas).place(x=20,y=320)
# Label(framePrincipal,image=imagenPies).place(x=20,y=380)
# Label(framePrincipal,image=imagenArma).place(x=20,y=440)

txt_Inventario = Text(framePrincipal,width=30,height=20,bd=0,bg="#961010",fg="white")
txt_Inventario.place(x=20,y=200)

# entry Equipar/Desequipar/Usar/Activar
et_edua = Entry(framePrincipal,textvariable=objetoEDUA,width=3,justify="center",font=("Arial",15),bd=0)
et_edua.place(x=20,y=535)
bt_edua = Button(framePrincipal,text="Equip/Deseq/Usar/Activar",bg="#390606",width=25,command=EDUA,height=1,bd=0,fg="white")
bt_edua.place(x=80,y=535)

# Consola
txt_Consola = Text(framePrincipal,width=60,height=20,bd=0,bg="#961010",fg="white")
txt_Consola.place(x=280,y=200)


et_celdasDisponibles=Entry(framePrincipal,state="readonly",justify="center",textvariable=celdasDisponibles,font=("Arial",30),width=2).place(x=1065,y=360)

# Ver objeto
# txt_info_obj =Text(framePrincipal,width=30,height=7,bd=0,bg="#961010",fg="white",)
# txt_info_obj.place(x=110,y=570)
# et_obj_mirar = Entry(framePrincipal,textvariable=infoObjeto,width=3,justify="center",font=("Arial",15),bd=0).place(x=110,y=700)
# bt_Info =Button(framePrincipal,text="Info",bg="#390606",width=25,height=1,bd=0,fg="white").place(x=170,y=703)
	
# Mejorar objetos
et_obj1 = Entry(framePrincipal,textvariable=obj1,width=3,justify="center",font=("Arial",15),bd=0).place(x=20,y=600)
et_obj2 = Entry(framePrincipal,textvariable=obj2,width=3,justify="center",font=("Arial",15),bd=0).place(x=20,y=650)
et_obj3 = Entry(framePrincipal,textvariable=obj3,width=3,justify="center",font=("Arial",15),bd=0).place(x=20,y=700)
bt_mejorar = Button(framePrincipal,text="->",bg="#390606",width=2,height=8,bd=0,fg="white",command=mejorarObjeto).place(x=70,y=600)
Label(framePrincipal,text="Mejorar Objeto",font=("Arial",12),fg="white").place(x=100,y=575)
et_nombreObj = Entry(framePrincipal,width=20,state="readonly",font=("Arial",15),bd=0).place(x=100,y=600)
txt_info_obj_mejorado = Text(framePrincipal,width=28,height=5,fg="white")
txt_info_obj_mejorado.place(x=100,y=630)

# Tirar dados
bt_TirarDados = Button(framePrincipal,text="Tirar dados",bg="#390606",width=10,height=2,bd=0,font=("Arial",15),fg="white",command=tirarDados).place(x=770,y=355)

et_dado1=Entry(framePrincipal,textvariable=valorDado1,width=3,font=("Arial",15),state="readonly",justify="center").place(x=1015,y=355)
et_dado2=Entry(framePrincipal,textvariable=valorDado2,width=3,font=("Arial",15),state="readonly",justify="center").place(x=1015,y=390)

# Enemigos
Frame(framePrincipal,width=600,height=140,bg="red").place(x=770,y=60)

Label(framePrincipal,text="Enemigo:",bg="red",font=("Arial",12),fg="white").place(x=910,y=80)
et_enemigo = Entry(framePrincipal,textvariable=nombreEnemigo,state="readonly",width=15,font=("Arial",15),bd=0).place(x=990,y=80)
Label(framePrincipal,text="Daño: ",bg="red",font=("Arial",12),fg="white").place(x=910,y=110)
et_dañoEnemigo = Entry(framePrincipal,textvariable=dañoEnemigo,state="readonly",width=3,justify="center",font=("Arial",15),bd=0).place(x=970,y=110)
Label(framePrincipal,text="Vida: ",bg="red",font=("Arial",12),fg="white").place(x=1020,y=110)
et_vidaEnemigo = Entry(framePrincipal,textvariable=vidaEnemigo,state="readonly",width=3,justify="center",font=("Arial",15),bd=0).place(x=1075,y=110)
Label(framePrincipal,text="Nivel: ",bg="red",font=("Arial",12),fg="white").place(x=1120,y=110)
et_nivelEnemigo= Entry(framePrincipal,textvariable=nivelEnemigo,state="readonly",width=3,justify="center",font=("Arial",15),bd=0).place(x=1170,y=110)
bt_luchar=Button(framePrincipal,text="Luchar",bg="#961010",width=20,height=1,bd=0,font=("Arial",15),fg="white",command=preBatalla).place(x=910,y=150)
bt_huir=Button(framePrincipal,text="Huir",bg="#961010",width=10,height=1,bd=0,font=("Arial",15),fg="white",command=huir).place(x=1145,y=150)
et_precau_enem = Entry(framePrincipal,textvariable=precaucion,state="readonly",width=3,justify="center",bg="#390606",font=("Arial",15),bd=0).place(x=1220,y=110)
Label(framePrincipal,text="Exp:",bg="red",font=("Arial",12),fg="white").place(x=1170,y=80)
et_expEnemigo = Entry(framePrincipal,textvariable=expEnemigo,state="readonly",width=4,bg="#ffffff",font=("Arial",15),bd=0).place(x=1210,y=80)

Label(framePrincipal,image=enem2).place(x=785,y=80)

nl_enemigo = Label(framePrincipal,image=e3).place(x=880,y=80)

# Cofres / Recompenzas

Frame(framePrincipal,width=350,height=150,bg="green").place(x=770,y=200)

Label(framePrincipal,image=imagenCofre).place(x=785,y=210)
nl_cofre = Label(framePrincipal,image=e3).place(x=880,y=210)
bt_abrir_cofre = Button(framePrincipal,text="Abrir",bg="#40E74F",width=16,height=1,bd=0,fg="white",command=abrirCofre).place(x=785,y=315)
et_precau_reco = Entry(framePrincipal,textvariable=precaucionRecom,state="readonly",width=3,justify="center",bg="#390606",font=("Arial",15),bd=0).place(x=770,y=455)

txt_recompenza = Text(framePrincipal,width=24,height=8)
txt_recompenza.place(x=915,y=210)

root.mainloop()