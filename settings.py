import utils
import pygame
import math


class Settings:

    window_width = 1450
    window_height = 1050
    block_size_name = "normal"
    running = True
    generation = 0
    step = 1
    manual = False

    def __init__(self, block_size):
        self.block_size = block_size

    def set_block_size(self):
        if self.block_size_name == "small":
            self.block_size = 5
        elif self.block_size_name == "normal":
            self.block_size = 10
        elif self.block_size_name == "big":
            self.block_size = 25

    def display_hud(self, surf, screen, grid):
        surf.fill((0, 0, 0))
        message_1, text_rect_1 = utils.display_message("Generation:", 20, (125, 20))
        message_2, text_rect_2 = utils.display_message(f"{grid.generation}", 20, (230, 20))
        message_3, text_rect_3 = utils.display_message("Blocks alive:", 20, (125, 50))
        message_4, text_rect_4 = utils.display_message(f"{grid.blocks_alive}",20, (230, 50))
        message_5, text_rect_5 = utils.display_message("Manual:", 20, (125, 80))
        message_6, text_rect_6 = utils.display_message(f"{self.manual}", 20, (230, 80))
        surf.blit(message_1, text_rect_1)
        surf.blit(message_2, text_rect_2)
        surf.blit(message_3, text_rect_3)
        surf.blit(message_4, text_rect_4)
        surf.blit(message_5, text_rect_5)
        surf.blit(message_6, text_rect_6)

        screen.blit(surf, (0, self.window_height-200))
        pygame.display.update()

    def manual_control(self, grid, history):
        while self.manual:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    quit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        self.step = 1
                        return

                    elif event.key == pygame.K_f:
                        self.step = 10
                        return

                    elif event.key == pygame.K_a:
                        history.previous_grid(10)
                        return

                    elif event.key == pygame.K_s:
                        history.previous_grid(1)
                        return

                    elif event.key == pygame.K_t:
                        grid.save()
                        return

                    elif event.key == pygame.K_m:
                        self.manual = False


#funkcja skrotu md5/sha256. Aktualny stan skracac i w programie odtwarzac