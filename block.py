import pygame
import colors


class Block:

    alive = False
    alive_color = colors.black
    dead_color = colors.white
    neighbour_count = 0
    grid = False

    def __init__(self, pos_x, pos_y, screen, settings):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.screen = screen
        self.settings = settings

    def create(self):
        self.visual_repr = pygame.Rect(self.pos_x, self.pos_y, self.settings.block_size, self.settings.block_size)
        self.hitbox = pygame.Rect(self.pos_x, self.pos_y, self.settings.block_size+5, self.settings.block_size+5)

    def draw(self):
        if self.alive:
            pygame.draw.rect(self.screen, self.alive_color, self.visual_repr)
        else:
            pygame.draw.rect(self.screen, self.dead_color, self.visual_repr)
            # pygame.draw.rect(self.screen, self.alive_color, self.visual_repr)