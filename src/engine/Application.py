import pygame
from engine.ApplicationTheme import ApplicationTheme
#todo: implement or exclude keyboardManager



class Application:
	"""Handles scenes, update loop, and render loop."""
	
	def __init__(self):
		"""Constructor for the application. Only instanciates low-overhead items"""
		
		#Initialize *some* private variables, declare others.
		self.__current_scene = None
		self.__screen = None
		#self.__clock
		self.__running = False
		#self.__theme
		
		#Initialize parameters with default values.
		self.target_fps = 60
		self.window_caption = "YellowEngine"
		self.window_icon = None #pygame.surface data type; an icon for the game window
		
		#Initialize pygame. Not sure if this should be here.
		pygame.init()
		pygame.font.init()
		
		#Initialize private variables which require pygame module(s) initialization.
		self.__clock = pygame.time.Clock()
		self.__theme = ApplicationTheme()
	
	
	
	def run(self, initial_scene, starting_window_size = (1280, 720)):
		"""Runs the application, given some initial values."""
		
		#Check if this instance is already running. If it is, then do not run, and return a 'did not run' status.
		if self.__running:
			return False
		
		#Set status as running, so something else can't run this instance twice.
		self.__running = True
		
		#Initialize the window, and properties of it.
		#Set the window caption; skip this step if the caption is invalid.
		if self.window_caption:
			pygame.display.set_caption(self.window_caption)
		#Set the window icon, if necessary.
		if self.window_icon:
			pygame.display.set_icon(surface)
		#Create the screen.
		self.__gameScreen = pygame.display.set_mode(starting_window_size) #not resizable by user
		
		#Create a surface for scenes to draw to.
		self.__screen = pygame.Surface(self.__gameScreen.get_size(), pygame.SRCALPHA)
		
		#Set the current scene to the starting scene!
		self.__current_scene = initial_scene
		
		#Encompass update/render loop for error catching.
		#TODO: Review this, since this is basically a debug statement.
		self.main_loop()
		'''try:
			print("Exiting application. Reason: {}".format(self.main_loop()))
			#Safely exited.
		except Exception as error:
			#Exited on bad terms (due to uncaught error)!
			print("Exiting application on bad terms (due to uncaught error). Error details:")
			print(repr(error))
			print("Press enter to continue.")
			input()'''
		
		#TODO: Perform some cleanup of pygame things, if necessary.
		
		#Set status as no longer running.
		self.__running = False
		#Return status as successfully run.
		return True
	
	
	
	def switch_scene(self, new_scene):
		"""Switches current scene to another. Keeps stack."""
		
		print("Switching from scene {} to scene {}.".format( \
			self.__current_scene.get_name() if self.__current_scene else "<None>", \
			new_scene.get_name() if new_scene else "<None>"))
		#Replace current scene; do not worry about destroying the old one due to garbage collection.
		self.__current_scene = new_scene
	
	
	
	def change_theme(self, filename):
		return self.__theme.load_from_file(filename)
	
	
	
	def main_loop(self):
		"""The main update and render loops."""
		
		#Start the timer.
		self.__clock.tick(self.target_fps)
		
		#Main update and render loop (combined).
		while self.__current_scene:
			#Ticks `target_fps` times per second or lower, divided by 1000 to convert ms to s.
			delta = self.__clock.tick(self.target_fps) / 1000.0
			
			#Process events.
			evt = self.event_handler()
			#If an event failed to process, then stop the program.
			if evt:
				return evt
			#Update inputs.
			#keyboardManager.update()
			
			#Update the current scene.
			self.__current_scene.update(self, delta)
			
			#Render the current scene.
			self.__current_scene.render(self.__screen)
			
			#Push screenbuffer to display.
			self.__gameScreen.blit(self.__screen, self.__screen.get_rect())
			#Call this to send whatever has been rendered on screen over to the monitor.
			pygame.display.flip()
		
		#If the game loop exits, there is no current scene, and therefore nothing to do.
		#This should never happen; if it does, the program got lucky!
		return "Ran out of scenes!"
	
	
	
	def event_handler(self):
		"""Handles events from pygame."""

		#Only events which are handled by the engine are listed.
		#Others which are not are parsed, but no action is taken on them, so they are discarded so they don't clog up the queue.
		for evt in pygame.event.get():
			if   evt.type == pygame.QUIT:    return "Window closed."
			elif evt.type == pygame.KEYDOWN: return None#keyboardManager.down_event(evt)
			elif evt.type == pygame.KEYUP:   return None#keyboardManager.up_event(evt)
