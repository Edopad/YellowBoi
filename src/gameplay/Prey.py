from pygame.sprite import Sprite
from gameplay import AIPlayer



class Prey(Sprite):

	def __init__(self, x, y):
		self.__still_alive = True
		self.__difficulty_setting = 0
		self.__ai_player_instance = AIPlayer()
		self.__pos_x = x
		self.__pos_y = y

	def move(self, x, y):
		self.__pos_x += x
		self.__pos_y += y
	
	def update_living_status(status):
		__still_alive = status