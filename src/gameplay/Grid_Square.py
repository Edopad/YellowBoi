from pygame.sprite import Sprite
import Dot

class Grid_Square(Sprite):
    
    def __init__(self, traverse):
        super.__init__(self)
        self.__textureID = None
        self.__traversible = traverse

    def tick(self):
        pass

class Path(Grid_Square):
    
    def __init__(self, traverse):
        super().__init__(self, traverse)
        self.__dot_instance = Dot()

    def tick(self):
        if self.__dot_instance.respawn_timer == 0 and self.__dot_instance.get_visible() == False:
            self.__dot_instance.respawn()
            self.__dot_instance.respawn_timer = 30
        elif self.__dot_instance.get_visible() == False:
            self.__dot_instance.respawn_timer -= 1

class Blockade(Grid_Square):
    
    def __init__(self, traverse):
        super().__init__(self, traverse)
        self.__wall_type = None