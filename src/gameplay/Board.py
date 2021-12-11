from pygame import Rect
from pygame.sprite import Sprite
from gameplay.GridSquare import GridSquare



BOARD_ARRAY = [ \
[0x40,0x30,0x30,0x30,0x30,0x30,0x30,0x30,0x30,0x30,0x30,0x30,0x30,0x61,0x70,0x30,0x30,0x30,0x30,0x30,0x30,0x30,0x30,0x30,0x30,0x30,0x30,0x41], \
[0x33,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x03,0x01,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x31], \
[0x33,0x91,0x10,0x00,0x00,0x11,0x91,0x10,0x00,0x00,0x00,0x11,0x91,0x03,0x01,0x91,0x10,0x00,0x00,0x00,0x11,0x91,0x10,0x00,0x00,0x11,0x91,0x31], \
[0x33,0x91,0x03,0x92,0x92,0x01,0x91,0x03,0x92,0x92,0x92,0x01,0x91,0x03,0x01,0x91,0x03,0x92,0x92,0x92,0x01,0x91,0x03,0x92,0x92,0x01,0x91,0x31], \
[0x33,0x91,0x13,0x02,0x02,0x12,0x91,0x13,0x02,0x02,0x02,0x12,0x91,0x13,0x12,0x91,0x13,0x02,0x02,0x02,0x12,0x91,0x13,0x02,0x02,0x12,0x91,0x31], \
[0x33,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x31], \
[0x33,0x91,0x10,0x00,0x00,0x11,0x91,0x10,0x11,0x91,0x10,0x00,0x00,0x00,0x00,0x00,0x00,0x11,0x91,0x10,0x11,0x91,0x10,0x00,0x00,0x11,0x91,0x31], \
[0x33,0x91,0x13,0x02,0x02,0x12,0x91,0x03,0x01,0x91,0x13,0x02,0x02,0x21,0x20,0x02,0x02,0x12,0x91,0x03,0x01,0x91,0x13,0x02,0x02,0x12,0x91,0x31], \
[0x33,0x91,0x91,0x91,0x91,0x91,0x91,0x03,0x01,0x91,0x91,0x91,0x91,0x03,0x01,0x91,0x91,0x91,0x91,0x03,0x01,0x91,0x91,0x91,0x91,0x91,0x91,0x31], \
[0x43,0x32,0x32,0x32,0x32,0x51,0x91,0x03,0x23,0x00,0x00,0x11,0x90,0x03,0x01,0x90,0x10,0x00,0x00,0x22,0x01,0x91,0x50,0x32,0x32,0x32,0x32,0x42], \
[0x92,0x92,0x92,0x92,0x92,0x33,0x91,0x03,0x20,0x02,0x02,0x12,0x90,0x13,0x12,0x90,0x13,0x02,0x02,0x21,0x01,0x91,0x31,0x92,0x92,0x92,0x92,0x92], \
[0x92,0x92,0x92,0x92,0x92,0x33,0x91,0x03,0x01,0x90,0x90,0x90,0x90,0x90,0x90,0x90,0x90,0x90,0x90,0x03,0x01,0x91,0x31,0x92,0x92,0x92,0x92,0x92], \
[0x92,0x92,0x92,0x92,0x92,0x33,0x91,0x03,0x01,0x90,0x80,0x32,0x32,0x90,0x90,0x32,0x32,0x81,0x90,0x03,0x01,0x91,0x31,0x92,0x92,0x92,0x92,0x92], \
[0x30,0x30,0x30,0x30,0x30,0x52,0x91,0x13,0x12,0x90,0x31,0x90,0x90,0x90,0x90,0x90,0x90,0x33,0x90,0x13,0x12,0x91,0x53,0x30,0x30,0x30,0x30,0x30], \
[0x90,0x90,0x90,0x90,0x90,0x90,0x91,0x90,0x90,0x90,0x31,0x90,0x90,0x90,0x90,0x90,0x90,0x33,0x90,0x90,0x90,0x91,0x90,0x90,0x90,0x90,0x90,0x90], \
[0x32,0x32,0x32,0x32,0x32,0x51,0x91,0x10,0x11,0x90,0x31,0x90,0x90,0x90,0x90,0x90,0x90,0x33,0x90,0x10,0x11,0x91,0x50,0x32,0x32,0x32,0x32,0x32], \
[0x92,0x92,0x92,0x92,0x92,0x33,0x91,0x03,0x01,0x90,0x83,0x30,0x30,0x30,0x30,0x30,0x30,0x82,0x90,0x03,0x01,0x91,0x31,0x92,0x92,0x92,0x92,0x92], \
[0x92,0x92,0x92,0x92,0x92,0x33,0x91,0x03,0x01,0x90,0x90,0x90,0x90,0x90,0x90,0x90,0x90,0x90,0x90,0x03,0x01,0x91,0x31,0x92,0x92,0x92,0x92,0x92], \
[0x92,0x92,0x92,0x92,0x92,0x33,0x91,0x03,0x01,0x90,0x10,0x00,0x00,0x00,0x00,0x00,0x00,0x11,0x90,0x03,0x01,0x91,0x31,0x92,0x92,0x92,0x92,0x92], \
[0x40,0x30,0x30,0x30,0x30,0x52,0x91,0x13,0x12,0x90,0x13,0x02,0x02,0x21,0x20,0x02,0x02,0x12,0x90,0x13,0x12,0x91,0x53,0x30,0x30,0x30,0x30,0x41], \
[0x33,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x03,0x01,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x31], \
[0x33,0x91,0x10,0x00,0x00,0x11,0x91,0x10,0x00,0x00,0x00,0x11,0x91,0x03,0x01,0x91,0x10,0x00,0x00,0x00,0x11,0x91,0x10,0x00,0x00,0x11,0x91,0x31], \
[0x33,0x91,0x13,0x02,0x21,0x01,0x91,0x13,0x02,0x02,0x02,0x12,0x91,0x13,0x12,0x91,0x13,0x02,0x02,0x02,0x12,0x91,0x03,0x20,0x02,0x12,0x91,0x31], \
[0x33,0x91,0x91,0x91,0x03,0x01,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x03,0x01,0x91,0x91,0x91,0x31], \
[0x73,0x00,0x11,0x91,0x03,0x01,0x91,0x10,0x11,0x91,0x10,0x00,0x00,0x00,0x00,0x00,0x00,0x11,0x91,0x10,0x11,0x91,0x03,0x01,0x91,0x10,0x00,0x62], \
[0x60,0x02,0x12,0x91,0x13,0x12,0x91,0x03,0x01,0x91,0x13,0x02,0x02,0x21,0x20,0x02,0x02,0x12,0x91,0x03,0x01,0x91,0x13,0x12,0x91,0x13,0x02,0x71], \
[0x33,0x91,0x91,0x91,0x91,0x91,0x91,0x03,0x01,0x91,0x91,0x91,0x91,0x03,0x01,0x91,0x91,0x91,0x91,0x03,0x01,0x91,0x91,0x91,0x91,0x91,0x91,0x31], \
[0x33,0x91,0x10,0x00,0x00,0x00,0x00,0x22,0x23,0x00,0x00,0x11,0x91,0x03,0x01,0x91,0x10,0x00,0x00,0x22,0x23,0x00,0x00,0x00,0x00,0x11,0x91,0x31], \
[0x33,0x91,0x13,0x02,0x02,0x02,0x02,0x02,0x02,0x02,0x02,0x12,0x91,0x13,0x12,0x91,0x13,0x02,0x02,0x02,0x02,0x02,0x02,0x02,0x02,0x12,0x91,0x31], \
[0x33,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x91,0x31], \
[0x43,0x32,0x32,0x32,0x32,0x32,0x32,0x32,0x32,0x32,0x32,0x32,0x32,0x32,0x32,0x32,0x32,0x32,0x32,0x32,0x32,0x32,0x32,0x32,0x32,0x32,0x32,0x42]]



class Board(Sprite):
	
	def __init__(self):
		super(type(self),self).__init__()
		self.__perimeter_height = None
		self.__perimeter_width = None
		#initialize GridSquare matrix
		self.__grid_square_matrix = [None] * 31 #GridSquare[31][28]
		for y in range(len(self.__grid_square_matrix)):
			self.__grid_square_matrix[y] = [None] * 28
		
		BOARD_SCALING_FACTOR = 16
		self.rect = Rect(0, 0, BOARD_SCALING_FACTOR * 28, BOARD_SCALING_FACTOR * 31)
	
	def initialize_level(self, game):
		for y in range(len(self.__grid_square_matrix)):
			for x in range(len(self.__grid_square_matrix[0])):
				self.__grid_square_matrix[y][x] = GridSquare(game, (x,y), False, BOARD_ARRAY[y][x])
		

	def update(self):
		#update individual grid squares
		for grid_square_row in self.__grid_square_matrix:
			for grid_square in grid_square_row:
				if grid_square:
					grid_square.update()
		#

	def draw(self, surface):
		#draw individual grid squares
		for grid_square_row in self.__grid_square_matrix:
			for grid_square in grid_square_row:
				if grid_square:
					grid_square.draw(surface)