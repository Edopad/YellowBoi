from pygame.sprite import Sprite
import pygame as pyg
from pygame import Color
from pygame.font import Font, SysFont



class UIButton(Sprite):

	def __init__(self, text, width, height, text_font = SysFont('Calibri', 18, bold = False, italic = False), text_color = Color(255, 255, 255), background_color = Color(  0,   0,   0), border_color = Color(255, 255, 255)):
		self.__text = text
		self.__highlighted = False
		self.__active = True
		self.__bounding_box = pyg.Rect(0, 0, width, height)
		
		self.text_font             = text_font
		self.text_color            = text_color
		self.background_color      = background_color
		self.border_color          = border_color

	def set_active_status(self, status):
		self.__active = status

	def get_active_status(self):
		return self.__active

	def set_highlight_status(self, status):
		self.__highlighted = status

	def get_highlight_status(self):
		return self.__highlighted