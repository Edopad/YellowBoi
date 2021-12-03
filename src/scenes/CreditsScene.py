from engine import Scene



class CreditsScene(Scene):
	"""Scene template class."""
	
	def __init__(self):
		"""Called on scene creation."""
		#call superclass constructor
		super(type(self),self).__init__()

		self._credits_render = UIButton("Credits", 300, 140)
		self._close_button = UIButton("Close", 300, 140)
	
	def update(self, app, delta):
		"""Update scene objects, check user input, etc."""
		pass
	
	def render(self, screen):
		"""Render scene objects, buttons, text, etc."""
		pass
