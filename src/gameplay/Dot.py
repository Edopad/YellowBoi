import engine
from pygame.sprite import Sprite
#from pygame import Color
import pygame.color


class Dot(Sprite):

	def __init__(self, position, start_spawned = True, does_auto_respawn = True, respawn_timer_reset = 30, respawn_timer_initial = -1):
		#call superclass constructor
		super(type(self),self).__init__()
		#create graphics and collider
		#load image
		self.image = engine.load_image("board", "dot_2x.png")
		#position object
		self.rect = position
		#initialize private variables
		self.__spawned = start_spawned
		self.__does_auto_respawn = does_auto_respawn
		self.__respawn_timer_reset = respawn_timer_reset
		self.__respawn_timer_value = respawn_timer_initial# if (respawn_timer_initial != None) else -1
	
	def respawn(self):
		self.__spawned = True
	
	def despawn(self):
		self.__spawned = False
		self.__respawn_timer_value = self.__respawn_timer_reset
	
	def get_visible(self):
		#A dot is visible if its respawn timer value is less than 0.
		return self.__spawned
	
	def update():
		#decrement timer
		self.respawn_timer = self.respawn_timer - 1
		#check if dot should automatically respawn
		if self.__respawn_timer == -1 and self.__does_auto_respawn:
			self.respawn()

	def draw(self, surface):
		surface.blit(self.image, self.rect)