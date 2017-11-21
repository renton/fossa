import sys
import os

import pygame
from pygame.locals import *

from src.system.inputmanager import im

DEFAULT_FPS     = 60
FULLSCREEN_MODE = False
WINDOW_X_SIZE   = 800
WINDOW_Y_SIZE   = 600
WINDOW_CAPTION  = 'Game'

EVENT_CUSTOM_SWITCH_STATE = USEREVENT + 2
EVENT_CUSTOM_CREATE_STATE = USEREVENT + 3

WINDOW_POS_X = 2800
WINDOW_POS_Y = 0

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (WINDOW_POS_X, WINDOW_POS_Y)

class Game():
    def __init__(self):
        # init game time
        self.clock = pygame.time.Clock()
        self.fps = DEFAULT_FPS
        self.playtime = 0.0

        # init screen
        flags = pygame.FULLSCREEN if FULLSCREEN_MODE else 0
        self.screen = pygame.display.set_mode((WINDOW_X_SIZE, WINDOW_Y_SIZE), flags)
        pygame.display.set_caption(WINDOW_CAPTION)

        # init mouse
        self.mouse_x, self.mouse_y = (0, 0)

        self.cur_state = None

    def set_start_state(self, state):
        self._set_cur_state(state)

    def _set_cur_state(self, state):
        self.cur_state = state

    # TODO pass custom state class here
    def _evoke_new_state(self, state):
        self._set_cur_state(State(self.screen, self.p1))

    def mainloop(self):
        while(1):
          # do not go faster than the framerate
          msec = self.clock.tick(self.fps)
          self.playtime += msec / 1000.0

          # reset im key events
          im.reset_events()
          self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

          # handle events
          for event in pygame.event.get():
            if event.type == EVENT_CUSTOM_SWITCH_STATE:
                self._set_cur_state(event.loadstate)
            if event.type == EVENT_CUSTOM_CREATE_STATE:
                self._evoke_new_state(event.createstate)
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                im.set_key_event(event.type, event.key)
            if event.type == pygame.JOYBUTTONDOWN:
                im.set_joy_button_event(event.type, event.button)
            if event.type == pygame.MOUSEBUTTONDOWN:
                im.set_mouse_event(event.type, event.button)

          # let state handle input
          im.update()
          self.cur_state.input(im)

          keystate = pygame.key.get_pressed()

          # emergency exit
          if keystate[K_q] and (keystate[K_LCTRL] or keystate[K_RCTRL]):
              pygame.display.quit()
              sys.exit()

          if keystate[K_F1]:
              self.cur_state = self.tooltilesetviewstate
              self.cur_state._force_draw()

          self.cur_state.set_fps(self.clock.get_fps())
          self.cur_state.run_mainloop()
