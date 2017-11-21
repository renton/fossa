import sys
import pygame

from src.states import State

class CanvasState(State):

    WINDOW_CAPTION  = 'Fossa Canvas'

    def __init__(self, screen):
        State.__init__(self, screen)
