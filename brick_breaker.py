# -*- coding: utf-8 -*-
"""
This is a worked example of applying the Model-View-Controller (MVC)
design pattern to the creation of a simple arcade game (in this case
Brick Breaker).

We will create our game in stages so that you can see the process by
which the MVC pattern can be utilized to create clean, extensible,
and modular code.

@author: SoftDesProfs
"""
import time
import pygame
from model import PianoModel
import model
from view import PyGameWindowView
from controller import PyGameKeyboardController


def start_game(size):
    """
    Given screen 'size' as (x,y) tuple, start BrickBreaker game
    """
    pygame.init()

    model1 = PianoModel(size)

    print(model1)

    view = PyGameWindowView(model1, size)
    controller = PyGameKeyboardController(model1)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                running = False
            controller.handle_event(event)
        model.update(0)
        view.draw()
        time.sleep(.001)

    pygame.quit()

if __name__ == '__main__':
    size = (375, 120)
    start_game(size)
