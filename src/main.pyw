from engine import Application
from scenes import MainMenuScene



def main():
	#Create the primary application instance.
	app = Application()
	
	#Set properties of the application to be run.
	app.target_fps = 60
	app.window_caption = "Yellow Boi"
	app.window_icon = None
	
	#Run the application, with initial scene being the Main Menu scene, and resolution of 720p.
	app.run( \
		initial_scene = MainMenuScene(), \
		starting_window_size = (1280, 720) \
	)



#Run main function if this thread is the primary one.
if __name__ == "__main__":
	main()
	exit()
