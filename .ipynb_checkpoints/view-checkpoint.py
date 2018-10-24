"""
BrickBreaker view code
"""

import pygame
import model
screen = pygame.display.set_mode((375, 120))
class PyGameWindowView(object):
    """ A view of piano rendered in a Pygame window """
    def __init__(self, model, size):
        """ Initialize the view with a reference to the model and the
            specified game screen dimensions (represented as a tuple
            containing the width and height """
        self.model = model
        

    def draw(colora=255, colorb=255, colorc=255, num=None):
        """ Draw the current game state to the screen """
        
        
        #self.screen.fill(pygame.Color(255,0,0))
        
        if num is None:
            for key in model.keys:
                pygame.draw.rect(screen,
                             pygame.Color(255, 255, 255),
                             pygame.Rect(key.x,
                                         key.y,
                                         key.width,
                                         key.height))
            pygame.display.update()
        else:
            for key in model.keys:
                if key==model.keys[num]:
                    pygame.draw.rect(screen,
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
