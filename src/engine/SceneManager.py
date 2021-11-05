import pygame
import math
import engine.graphics

#Not sure if this should be here.
pygame.init()

#set the window caption
pygame.display.set_caption("Breakout!")
#set the window icon
#pygame.display.set_icon(surface)
starting_size = (1280, 720)
#Here for game engine only - do not use!
gameScreen = pygame.display.set_mode(starting_size, pygame.RESIZABLE)
engine.graphics.resize(starting_size)


#Handles Scenes and gameloop
class SceneManager:

	#Here for organization purposes. May be temporary.
	class SafeExit(Exception):
		pass

	def __init__(self):

		self.scenes = []
		self.screens = []

		self.targetFPS = 60
		self.minFPS = 15
		self.clock = pygame.time.Clock()
	
	def add_scene(self, scene):
		"""Adds a scene to the stack, useful in pause menus."""
		print("Scene Manager: Adding {}.".format(scene.get_name()))
		self.silent_add_scene(scene)

	def switch_scene(self, scene):
		"""Switches current scene to another. Keeps stack."""
		print("Scene Manager: Switching from {} to {}.".format(self.scenes[-1].get_name() if self.scenes else "<None>", scene.get_name()))
		#get out of old scene
		self.silent_exit_scene()
		#add new scene
		self.silent_add_scene(scene)

	def replace_scene(self, scene):
		"""Replaces current scenes with a scene. Clears stack."""
		print("Scene Manager: Replacing to {}.".format(scene.get_name()))
		#get out of old scene
		while self.scenes:
			self.silent_exit_scene()
		#add new scene
		self.silent_add_scene(scene)

	def exit_scene(self):
		"""Exits current scene."""
		if(not self.scenes):
			return
		print("Scene Manager: Exiting {}.".format(self.scenes[-1].get_name()))
		self.silent_exit_scene()
	
	#Only for internal engine use, due to no debug print statements.
	def silent_add_scene(self, scene):
		#push the scene to the stack without replacing the top
		self.scenes.append(scene)
		self.screens.append(pygame.Surface(gameScreen.get_size(),pygame.SRCALPHA))

	#Only for internal engine use, due to no debug print statements.
	def silent_exit_scene(self):
		#protection for empty scene stack
		if not self.scenes:
			return
		#remove current scene from stack
		scene = self.scenes.pop()
		screen = self.screens.pop()
		#destroy the scene (here for future reference)
		#scene.destroy()

	def run(self,scene = None):
		"""Starts the game, with an optional starting scene."""

		#start at provided scene if it exists
		if(scene):
			self.add_scene(scene)
		#start the timer
		self.clock.tick(60)
		#encompass loop for easy exiting
		try:
			print("Scene Manager: Exiting game. Reason: {}.".format(self.main_loop()))
			exit()
		#Safely exited
		except self.SafeExit as error:
			reason = "safe exit"
			print("Exiting game. Reason: {}.".format(repr(error)))
		#Exited on bad terms
		#except Exception as error:
		#	print("Exiting game on bad terms.")
		#	print(repr(error))
		#	print("Press enter to continue.")
		#	input()
		#self.scenes = []
		exit()

	def main_loop(self):
		"""The main game loop."""
		while(self.scenes):

			#process events
			evt = self.event_handler()
			if(evt):
				return evt

			# ticks targetFPS times per second, divided by 1000 to convert ms to s
			delta = self.clock.tick(self.targetFPS) / 1000.0

			#protection against extremely low fps; pause if fps is below 
			if delta > (1.0 / self.minFPS):
				print("Scene Manager: Called scene ({}) pause() due to low FPS. Setting highest delta.".format(self.scenes[-1].get_name()))
				self.scenes[-1].pause()
				#set delta to highest allowed value for update protection
				delta = 1.0 / self.minFPS

			#only update and render current (top/focused) scene

			#try to update the current scene
			self.scenes[-1].update(delta)
			#right now this is the only leak, therefore it warrants a check here, but nowhere else.
			if not self.scenes: break

			#render the current scene
			self.scenes[-1].render(self.screens[-1])

			#render all scenes on top of one another
			for curscreen in self.screens:
				gameScreen.blit(curscreen, curscreen.get_rect())
			# Call this to send whatever has been rendered on screen over to the monitor
			pygame.display.flip()

			#update inputs
			keyboardManager.update()
			mouseManager.update()
			gamepadManager.update()

			
		return "no more scenes"
		#raise self.SafeExit("no more scenes")

	def event_handler(self):
		"""Handles events from pygame"""

		for evt in pygame.event.get():
			if  (evt.type == pygame.QUIT):            return "Window closed."
			elif(evt.type == pygame.MOUSEBUTTONUP):   return mouseManager.up_event(evt)
			elif(evt.type == pygame.MOUSEBUTTONDOWN): return mouseManager.down_event(evt)
			elif(evt.type == pygame.KEYDOWN):         return keyboardManager.down_event(evt)
			elif(evt.type == pygame.KEYUP):           return keyboardManager.up_event(evt)
			elif(evt.type == pygame.JOYAXISMOTION):   return gamepadManager.axis_motion_event(evt)
			elif(evt.type == pygame.JOYBALLMOTION):   return gamepadManager.ball_motion_event(evt)
			elif(evt.type == pygame.JOYHATMOTION):    return gamepadManager.hat_motion_event(evt)
			elif(evt.type == pygame.JOYBUTTONUP):     return gamepadManager.button_up_event(evt)
			elif(evt.type == pygame.JOYBUTTONDOWN):   return gamepadManager.button_down_event(evt)
			elif(evt.type == pygame.VIDEORESIZE):     return self.resize_event(evt)

	def resize_event(self, evt):
		"""Called when the screen is resized."""
		size = evt.size
		#Log this event. It's a dangerous one.
		print("Screen resized to: ({}, {}).".format(size[0], size[1]))
		#TEMPORARY STUFFS
		engine.graphics.resize(size)
		#engine.screen_bounds = engine.graphics.interface.screen_bounds
		#engine.window_scale = engine.graphics.interface.window_scale
		#engine.window_bounds = engine.graphics.interface.window_bounds
		#print(engine.graphics.interface.window_scale)
		#update the display window size
		pygame.display.set_mode(size, pygame.RESIZABLE )
		#update (replace) scene screens
		for i in range(len(self.screens)):
			#resize the screens
			self.screens[i] = pygame.Surface(gameScreen.get_size(),pygame.SRCALPHA)
			#re-render the resized scenes
			self.scenes[i].render(self.screens[i])
