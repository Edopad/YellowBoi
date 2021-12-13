from pygame import Color
from pygame.font import Font, SysFont



class ApplicationTheme:
	def __init__(self):
		"""When object is initialized, create default colors and fonts."""
		
		#set default color and font scheme
		
		self.ui_button_normal_text_font             = SysFont('Calibri', 18, bold = False, italic = False)
		self.ui_button_normal_text_color            = Color(255, 255, 255)
		self.ui_button_normal_background_color      = Color(  0,   0,   0)
		self.ui_botton_normal_border_color          = Color(255, 255, 255)
		
		self.ui_button_highlighted_text_font        = SysFont('Calibri', 18, bold = True,  italic = False)
		self.ui_button_highlighted_text_color       = Color(255, 255, 255)
		self.ui_button_highlighted_background_color = Color(  0,   0,   0)
		self.ui_botton_highlighted_border_color     = Color(255, 255, 255)
		
		self.ui_button_active_text_font             = SysFont('Calibri', 18, bold = True,  italic = False)
		self.ui_button_active_text_color            = Color(255, 255, 255)
		self.ui_button_active_background_color      = Color(  0,   0,   0)
		self.ui_botton_active_border_color          = Color(255, 255, 255)
		
		#title text in the Main Menu Scene
		self.ui_title_text_font                     = SysFont('Calibri', 48, bold = False, italic = False)
		self.ui_title_text_color                    = Color(255, 255, 255)
		
		#text in the credits Scene
		self.ui_credits_text_font                   = SysFont('Calibri', 48, bold = False, italic = False)
		self.ui_credits_text_color                  = Color(255, 255, 255)
		
		#gameplay background color
		self.gameplay_bg_color = Color(7, 3, 44)
	
	def load_from_file(self, filename):
		pass
