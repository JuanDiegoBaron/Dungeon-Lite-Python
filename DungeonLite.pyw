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
frame_JuegoDeMesa = Frame(framePrincipal,width="1366",height="758",bg="#5F0A0A")
frame_JuegoDeMesa.place(x=0,y=25)

def salir():
					
	frame_JuegoDeMesa.destroy()

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
		Label(framePrincipal,image=img_dado1).place(x=890,y=380)
	elif(aux1==2):
		Label(framePrincipal,image=img_dado2).place(x=890,y=380)	
	elif(aux1==3):
		Label(framePrincipal,image=img_dado3).place(x=890,y=380)
	elif(aux1==4):
		Label(framePrincipal,image=img_dado4).place(x=890,y=380)
	elif(aux1==5):
		Label(framePrincipal,image=img_dado5).place(x=890,y=380)
	elif(aux1==6):
		Label(framePrincipal,image=img_dado6).place(x=890,y=380)

	aux2=choice([1,2,3,4,5,6])

	valorDado2.set(aux2)

	if(aux2==1):
		Label(framePrincipal,image=img_dado1).place(x=950,y=380)
	elif(aux2==2):
		Label(framePrincipal,image=img_dado2).place(x=950,y=380)	
	elif(aux2==3):
		Label(framePrincipal,image=img_dado3).place(x=950,y=380)
	elif(aux2==4):
		Label(framePrincipal,image=img_dado4).place(x=950,y=380)
	elif(aux2==5):
		Label(framePrincipal,image=img_dado5).place(x=950,y=380)
	elif(aux2==6):
		Label(framePrincipal,image=img_dado6).place(x=950,y=380)	

def moverArriba():
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
mapa_x.set(-200)
mapa_y.set(-200)

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


# BOTONES SALIR JUEGO
bt_salir=Button(frame_JuegoDeMesa,text="Salir",bg="#390606",width=20,height=1,bd=0,fg="white",command=salir).place(x=1200,y=700)
bt_guardar_salir=Button(frame_JuegoDeMesa,text="Guardar y Salir",bg="#390606",width=20,height=1,bd=0,fg="white",command=guardar_salir).place(x=1050,y=700)

# WIDGETS del juego

# nivel
Label(frame_JuegoDeMesa,text="Nivel",font=("Arial",15),bg="#5F0A0A",fg="white",bd=0).place(x=840,y=15)
et_nivel=Entry(frame_JuegoDeMesa,textvariable=nivel,width=5,justify="center",state="readonly",font=("Arial",15),bd=0).place(x=900,y=15)
# oro
Label(frame_JuegoDeMesa,image=imagenOro,bg="#5F0A0A").place(x=700,y=10)
et_oro=Entry(frame_JuegoDeMesa,textvariable=oro,width=6,state="readonly",font=("Arial",15),bd=0).place(x=740,y=15)
# exp
Label(frame_JuegoDeMesa,text="XP",bg="#5F0A0A",font=("Arial",15),bd=0,fg="white").place(x=1060,y=15)
et_exp=Entry(frame_JuegoDeMesa,textvariable=exp,width=5,font=("Arial",15),bd=0,justify="center",state="readonly").place(x=1000,y=15)
# celda
Label(frame_JuegoDeMesa,text="Celda",bg="#5F0A0A",font=("Arial",15),bd=0,fg="white").place(x=1230,y=15)
et_celda=Entry(frame_JuegoDeMesa,textvariable=celda,width=5,justify="center",state="readonly",font=("Arial",15),bd=0).place(x=1290,y=15)
# turno
Label(frame_JuegoDeMesa,text="Turno",bg="#5F0A0A",font=("Arial",15),bd=0,fg="white").place(x=1110,y=15)
et_turno=Entry(frame_JuegoDeMesa,textvariable=turno,width=3,justify="center",state="readonly",font=("Arial",15),bd=0)
et_turno.place(x=1170,y=15)
# Columna 1

Label(frame_JuegoDeMesa,image=imagenCorazon,bg="#5F0A0A").place(x=0,y=10)
et_vida=Entry(frame_JuegoDeMesa,textvariable=vida,width=4,justify="center",state="readonly",font=("Arial",15),bd=0).place(x=80,y=20)
								
Label(frame_JuegoDeMesa,image=imagenBarrera,bg="#5F0A0A").place(x=18,y=70)
et_barrera=Entry(frame_JuegoDeMesa,textvariable=barrera,width=4,justify="center",state="readonly",font=("Arial",15),bd=0).place(x=80,y=80)

Label(frame_JuegoDeMesa,image=imagenArmadura,bg="#5F0A0A").place(x=23,y=130)
et_armadura=Entry(frame_JuegoDeMesa,textvariable=armadura,width=4,justify="center",state="readonly",font=("Arial",15),bd=0).place(x=80,y=140)
# Columna 2

Label(frame_JuegoDeMesa,image=imagenEspada,bg="#5F0A0A").place(x=160,y=10)
et_daño=Entry(frame_JuegoDeMesa,textvariable=daño,width=4,justify="center",state="readonly",font=("Arial",15),bd=0).place(x=220,y=20)

Label(frame_JuegoDeMesa,image=imagenMana,bg="#5F0A0A").place(x=150,y=60)
et_mana=Entry(frame_JuegoDeMesa,textvariable=mana,width=4,justify="center",state="readonly",font=("Arial",15),bd=0).place(x=220,y=80)

Label(frame_JuegoDeMesa,image=imagenSuerte,bg="#5F0A0A").place(x=150,y=125)
et_suerte=Entry(frame_JuegoDeMesa,textvariable=suerte,width=4,justify="center",state="readonly",font=("Arial",15),bd=0).place(x=220,y=140)

# IMAGENES DE LAS PARTES DEL EQUIPAMIENTO
# Label(frame_JuegoDeMesa,image=imagenCabeza).place(x=20,y=200)
# Label(frame_JuegoDeMesa,image=imagenPecho).place(x=20,y=260)
# Label(frame_JuegoDeMesa,image=imagenPiernas).place(x=20,y=320)
# Label(frame_JuegoDeMesa,image=imagenPies).place(x=20,y=380)
# Label(frame_JuegoDeMesa,image=imagenArma).place(x=20,y=440)

txt_Inventario = Text(frame_JuegoDeMesa,width=30,height=20,bd=0,bg="#961010",fg="white")
txt_Inventario.place(x=20,y=200)

# entry Equipar/Desequipar/Usar/Activar
et_edua = Entry(frame_JuegoDeMesa,textvariable=objetoEDUA,width=3,justify="center",font=("Arial",15),bd=0)
et_edua.place(x=20,y=535)
bt_edua = Button(frame_JuegoDeMesa,text="Equip/Deseq/Usar/Activar",bg="#390606",width=25,command=EDUA,height=1,bd=0,fg="white")
bt_edua.place(x=80,y=535)

# Consola
txt_Consola = Text(frame_JuegoDeMesa,width=60,height=20,bd=0,bg="#961010",fg="white")
txt_Consola.place(x=280,y=200)

# Mapa
frameMapa=Frame(frame_JuegoDeMesa,width=220,height=220).place(x=1135,y=200)
Label(frameMapa,image=mapa).place(x=1135,y=500)


bt_accion=Button(frame_JuegoDeMesa,text="X",width=5,command=accion).place(x=1225,y=465)

bt_moverArriba=Button(frame_JuegoDeMesa,width=5,text="⇧",command=moverArriba).place(x=1225,y=430)
bt_moverAbajo=Button(frame_JuegoDeMesa,width=5,text="⇩",command=moverAbajo).place(x=1225,y=500)
bt_moverDerecha=Button(frame_JuegoDeMesa,width=5,text="⇨",command=moverDerecha).place(x=1285,y=465)
bt_moverIzquierda=Button(frame_JuegoDeMesa,width=5,text="⇦",command=moverIzquierda).place(x=1165,y=465)

et_celdasDisponibles=Entry(frame_JuegoDeMesa,state="readonly",textvariable=celdasDisponibles,font=("Arial",30),width=2).place(x=1070,y=360)

# Ver objeto
# txt_info_obj =Text(frame_JuegoDeMesa,width=30,height=7,bd=0,bg="#961010",fg="white",)
# txt_info_obj.place(x=110,y=570)
# et_obj_mirar = Entry(frame_JuegoDeMesa,textvariable=infoObjeto,width=3,justify="center",font=("Arial",15),bd=0).place(x=110,y=700)
# bt_Info =Button(frame_JuegoDeMesa,text="Info",bg="#390606",width=25,height=1,bd=0,fg="white").place(x=170,y=703)
	
# Mejorar objetos
et_obj1 = Entry(frame_JuegoDeMesa,textvariable=obj1,width=3,justify="center",font=("Arial",15),bd=0).place(x=20,y=600)
et_obj2 = Entry(frame_JuegoDeMesa,textvariable=obj2,width=3,justify="center",font=("Arial",15),bd=0).place(x=20,y=650)
et_obj3 = Entry(frame_JuegoDeMesa,textvariable=obj3,width=3,justify="center",font=("Arial",15),bd=0).place(x=20,y=700)
bt_mejorar = Button(frame_JuegoDeMesa,text="->",bg="#390606",width=2,height=8,bd=0,fg="white",command=mejorarObjeto).place(x=70,y=600)
Label(frame_JuegoDeMesa,text="Mejorar Objeto",font=("Arial",12),bg="#5F0A0A",fg="white").place(x=100,y=575)
et_nombreObj = Entry(frame_JuegoDeMesa,width=20,state="readonly",font=("Arial",15),bd=0).place(x=100,y=600)
txt_info_obj_mejorado = Text(frame_JuegoDeMesa,width=28,height=5,fg="white")
txt_info_obj_mejorado.place(x=100,y=630)

# Tirar dados
bt_TirarDados = Button(frame_JuegoDeMesa,text="Tirar dados",bg="#390606",width=10,height=2,bd=0,font=("Arial",15),fg="white",command=tirarDados).place(x=770,y=355)

et_dado1=Entry(frame_JuegoDeMesa,textvariable=valorDado1,width=3,font=("Arial",15),state="readonly",justify="center").place(x=1020,y=350)
et_dado2=Entry(frame_JuegoDeMesa,textvariable=valorDado2,width=3,font=("Arial",15),state="readonly",justify="center").place(x=1020,y=385)

# Enemigos

frameEnemigo=Frame(frame_JuegoDeMesa,width=500,height=140,bg="#390606").place(x=770,y=50)

Label(frameEnemigo,text="Enemigo:",font=("Arial",12),bg="#5F0A0A",fg="white").place(x=910,y=90)
et_enemigo = Entry(frameEnemigo,textvariable=nombreEnemigo,state="readonly",width=15,font=("Arial",15),bd=0)
et_enemigo.place(x=990,y=90)
Label(frameEnemigo,text="Daño: ",font=("Arial",12),bg="#5F0A0A",fg="white").place(x=910,y=120)
et_dañoEnemigo = Entry(frameEnemigo,textvariable=dañoEnemigo,state="readonly",width=3,justify="center",font=("Arial",15),bd=0).place(x=970,y=120)
Label(frameEnemigo,text="Vida: ",font=("Arial",12),bg="#5F0A0A",fg="white").place(x=1020,y=120)
et_vidaEnemigo = Entry(frameEnemigo,textvariable=vidaEnemigo,state="readonly",width=3,justify="center",font=("Arial",15),bd=0).place(x=1075,y=120)
Label(frameEnemigo,text="Nivel: ",font=("Arial",12),bg="#5F0A0A",fg="white").place(x=1120,y=120)
et_nivelEnemigo= Entry(frameEnemigo,textvariable=nivelEnemigo,state="readonly",width=3,justify="center",font=("Arial",15),bd=0).place(x=1170,y=120)
bt_luchar=Button(frameEnemigo,text="Luchar",bg="#961010",width=20,height=1,bd=0,font=("Arial",15),fg="white",command=preBatalla).place(x=910,y=160)
bt_huir=Button(frameEnemigo,text="Huir",bg="#961010",width=10,height=1,bd=0,font=("Arial",15),fg="white",command=huir).place(x=1145,y=160)
et_precau_enem = Entry(frameEnemigo,textvariable=precaucion,state="readonly",width=3,justify="center",bg="#390606",font=("Arial",15),bd=0).place(x=1220,y=120)
Label(frameEnemigo,text="Exp:",font=("Arial",12),bg="#5F0A0A",fg="white").place(x=1170,y=90)
et_expEnemigo = Entry(frameEnemigo,textvariable=expEnemigo,state="readonly",width=4,bg="#ffffff",font=("Arial",15),bd=0).place(x=1210,y=90)

Label(frameEnemigo,image=enem2).place(x=785,y=90)

nl_enemigo = Label(frameEnemigo,image=e3).place(x=880,y=90)

# Cofres / Recompenzas

frameCofres=Frame(frame_JuegoDeMesa,width=350,height=150,bg="#390606").place(x=770,y=200)

Label(frameCofres,image=imagenCofre).place(x=785,y=240)
nl_cofre = Label(frameCofres,image=e3).place(x=880,y=240)
bt_abrir_cofre = Button(frameCofres,text="Abrir",bg="#961010",width=16,height=1,bd=0,fg="white",command=abrirCofre).place(x=785,y=345)
et_precau_reco = Entry(frameCofres,textvariable=precaucionRecom,state="readonly",width=3,justify="center",bg="#390606",font=("Arial",15),bd=0).place(x=1260,y=400)

txt_recompenza = Text(frame_JuegoDeMesa,width=24,height=8)
txt_recompenza.place(x=915,y=210)

root.mainloop()