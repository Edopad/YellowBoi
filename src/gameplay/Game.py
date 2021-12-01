import Prey, Predator, Board


class Game:
	def __init__(self):
		self.__lives = 3
		self.__score = 0
		self.__time = 0
		self.__prey_spawn_position = (10, 10)
		self.__predator_spawn_position = (10, 10, 200, 200)
		self.__prey_instant = Prey(self.__prey_spawn_position[0], self.__prey_spawn_position[1])
		self.__predators = (Predator(self.__predator_spawn_position[0], self.__predator_spawn_position[1]), Predator(self.__predator_spawn_position[2], self.__predator_spawn_position[3]))
		self.__board = Board()

		self._game_loop

	def _game_loop(self):

		while(self.__lives > 0):
			
			#Game code
			#collision checking
			#Key handling

			self.__time = self.__time + 1
