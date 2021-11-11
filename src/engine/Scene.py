#Scene - a part of the game, such as the main menu or play screen.
#these can also be individual levels
class Scene:

	def __init__(self):
		"""Called on scene creation."""
		pass

	def __del__(self):
		"""Called on scene deletion (garbage collection). Here for debugging."""
		
		#debug statement(s)
		print("Scene {} deleted.".format(self.get_name()))

	def get_name(self):
		"""Here for naming purposes. Can be overridden for manual control over scene name."""
		return self.__class__.__name__

	def update(self, app, delta):
		"""Update scene objects, check user input, etc."""
		
		#debug statement(s)
		print("Scene {} has no update method!".format(self.get_name()))
		app.switch_scene(None)

	def render(self, screen):
		"""Render scene objects, buttons, text, etc."""
		
		#debug statement(s)
		print("Scene {} has no render method!".format(self.get_name()))
