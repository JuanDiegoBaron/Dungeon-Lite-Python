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

# Funciones botones

def EDUA():
	pass
def mejorarObjeto():
	pass
def tirarDados():
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

# valorDado1=StringVar()
# valorDado1.set(1)
# valorDado2=StringVar()
# valorDado2.set(1)

daño_enemigo=StringVar()
vida_enemigo=StringVar()
nombreEnemigo=StringVar()
nivelEnemigo=StringVar()
exp_enemigo=StringVar()

valorDado1=StringVar()
valorDado1.set(1)
valorDado2=StringVar()
valorDado2.set(1)

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
Label(frame_JuegoDeMesa,text="Nivel",font=("Arial",15),bg="#5F0A0A",fg="white",bd=0).place(x=840,y=20)
et_nivel=Entry(frame_JuegoDeMesa,textvariable=nivel,width=5,justify="center",state="readonly",font=("Arial",15),bd=0).place(x=900,y=20)
# oro
Label(frame_JuegoDeMesa,image=imagenOro,bg="#5F0A0A").place(x=700,y=15)
et_oro=Entry(frame_JuegoDeMesa,textvariable=oro,width=6,state="readonly",font=("Arial",15),bd=0).place(x=740,y=20)
# exp
Label(frame_JuegoDeMesa,text="XP",bg="#5F0A0A",font=("Arial",15),bd=0,fg="white").place(x=1060,y=20)
et_exp=Entry(frame_JuegoDeMesa,textvariable=exp,width=5,font=("Arial",15),bd=0,justify="center",state="readonly").place(x=1000,y=20)
# celda
Label(frame_JuegoDeMesa,text="Celda",bg="#5F0A0A",font=("Arial",15),bd=0,fg="white").place(x=1230,y=20)
et_celda=Entry(frame_JuegoDeMesa,textvariable=celda,width=5,justify="center",state="readonly",font=("Arial",15),bd=0).place(x=1290,y=20)
# turno
Label(frame_JuegoDeMesa,text="Turno",bg="#5F0A0A",font=("Arial",15),bd=0,fg="white").place(x=1110,y=20)
et_turno=Entry(frame_JuegoDeMesa,textvariable=turno,width=3,justify="center",state="readonly",font=("Arial",15),bd=0)
et_turno.place(x=1170,y=20)
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
Label(frame_JuegoDeMesa,image=imagenCabeza).place(x=20,y=200)
Label(frame_JuegoDeMesa,image=imagenPecho).place(x=20,y=260)
Label(frame_JuegoDeMesa,image=imagenPiernas).place(x=20,y=320)
Label(frame_JuegoDeMesa,image=imagenPies).place(x=20,y=380)
Label(frame_JuegoDeMesa,image=imagenArma).place(x=20,y=440)

txt_Inventario = Text(frame_JuegoDeMesa,width=30,height=20,bd=0,bg="#961010",fg="white")
txt_Inventario.place(x=110,y=200)

# entry Equipar/Desequipar/Usar/Activar
et_edua = Entry(frame_JuegoDeMesa,textvariable=objetoEDUA,width=3,justify="center",font=("Arial",15),bd=0)
et_edua.place(x=110,y=535)
bt_edua = Button(frame_JuegoDeMesa,text="Equip/Deseq/Usar/Activar",bg="#390606",width=25,command=EDUA,height=1,bd=0,fg="white")
bt_edua.place(x=170,y=535)

# Consola
txt_Consola = Text(frame_JuegoDeMesa,width=60,height=20,bd=0,bg="#961010",fg="white")
txt_Consola.place(x=380,y=200)

# Ver objeto
txt_info_obj =Text(frame_JuegoDeMesa,width=30,height=7,bd=0,bg="#961010",fg="white",)
txt_info_obj.place(x=110,y=570)
et_obj_mirar = Entry(frame_JuegoDeMesa,textvariable=infoObjeto,width=3,justify="center",font=("Arial",15),bd=0).place(x=110,y=700)
bt_Info =Button(frame_JuegoDeMesa,text="Info",bg="#390606",width=25,height=1,bd=0,fg="white").place(x=170,y=703)
	
# Mejorar objetos
et_obj1 = Entry(frame_JuegoDeMesa,textvariable=obj1,width=3,justify="center",font=("Arial",15),bd=0).place(x=880,y=520)
et_obj2 = Entry(frame_JuegoDeMesa,textvariable=obj2,width=3,justify="center",font=("Arial",15),bd=0).place(x=880,y=580)
et_obj3 = Entry(frame_JuegoDeMesa,textvariable=obj3,width=3,justify="center",font=("Arial",15),bd=0).place(x=880,y=640)
bt_mejorar = Button(frame_JuegoDeMesa,text="->",bg="#390606",width=2,height=9,bd=0,fg="white",command=mejorarObjeto).place(x=930,y=520)
et_nombreObj = Entry(frame_JuegoDeMesa,width=20,state="readonly",font=("Arial",15),bd=0).place(x=960,y=520)
txt_info_obj_mejorado = Text(frame_JuegoDeMesa,width=28,height=7,fg="white")
txt_info_obj_mejorado.place(x=960,y=550)

# Tirar dados
bt_TirarDados = Button(frame_JuegoDeMesa,text="Tirar dados",bg="#390606",width=40,height=4,bd=0,fg="white",command=tirarDados).place(x=480,y=635)

et_dado1=Entry(frame_JuegoDeMesa,textvariable=valorDado1,width=3,state="readonly",justify="center").place(x=480,y=600)
et_dado2=Entry(frame_JuegoDeMesa,textvariable=valorDado2,width=3,state="readonly",justify="center").place(x=740,y=600)
				
dado1=Label(frame_JuegoDeMesa,image=img_dado3).place(x=400,y=640)		
dado2=Label(frame_JuegoDeMesa,image=img_dado5).place(x=790,y=640)

# Enemigos
Label(frame_JuegoDeMesa,text="Enemigo:",font=("Arial",12),bg="#5F0A0A",fg="white").place(x=1016,y=175)
et_enemigo = Entry(frame_JuegoDeMesa,textvariable=nombreEnemigo,state="readonly",width=15,font=("Arial",15),bd=0)
et_enemigo.place(x=1020,y=200)
Label(frame_JuegoDeMesa,text="Daño: ",font=("Arial",12),bg="#5F0A0A",fg="white").place(x=1016,y=235)
et_dañoEnemigo = Entry(frame_JuegoDeMesa,textvariable=daño_enemigo,state="readonly",width=3,justify="center",font=("Arial",15),bd=0).place(x=1066,y=235)
Label(frame_JuegoDeMesa,text="Vida: ",font=("Arial",12),bg="#5F0A0A",fg="white").place(x=1110,y=235)
et_vidaEnemigo = Entry(frame_JuegoDeMesa,textvariable=vida_enemigo,state="readonly",width=3,justify="center",font=("Arial",15),bd=0).place(x=1160,y=235)
Label(frame_JuegoDeMesa,text="Nivel: ",font=("Arial",12),bg="#5F0A0A",fg="white").place(x=1200,y=235)
et_nivelEnemigo= Entry(frame_JuegoDeMesa,textvariable=nivelEnemigo,state="readonly",width=3,justify="center",font=("Arial",15),bd=0).place(x=1250,y=235)
bt_luchar=Button(frame_JuegoDeMesa,text="Luchar",bg="#390606",width=10,height=1,bd=0,fg="white",command=preBatalla).place(x=1020,y=286)
bt_huir=Button(frame_JuegoDeMesa,text="Huir",bg="#390606",width=10,height=1,bd=0,fg="white",command=huir).place(x=1120,y=286)
et_precau_enem = Entry(frame_JuegoDeMesa,textvariable=precaucion,state="readonly",width=3,justify="center",bg="#390606",font=("Arial",15),bd=0).place(x=1200,y=200)
Label(frame_JuegoDeMesa,text="Exp:",font=("Arial",12),bg="#5F0A0A",fg="white").place(x=1250,y=200)
et_exp_enemigo = Entry(frame_JuegoDeMesa,textvariable=exp_enemigo,state="readonly",width=4,bg="#ffffff",font=("Arial",15),bd=0).place(x=1300,y=200)
Label(frame_JuegoDeMesa,image=enem2).place(x=880,y=200)
nl_enemigo = Label(frame_JuegoDeMesa,image=e3).place(x=980,y=200)

# Cofres / Recompenzas


Label(frame_JuegoDeMesa,image=imagenCofre).place(x=880,y=350)
nl_cofre = Label(frame_JuegoDeMesa,image=e3).place(x=980,y=350)
bt_abrir_cofre = Button(frame_JuegoDeMesa,text="Abrir",bg="#390606",width=17,height=1,bd=0,fg="white",command=abrirCofre).place(x=880,y=460)
et_precau_reco = Entry(frame_JuegoDeMesa,textvariable=precaucionRecom,state="readonly",width=3,justify="center",bg="#390606",font=("Arial",15),bd=0).place(x=1260,y=400)

txt_recompenza = Text(frame_JuegoDeMesa,width=28,height=8)
txt_recompenza.place(x=1010,y=350)

root.mainloop()