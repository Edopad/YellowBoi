from pygame.sprite import Sprite
import Grid_Square

class Board:

	def __init__(self):	
		self.__perimeter_height = 300
		self.__perimeter_width = 300
		self.__out_of_bounds = False
		self.__grid_square_matrix = Grid_Square[32][32]

