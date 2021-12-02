from pygame.sprite import Sprite



class Predator(Sprite):
	
	def __init__(self, x, y, size):
		super.__init__(x, y, size, size)
		self.__last_key = ""
		self.__pos_x = x
		self.__pos_y = y
		self.__speed = None
		self.__size = None

	def move(self):
		if self.__last_key == "UP":
			self.__pos_y += self.__speed
		elif self.__last_key == "DOWN":
			self.__pos_y -= self.__speed
		elif self.__last_key == "LEFT":
			self.__pos_x -= self.__speed
		elif self.__last_key == "RIGHT":
			self.__pos_x += self.__speed

	def direction_change(self, key):
		self.__last_key = key

	def get_x(self):
		return self.__pos_x

	def get_y(self):
		return self.__pos_y

	def get_size(self):
		return self.__size