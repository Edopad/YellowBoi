from pygame.sprite import Sprite



class Predator(Sprite):
	
	def __init__(self, x, y):
		self.__pos_x = x
		self.__pos_y = y

	def move(self, x, y):
		self.__pos_x += x
		self.__pos_y += y

