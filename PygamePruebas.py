import pygame
import sys
# import os

pygame.init()

# Dimenciones pantalla
SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768

# COLORES
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#CLASES

class Game():

	def __init__(self,screens):

		self.running = False

		self.screens = screens

		self.currentScreen = self.screens[0]

	def change_screen(self,newScreen):
	
		pass

	def run(self):
	
		print("Run")
		self.running = True

		while self.running:

			for event in pygame.event.get():

				if event.type == pygame.QUIT:

					pygame.quit()
					sys.exit()	

			# Logica del juego
		
			self.currentScreen.run()

			# Actualizar pantalla
			pygame.display.flip()

			# Velocidad de la animacion
			pygame.time.Clock().tick(60)		

class Screen():

	def __init__(self,nombre,color=BLACK,image=""):

		self.nombre=nombre
		self.running = False
		self.color=color
		self.image=image
		self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
		self.elements = []

	def render(self):
	
		if(self.image==""):
		
			self.screen.fill(self.color)

		else:

			background = pygame.image.load(self.image)#.convert()
			self.screen.blit(background,(0,0))

	# eventos de teclado entre otros
	def event_listener(self):

		for event in pygame.event.get():

			if event.type == pygame.QUIT:

				print("se cerro la ventana")
				self.running==False	
				pygame.quit()
				sys.exit()

	# VERIFICACIONES (coliciones,etc)
	def update(self):
	
		pass
		
	def run(self):
	
		clock = pygame.time.Clock()
		self.running = True

		while self.running:

			self.event_listener()
			self.render()
			self.update()

			# Actualizar pantalla
			pygame.display.flip()

			# Velocidad de la animacion
			clock.tick(60)


# menu = Screen(image="assets/images/texturamapa.jpg")
menu = Screen("Menu",image="assets/images/fondo2.jpg")
creacionPersonaje = Screen("Creacion Personaje",image="assets/images/fondo.png")

myGame = Game([menu,creacionPersonaje])

# while True:

# 	for event in pygame.event.get():

# 		if event.type == pygame.QUIT:

# 			pygame.quit()
# 			sys.exit()

# 		# Logica del juego
		
# 		menu.run()
# 		menu2.run()

# 		# Actualizar pantalla
# 		pygame.display.flip()

# 		# Velocidad de la animacion
# 		pygame.time.Clock().tick(60)	