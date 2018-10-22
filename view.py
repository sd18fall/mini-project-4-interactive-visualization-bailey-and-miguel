"""
BrickBreaker view code
"""

import pygame
import model

class PyGameWindowView(object):
    """ A view of piano rendered in a Pygame window """
    def __init__(self, model, size):
        """ Initialize the view with a reference to the model and the
            specified game screen dimensions (represented as a tuple
            containing the width and height """
        self.model = model
        self.screen = pygame.display.set_mode(size)

    def draw(self, colora, colorb, colorc, num=None):
        """ Draw the current game state to the screen """
        self.screen.fill(pygame.Color(255,0,0))

        for key in model.keys:
            if num is None:
                pygame.draw.rect(self.screen,
                             pygame.Color(255, 255, 255),
                             pygame.Rect(key.x,
                                         key.y,
                                         key.width,
                                         key.height))
                pygame.display.update()

            elif key==model.keys[num]:
                pygame.draw.rect(self.screen,
                                 pygame.Color(colora, colorb, colorc),
                                 pygame.Rect(key.x,
                                             key.y,
                                             key.width,
                                             key.height))
                pygame.display.update()

            else:
                #pygame.draw.rect(self.screen,
                            # pygame.Color(255, 255, 255),
                             #pygame.Rect(key.x,
                                        # key.y,
                                         #key.width,
                                         #key.height))
                                    
                    pygame.display.update()
