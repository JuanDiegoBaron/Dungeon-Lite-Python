from items import Item

class Armadura(Item):

	def __init__(self,nombre,valor,nivel,tipo,armadura,fuerza,aguante,agilidad,inteligencia,magia):

		super().__init__(nombre,valor,nivel)

		self.tipo=tipo
		self.armadura=armadura
		self.fuerza=fuerza
		self.aguante=aguante
		self.agilidad=agilidad
		self.inteligencia=inteligencia
		self.magia=magia

	def equiparDesequipar(self):

		if(self.tipo=="cabeza"):

			if(partida.personaje.equipamiento["cabeza"]=="vacio"):

				partida.personaje.equipamiento["cabeza"]=self.nombre
				partida.personaje.armadura+=self.armadura
				partida.personaje.fuerza+=self.fuerza
				partida.personaje.aguante+=self.aguante
				partida.personaje.agilidad+=self.agilidad
				partida.personaje.inteligencia+=self.inteligencia
				partida.personaje.magia+=self.magia

			elif(partida.personaje.equipamiento["cabeza"]==self.nombre):

				partida.personaje.equipamiento["cabeza"]="vacio"
				partida.personaje.armadura-=self.armadura
				partida.personaje.fuerza-=self.fuerza
				partida.personaje.aguante-=self.aguante
				partida.personaje.agilidad-=self.agilidad
				partida.personaje.inteligencia-=self.inteligencia
				partida.personaje.magia-=self.magia

		elif(self.tipo=="pecho"):

			if(partida.personaje.equipamiento["pecho"]=="vacio"):

				partida.personaje.equipamiento["pecho"]=self.nombre
				partida.personaje.armadura+=self.armadura
				partida.personaje.fuerza+=self.fuerza
				partida.personaje.aguante+=self.aguante
				partida.personaje.agilidad+=self.agilidad
				partida.personaje.inteligencia+=self.inteligencia
				partida.personaje.magia+=self.magia

			elif(partida.personaje.equipamiento["pecho"]==self.nombre):

				partida.personaje.equipamiento["pecho"]="vacio"
				partida.personaje.armadura-=self.armadura
				partida.personaje.fuerza-=self.fuerza
				partida.personaje.aguante-=self.aguante
				partida.personaje.agilidad-=self.agilidad
				partida.personaje.inteligencia-=self.inteligencia
				partida.personaje.magia-=self.magia

		elif(self.tipo=="piernas"):

			if(partida.personaje.equipamiento["piernas"]=="vacio"):

				partida.personaje.equipamiento["piernas"]=self.nombre
				partida.personaje.armadura+=self.armadura
				partida.personaje.fuerza+=self.fuerza
				partida.personaje.aguante+=self.aguante
				partida.personaje.agilidad+=self.agilidad
				partida.personaje.inteligencia+=self.inteligencia
				partida.personaje.magia+=self.magia

			elif(partida.personaje.equipamiento["piernas"]==self.nombre):

				partida.personaje.equipamiento["piernas"]="vacio"
				partida.personaje.armadura-=self.armadura
				partida.personaje.fuerza-=self.fuerza
				partida.personaje.aguante-=self.aguante
				partida.personaje.agilidad-=self.agilidad
				partida.personaje.inteligencia-=self.inteligencia
				partida.personaje.magia-=self.magia

		elif(self.tipo=="pies"):

			if(partida.personaje.equipamiento["pies"]=="vacio"):

				partida.personaje.equipamiento["pies"]=self.nombre
				partida.personaje.armadura+=self.armadura
				partida.personaje.fuerza+=self.fuerza
				partida.personaje.aguante+=self.aguante
				partida.personaje.agilidad+=self.agilidad
				partida.personaje.inteligencia+=self.inteligencia
				partida.personaje.magia+=self.magia

			elif(partida.personaje.equipamiento["pies"]==self.nombre):

				partida.personaje.equipamiento["pies"]="vacio"
				partida.personaje.armadura-=self.armadura
				partida.personaje.fuerza-=self.fuerza
				partida.personaje.aguante-=self.aguante
				partida.personaje.agilidad-=self.agilidad
				partida.personaje.inteligencia-=self.inteligencia
				partida.personaje.magia-=self.magia

		partida.crearFrameSuperior()
