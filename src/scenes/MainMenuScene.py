from engine import Scene
#TODO: Figure out importing Surface from pygame
#from pygame import Surface



class MainMenuScene(Scene):
	"""Scene template class."""
	
	
	def __init__(self, first_run = False):
		"""Called on scene creation."""
		#call superclass constructor
		super(type(self),self).__init__()
		
		self.__first_run = first_run
		self._title_text = None
		self._play_button = None
		self._background_image = None
	
	def update(self, app, delta):
		"""Update scene objects, check user input, etc."""
		
		#only run this once, at the beginning of the application launch
		if self.__first_run:
			self.__first_run = False
			
			#proof-of-concept code for AI selection
			import tkinter, tkinter.filedialog
			root = tkinter.Tk()
			root.withdraw()
			
			file_path = tkinter.filedialog.askopenfilename( \
				title = "Select AI File", \
				multiple = False, \
				initialdir = "..\\data\\AIs", \
				filetypes = [("Python File", "*.py"), ("All Files", "*.*")], \
			)
			
	
	def render(self, screen):
		"""Render scene objects, buttons, text, etc."""
		pass
