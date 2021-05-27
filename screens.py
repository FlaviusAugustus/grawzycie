import pygame
import utils


class Screen:

    def __init__(self, screen, Button, settings):
        self.screen = screen
        self.Button = Button
        self.settings = settings

    def settings_screen(self):
        utils.clear_screen(self.screen)
        visible = True
        small_button = self.Button(self.settings.window_width // 2, self.settings.window_height // 2, 300, 75, (255, 255, 255), (220, 220, 220),
                                   "5", 50, (255, 255, 255), self.screen)
        normal_button = self.Button((self.settings.window_width // 2) + 350, self.settings.window_height // 2, 300, 75, (255, 255, 255),
                                    (220, 220, 220), "10", 50, (255, 255, 255), self.screen)
        big_button = self.Button((self.settings.window_width // 2) - 350, self.settings.window_height // 2, 300, 75, (255, 255, 255), (220, 220, 220),
                                 "25", 50, (255, 255, 255), self.screen)

        buttons = [small_button, normal_button, big_button]
        for button in buttons:
            button.create()

        if self.settings.block_size_name == "small":
            small_button.is_chosen = True
        if self.settings.block_size_name == "normal":
            normal_button.is_chosen = True
        if self.settings.block_size_name == "big":
            big_button.is_chosen = True

        while visible:

            for button in buttons:
                button.show_chosen()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    visible = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if small_button.button.collidepoint(pygame.mouse.get_pos()):
                        self.settings.block_size_name = "small"
                        small_button.is_chosen = True
                        normal_button.is_chosen = False
                        big_button.is_chosen = False

                    elif normal_button.button.collidepoint(pygame.mouse.get_pos()):
                        self.settings.block_size_name = "normal"
                        small_button.is_chosen = False
                        normal_button.is_chosen = True
                        big_button.is_chosen = False

                    elif big_button.button.collidepoint(pygame.mouse.get_pos()):
                        self.settings.block_size_name = "big"
                        small_button.is_chosen = False
                        normal_button.is_chosen = False
                        big_button.is_chosen = True

                elif event.type == pygame.MOUSEMOTION:

                    for button in buttons:
                        button.blink_on_hover()

            gamemode_text, text_rect_1 = utils.display_message("Block Size", 50, (self.settings.window_width // 2, (self.settings.window_height // 2) - 120))

            self.screen.blit(gamemode_text, text_rect_1)
            pygame.display.update()