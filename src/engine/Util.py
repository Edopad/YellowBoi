
#def get_asset_path(relative_path):
#	return os.path.join(relative_path)

import pygame
import os

__loaded_spritemaps = {}

def load_image(*args):
	"""Returns a pygame Surface with the image requested by a path."""
	path = os.path.join("../", "assets", "pictures", *args)
	try:
		image = pygame.image.load(path)
		return image
	except FileNotFoundError as error:
		print("[WARN] Requested image at location \"" + path + "\", but file not found! Using blank tile instead.")
		return pygame.Surface((16, 16), flags = pygame.HWSURFACE | pygame.SRCALPHA)
	

def load_spritemap(name):
	"""Creates a spritemap or loads a reference to an existing one."""
	#return a reference to the desired spritemap if it already exists
	result = __loaded_spritemaps.get(name)
	if result:
		return result
	
	#create the desired spritemap (this should only execute once per spritemap)
	if name == "board_tiles_2x":
		#generate spritemap for board tiles
		#load seperate line pieces
		tile_bases = [
			load_image("board", "L_line_2x.png"),\
			load_image("board", "L2L_curve_outer_2x.png"),\
			load_image("board", "L2L_curve_inner_2x.png"),\
			load_image("board", "D_line_2x.png"),\
			load_image("board", "D2D_curve_outer_2x.png"),\
			load_image("board", "D2D_curve_inner_2x.png"),\
			load_image("board", "DLD_branch_2x.png"),\
			pygame.transform.rotate(pygame.transform.flip(load_image("board", "DLD_branch_2x.png"), False, True), -90),\
			load_image("board", "D2D_square_outer_2x.png")\
		]
		
		#create a blank spritemap with the desired size
		result = pygame.Surface((4 * 16, 9 * 16), flags = pygame.HWSURFACE | pygame.SRCALPHA)
		
		#populate the spritemap with various rotations of the tiles
		for y in range(0, len(tile_bases)):
			tile_piece = tile_bases[y]
			for x in range(0, 4):
				result.blit(pygame.transform.rotate(tile_piece, x * -90), pygame.Rect(x * 16, y * 16, 16, 16), pygame.Rect(0,0,16,16))
	else:
		print("[WARN] The spritemap \"" + name + "\" was requested, but it has no generation function!")
	
	#protect the result in video memory
	result.lock()
	#add the created spritemap to the map of existing spritemaps, and return the result
	__loaded_spritemaps[name] = result
	return result