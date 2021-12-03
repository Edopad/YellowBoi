from engine import Scene



class PauseGameScene(Scene):
	"""Scene template class."""
	
	def __init__(self):
		"""Called on scene creation."""
		#call superclass constructor
		super(type(self),self).__init__()

		self._resume_button = UIButton("Resume", 300, 140)
		self._exit_button = UIButton("Exit", 300, 140)
		self._pause_text = UIButton("Pause", 300, 140)

	def update(self, app, delta):
		"""Update scene objects, check user input, etc."""
		pass
	
	def render(self, screen):
		"""Render scene objects, buttons, text, etc."""
		pass
