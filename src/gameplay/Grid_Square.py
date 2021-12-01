from pygame import Rect
import Dot

class Grid_Square(Rect):
    
    def __init__(self, x, y):
        super().__init__(x, y, 30, 30)
        self.__textureID = 0

class Path(Grid_Square):
    
    def __init__(self):
        super().__init__()
        self.__dot_instance = Dot()

class Blockade(Grid_Square):
    
    def __init__(self):
        super().__init__()
        pass