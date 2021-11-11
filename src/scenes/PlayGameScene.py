from engine import Scene



class PlayGameScene(Scene):
	"""Scene template class."""
	
	def __init__(self):
		"""Called on scene creation."""
		#call superclass constructor
		super(type(self),self).__init__()
		
		self.__minimum_fps = 15
	
	def update(self, app, delta):
		"""Update scene objects, check user input, etc."""
		
		#protection against extremely low fps; pause if fps is below 
		if delta > (1.0 / self.__minimum_fps):
			print("Paused game due to low FPS. Setting highest delta.");
			self.pause()
			return
		pass
	
	def render(self, screen):
		"""Render scene objects, buttons, text, etc."""
		pass
