
#def get_asset_path(relative_path):
#	return os.path.join(relative_path)

import pygame
import os

def load_image(*args):
	"""Returns a pygame Surface with the image requested by a path."""
	path = os.path.join("../", "assets", "pictures", *args)
	image = pygame.image.load(path)
	return image
