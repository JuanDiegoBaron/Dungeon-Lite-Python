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

	def __init__(self):

		self.running = False

		self.root = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) 

		self.screens = []

		self.currentScreen = 0

	def add_screens(self,screens):

		self.screens.extend(screens)
		# print(type(self.screens), "     ", self.screens)

		self.currentScreen = self.screens[0]
		# print("ACA    ", type(self.currentScreen))

	def event_listener(self):

		for event in pygame.event.get():

			if event.type == pygame.QUIT:

				pygame.quit()
				sys.exit()
			
	def change_screen(self,newScreen):
	
		index = 0
		for screen in self.screens:

			if screen.name == newScreen:

				self.currentScreen = self.screens[index]
				return 	

			index+=1	

	def run(self):
	
		
		self.running = True

		while self.running:

			self.event_listener()

			# Logica del juego
			self.currentScreen.run()

			# Actualizar pantalla
			pygame.display.flip()

			# Velocidad de la animacion
			pygame.time.Clock().tick(60)		

class Frame():

	def __init__(self,game,name,elements,event_listener,color=BLACK,image=""):

		self.game = game
		self.name=name
		self.running = False
		self.color=color
		self.image=image
		self.screen = game.root
		self.elements = elements
		self.event_listener = lambda:event_listener()

	def render(self):
	
		if(self.image==""):
		
			pygame.draw.rect(self.color)

		else:

			background = pygame.image.load(self.image)#.convert()
			self.screen.blit(background,(0,0))

	# eventos de teclado entre otros
	def common_event_listener(self):

		for event in pygame.event.get():

			if event.type == pygame.QUIT:

				self.running==False	
				pygame.quit()
				sys.exit()

			# Eventos de tecla precionada	
			elif event.type == pygame.KEYDOWN:

				# if event.key == pygame.K_SPACE:
					
				# 	self.game.change_screen("Character creator")
				# 	self.running = False

				if event.key == pygame.K_ESCAPE:

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

			self.common_event_listener()
			self.event_listener()
			self.render()
			self.update()

			# Actualizar pantalla
			pygame.display.flip()

			# Velocidad de la animacion
			clock.tick(60)


#########################################################
#						 MAIN							#
#########################################################


myGame = Game()

def event_listener_menu():

	for event in pygame.event.get():

			# Eventos de tecla precionada	
			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_SPACE:
					
					self.game.change_screen("Character creator")
					self.running = False


def event_listener_characterCreator():

	print(" EVENTOS ESPECIFICOS")
	for event in pygame.event.get():

			# Eventos de tecla precionada	
			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_SPACE:
					
					self.game.change_screen("Menu")
					self.running = False


# VENTANAS
screen_menu = Frame(
	myGame, # game
	"Menu", # name
	[], # elementos
	lambda:event_listener_menu(),
	image="assets/images/fondo2.jpg" # image
)

screen_characterCreator = Frame(
	myGame,
	"Character creator",
	[], # elementos
	lambda:event_listener_characterCreator(),
	image="assets/images/fondo.png"
)




myGame.add_screens([screen_menu,screen_characterCreator])

myGame.run()

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