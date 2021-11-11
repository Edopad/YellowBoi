from pygame.sprite import Sprite
import Dot



class Board:
	__perimeter_height = 300
	__perimeter_width = 300
	__out_of_bounds = False
	__prey_spawn_position = (10, 10)
	__predator_spawn_position = (10, 10, 200, 200)
	__dot_matrix = []
