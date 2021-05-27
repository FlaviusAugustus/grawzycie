import math
import pygame


class History:

    size = 50
    history = []

    def __init__(self, grid, settings):
        self.grid = grid
        self.settings = settings

    def stop_playing(self):
        if len(self.history) > 2:
            if self.history[-2] == self.grid.blocks_state:
                self.grid.generation -= 2
                self.settings.manual = True

    def adjust_size(self):
        if len(self.history) > 50:
            self.history = self.history[-50::]

    def previous_grid(self, step):
        if len(self.history) > step:
            self.settings.step = -step
            for i in range(step):
                self.history.pop()
            self.grid.blocks_state = self.history.pop()
            pygame.display.flip()

    def manage_history(self):
        self.stop_playing()
        self.adjust_size()

