"""
BrickBreaker controller code
"""

import pygame.locals
from view import PyGameWindowView

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

        if event.type != pygame.locals.KEYDOWN:
            return

        if event.key == pygame.K_a.KEYDOWN:
            model.key.name[0] = color(255,255,0)

            model.update(0)
            time.sleep(.1)
