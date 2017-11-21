from __future__ import print_function
from __future__ import division

import sys
import pygame

pygame.init()

from pygame.locals import *
from src import Fossa, CanvasState, Game


fossa = Fossa()

game = Game()
canvas_state = CanvasState(game.screen)
game.set_start_state(canvas_state)


game.mainloop()
