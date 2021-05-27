import pygame


class Button:

    is_chosen = False

    def __init__(self, pos_x, pos_y, width, height, color, color_on_hover, text, text_size, text_color, screen):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.color = color
        self.color_on_hover = color_on_hover
        self.text = text
        self.text_size = text_size
        self.text_color = text_color

        self.screen = screen

    def create(self):
        self.button = pygame.Rect(self.pos_x - self.width / 2, self.pos_y, self.width, self.height)
        pygame.draw.rect(self.screen, self.color, self.button)

        text_parameters = pygame.font.Font("freesansbold.ttf", self.text_size)
        message = text_parameters.render(self.text, True, self.text_color)
        text_rect = message.get_rect()
        text_rect.midbottom = (self.pos_x, self.pos_y)
        self.screen.blit(message, text_rect)

        pygame.display.update(self.button)

    def blink_on_hover(self):
        if not self.is_chosen:
            if self.button.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.screen, self.color_on_hover, self.button)
            if not self.button.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                pygame.draw.rect(self.screen, self.color, self.button)
            pygame.display.update(self.button)

    def show_chosen(self):
        if self.is_chosen:
            pygame.draw.rect(self.screen, self.color_on_hover, self.button)
            pygame.display.update(self.button)