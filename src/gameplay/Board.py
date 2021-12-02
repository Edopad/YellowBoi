from pygame import sprite
from pygame.sprite import Sprite
import Grid_Square

class Board(Sprite):

	def __init__(self):	
		self.__perimeter_height = None
		self.__perimeter_width = None
		self.__out_of_bounds = False
		self.__grid_square_matrix = Grid_Square[32][32]

	def check_collision(self, x, y):
		pass

	def tick_time(self):
		for i in range(32):
			for j in  range(32):
				self.__grid_square_matrix[i][j].tick()