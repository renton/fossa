import pygame
from pygame.locals import *

DEFAULT_BACKGROUND_COLOUR = (0, 0, 0)

class State():
    def __init__(self, screen, prev_state = None):
        self.screen = screen
        self.ticks = 0
        self.set_prev_state(prev_state)
        self.fps = 0
        self.bg_colour = DEFAULT_BACKGROUND_COLOUR
        self.widgets = []

    def run_mainloop(self):
        self._draw()
        self._step()

    def _force_draw(self):
        self._draw()

    def _draw(self):
        self._before_draw()
        self.draw()
        self._after_draw()

    def _step(self):
        self._before_step()
        self.step()
        self._after_step()

    def _before_step(self):
        pass

    def step(self):
        self.ticks += 1

    def _after_step(self):
        pass

    def _before_draw(self):
        pass

    def draw(self):
        self.screen.fill(self.bg_colour)

    def draw_widgets(self):
        for widget in self.widgets:
            widget.draw(self.screen)

    def add_widget(self, widget):
        self.widgets.append(widget)

    def _after_draw(self):
        self.draw_widgets()
        pygame.display.flip()

    def set_fps(self, fps):
        self.fps = fps

    def input(self, im):
        if im.is_key_event(KEYDOWN, K_ESCAPE):
            if self.prev_state:
                self.close()

    def close(self):
        pygame.event.post(pygame.event.Event(SETTINGS['EVENT_CUSTOM_SWITCH_STATE'], loadstate = self.prev_state))

    def set_prev_state(self, state):
        self.prev_state = state
