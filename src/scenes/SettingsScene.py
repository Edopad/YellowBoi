from engine import Scene



class SettingsScene(Scene):
	"""Scene template class."""
	
	def __init__(self):
		"""Called on scene creation."""
		#call superclass constructor
		super(type(self),self).__init__()

		self.__ai_error_checking = True
		self.__sfx_volume = 100
		self.__music_volume = 100
		self.__theme = None
		self.__close_button = UIButton("Close", 300, 140)

	def update(self, app, delta):
		"""Update scene objects, check user input, etc."""
		pass
	
	def render(self, screen):
		"""Render scene objects, buttons, text, etc."""
		pass
