from pygame import Color, Rect
from pygame.font import Font, SysFont
from pygame.sprite import Sprite



class UIButton(Sprite):

	def __init__(self, text, width, height, text_font = None, text_color = None, background_color = None, border_color = None):
		super(type(self),self).__init__()
		self.__text = text
		self.__highlighted = False
		self.__active = True
		self.__bounding_box = Rect(0, 0, width, height)
		
		self.__text_font        = text_font        if text_font        else SysFont('Calibri', 18, bold = False, italic = False)
		self.__text_color       = text_color       if text_color       else Color(255, 255, 255)
		self.__background_color = background_color if background_color else Color(  0,   0,   0)
		self.__border_color     = border_color     if border_color     else Color(255, 255, 255)

	def set_active_status(self, status):
		self.__active = status

	def get_active_status(self):
		return self.__active

	def set_highlight_status(self, status):
		self.__highlighted = status

	def get_highlight_status(self):
		return self.__highlighted