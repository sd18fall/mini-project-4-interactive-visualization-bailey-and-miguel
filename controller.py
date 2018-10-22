"""
BrickBreaker controller code
"""

import pygame.locals
from view import PyGameWindowView as viewer
import view
import model

class PyGameMouseController(object):
    """ A controller that uses the mouse to move the paddle """
    def __init__(self,model):
        self.model = model

    def handle_event(self,event):
        """ Handle the mouse event so the paddle tracks the mouse position """
        if event.type == pygame.locals.MOUSEMOTION:
            self.model.key = event.pos[0] - self.model

class PyGameKeyboardController(object):
    """ Handles keyboard input for brick breaker """
    def __init__(self,model):
        self.model = model

    def handle_event(self,event):
        """ Left and right presses modify the x velocity of the paddle """
        keys_pressed= get_pygame_events()
        for event in keys_pressed:
            
            if event.type != pygame.locals.KEYDOWN:
                view.draw(255,255,255)
                return

            if event.type == pygame.KEYDOWN:
                if event.key==K_a:
                    view.draw(255,255,0, 0)
                    time.sleep(.1)
                
def get_pygame_events():
    pygame_events=pygame.event.get()
    return pygame_events