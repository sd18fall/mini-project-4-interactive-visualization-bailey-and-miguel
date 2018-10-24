"""
BrickBreaker controller code
"""
import time
import pygame.locals
import pygame.key
from view import PyGameWindowView as viewer
import view
import model
import blues_solo

#class PyGameMouseController(object):
    #""" A controller that uses the mouse to move the paddle """
    #def __init__(self,model):
        #self.model = model

   # def handle_event(self,event):
    #    """ Handle the mouse event so the paddle tracks the mouse position """
     #   if event.type == pygame.locals.MOUSEMOTION:
      #      self.model.key = event.pos[0] - self.model

class PyGameKeyboardController(object):
    """ Handles keyboard input for brick breaker """
    def __init__(self,model):
        self.model = model

    def handle_event(self,event):
        
        if event.type != pygame.locals.KEYDOWN:
            #view.PyGameWindowView.draw(255,255,255)
            return

        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_a:
                viewer.draw(255,255,0, 0)
                blues_solo.play_note(40, beats=1, bpm=30)
                time.sleep(.1)
                
            if event.key==pygame.K_s:
                viewer.draw(255,255,0, 1)
                blues_solo.play_note(43, beats=1, bpm=30)
                time.sleep(.1)
                
            if event.key==pygame.K_d:
                viewer.draw(255,255,0, 2)
                blues_solo.play_note(45, beats=1, bpm=30)
                time.sleep(.1)
                
            if event.key==pygame.K_f:
                viewer.draw(255,255,0, 3)
                blues_solo.play_note(46, beats=1, bpm=30)
                time.sleep(.1)
                
            if event.key==pygame.K_g:
                viewer.draw(255,255,0, 4)
                blues_solo.play_note(47, beats=1, bpm=30)
                time.sleep(.1)
            if event.key==pygame.K_h:
                viewer.draw(255,255,0, 5)
                blues_solo.play_note(50, beats=1, bpm=30)
                time.sleep(.1)
            if event.key==pygame.K_j:
                viewer.draw(255,255,0, 6)
                blues_solo.play_note(52, beats=1, bpm=30)
                time.sleep(.1)
            if event.key==pygame.K_k:
                viewer.draw(255,255,0, 7)
                blues_solo.play_note(55, beats=1, bpm=30)
                time.sleep(.1) 
            if event.key==pygame.K_l:
                viewer.draw(255,255,0, 8)
                blues_solo.play_note(57, beats=1, bpm=30)
                time.sleep(.1)
            if event.key==pygame.K_z:
                viewer.draw(255,255,0, 9)
                blues_solo.play_note(58, beats=1, bpm=30)
                time.sleep(.1)
            if event.key==pygame.K_x:
                viewer.draw(255,255,0, 10)
                blues_solo.play_note(59, beats=1, bpm=30)
                time.sleep(.1)
            if event.key==pygame.K_c:
                viewer.draw(255,255,0, 11)
                blues_solo.play_note(62, beats=1, bpm=30)
                time.sleep(.1)
            if event.key==pygame.K_v:
                viewer.draw(255,255,0, 12)
                blues_solo.play_note(64, beats=1, bpm=30)
                time.sleep(.1)
            if event.key==pygame.K_b:
                viewer.draw(255,255,0, 13)
                blues_solo.play_note(67, beats=1, bpm=30)
                time.sleep(.1)
            if event.key==pygame.K_n:
                viewer.draw(255,255,0, 14)
                blues_solo.play_note(69, beats=1, bpm=30)
                time.sleep(.1)
            if event.key==pygame.K_m:
                viewer.draw(255,255,0, 15)
                blues_solo.play_note(70, beats=1, bpm=30)
                time.sleep(.1)
                
def get_pygame_events():
    pygame_events=pygame.event.get()
    return pygame_events