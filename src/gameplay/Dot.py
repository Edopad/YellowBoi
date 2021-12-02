from pygame.sprite import Sprite

class Dot(Sprite):

	def __init__(self):
		super().__init__()
		self.respawn_timer = 30
		self.__visible = True

	def respawn(self):
		self.__visible = True
	
	def consume(self):
		self.__visible = False

	def get_visible(self):
		return self.__visible
