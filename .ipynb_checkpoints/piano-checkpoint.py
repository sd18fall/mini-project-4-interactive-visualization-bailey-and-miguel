# -*- coding: utf-8 -*-
"""This is a piano app that uses the a to l keys and z to m keys to play notes. 
@authors: bwolfe1, miguelii44
"""
import time
import pygame
from model import PianoModel
from model import update as UPDATE
from view import PyGameWindowView
import view
from controller import PyGameKeyboardController


def start_game(size):
    """
    Given screen 'size' as (x,y) tuple, start piano model
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
        PyGameWindowView.draw()
        time.sleep(.001)

    pygame.quit()

if __name__ == '__main__':
    size = (375, 120)
    start_game(size)
