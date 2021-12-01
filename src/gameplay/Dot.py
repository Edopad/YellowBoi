from pygame.sprite import Sprite



class Dot(Sprite):

	def __init__(self):
		super().__init__()
		self.respawn_timer = 30
		self.__visible = True
