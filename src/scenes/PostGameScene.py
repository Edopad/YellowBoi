from engine import Scene



class PostGameScene(Scene):
	"""Scene template class."""
	
	def __init__(self):
		"""Called on scene creation."""
		#call superclass constructor
		super(type(self),self).__init__()
	
	def update(self, app, delta):
		"""Update scene objects, check user input, etc."""
		pass
	
	def render(self, screen):
		"""Render scene objects, buttons, text, etc."""
		pass
