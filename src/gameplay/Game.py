from gameplay import Prey, Predator, Board
from pygame import Color
import pygame.surface
import engine

class Game:
	def __init__(self):
		self.__lives = 3
		self.__score = 0
		self.__time = 0
		self.__prey_spawn_position = (10, 10)
		self.__predator_spawn_position = (10, 10, 200, 200)
		#self.__prey_instant = Prey(self.__prey_spawn_position[0], self.__prey_spawn_position[1])
		#self.__predators = [Predator(self.__predator_spawn_position[0], self.__predator_spawn_position[1]), Predator(self.__predator_spawn_position[2], self.__predator_spawn_position[3])]
		self.__board = Board()
		self.__board.initialize_level(self)
	
	def cd_to_px(self, board_coordinates):
		"""Converts board coordinates to screen coordinates (in pixels)."""
		BOARD_SCALING_FACTOR = 16
		return ( \
			board_coordinates[0] * BOARD_SCALING_FACTOR + self.__board.rect.x, \
			board_coordinates[1] * BOARD_SCALING_FACTOR + self.__board.rect.y  \
		)
	
	def update(self):
		"""Essentially acts as the main game loop."""
		if(self.__lives < 0):
			#Indicate the game should not continue
			return False
		
		#TODO: what does this do?
		self.__time = self.__time + 1
		#Indicate the game should continue
		return True
	
	def draw(self, surface):
		surface.fill(Color(0,0,0))
		self.__board.draw(surface)
		
			