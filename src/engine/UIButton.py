from pygame.sprite import Sprite



class UIButton(Sprite):

	def __init__(self, text, width, height):
		self.__text = text
		self.__highlighted = False
		self.__active = True
		self.__bounding_box

	def set_active_status(self, status):
		self.__active = status

	def get_active_status(self):
		return self.__active

	def set_highlight_status(self, status):
		self.__highlighted = status

	def get_highlight_status(self):
		return self.__highlighted