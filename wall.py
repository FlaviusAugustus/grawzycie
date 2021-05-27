import pygame
import colors


class Wall:

    alive = False

    def __init__(self, pos_x, pos_y, screen, settings):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.screen = screen
        self.settings = settings

    def draw(self):
        self.visual_repr = pygame.Rect(self.pos_x, self.pos_y, self.settings.block_size, self.settings.block_size)
        self.hitbox = pygame.Rect(self.pos_x, self.pos_y, self.settings.block_size + 5, self.settings.block_size + 5)
        pygame.draw.rect(self.screen, colors.white, self.visual_repr)