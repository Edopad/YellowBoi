from pygame.sprite import Sprite
import AIPlayer



class Prey(Sprite):

	def __init__(self):
		__still_alive = True
		__difficulty_setting = 0
		__ai_player_instance = AIPlayer()

	def move():
		pass
	
	def update_living_status(status):
		__still_alive = status