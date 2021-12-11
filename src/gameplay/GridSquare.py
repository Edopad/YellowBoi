from pygame.sprite import Sprite
import gameplay
import engine
import pygame.surface
from pygame import Rect

class GridSquare(Sprite):
	def __init__(self, game, position, traversable, texture_id = 0):
		super(type(self),self).__init__()
		self.__dot = None
		self.__texture_id = texture_id
		self.__traversable = traversable
		
		#create graphics and collider
		#load image
		self.image = engine.load_image("Tileset_Default.png")#("Tileset_Default.png")
		#self.image.fill(pygame.Color(0,0,0))
		#position object
		self.rect = Rect(0,0,16,16)#self.image.get_rect()
		self.rect.x, self.rect.y = game.cd_to_px((position[0], position[1]))
		
		if texture_id == 0x91:
			self.__dot = gameplay.Dot(self.rect)

	def is_traversable(self):
		return self.__traversable

	def update(self):
		if self.__dot:
			self.__dot.update()
	
	def draw(self, surface):
		#return surface.blit(self.image, self.rect, Rect(0,0,16,16))
		surface.blit(self.image, self.rect, Rect(16*(self.__texture_id % 4), 16*(self.__texture_id // 16), 16, 16))
		#draw the dot this space contains, if it has one
		if self.__dot:
			self.__dot.draw(surface)
	

		

'''
class Path(GridSquare):
	def __init__(self, position, path_type = 0):
		super(type(self),self).__init__(position, traversable = True, texture_id = path_type)
		self.__dot = Dot()
	
	def is_traversable(self):
		return True
	
	def update(self):
	
	def render(self, surface):
		#draw grid square
		super(type(self),self).render(surface)
		#draw the enclosed dot
		self.__dot.draw(surface)


class Blockade(GridSquare):
	def __init__(self, path_type = 0):
		super(type(self),self).__init__(traversable = False, texture_id = path_type)

	def is_traversable(self):
		return False
'''