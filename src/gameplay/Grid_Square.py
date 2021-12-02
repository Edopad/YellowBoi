from pygame.sprite import Sprite
import Dot

class Grid_Square(Sprite):
    
    def __init__(self, x, y):
        super().__init__(x, y, 30, 30)
        self.__textureID = None

class Path(Grid_Square):
    
    def __init__(self):
        super().__init__()
        self.__dot_instance = Dot()

class Blockade(Grid_Square):
    
    def __init__(self):
        super().__init__()
        pass