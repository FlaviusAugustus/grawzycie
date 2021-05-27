import math
import random
import pygame
import colors


def clear_screen(screen):
    screen.fill(colors.black)


def display_message(text, size, pos):
    text_parameters = pygame.font.Font("freesansbold.ttf", size)
    message = text_parameters.render(text, True, colors.white)
    text_rect = message.get_rect()
    text_rect.center = pos

    return message, text_rect