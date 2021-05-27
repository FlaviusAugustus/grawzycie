import pygame
import colors
import math
from settings import Settings
from block import Block
from wall import Wall
from grid import Grid
from screens import Screen
from button import Button
from history import History
import utils


pygame.init()
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()

settings = Settings(10)
screen = Screen(pygame.display.set_mode((settings.window_width, settings.window_height)), Button, settings)
hud_surface = pygame.surface.Surface((settings.window_width, 300))
grid = Grid(settings, screen.screen, Block, Wall)
history = History(grid, settings)

grid.create_grid()

while settings.running:

    settings.display_hud(hud_surface, screen.screen, grid)
    settings.set_block_size()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                screen.settings_screen()
                settings.set_block_size()
                grid.create_grid()

            elif event.key == pygame.K_g:
                grid.draw_glider()

            elif event.key == pygame.K_m:
                settings.manual = True

            elif event.key == pygame.K_s:
                grid.create_blocks_state()
                grid.save()

            elif event.key == pygame.K_r:
                grid.blocks_state = grid.read()
                grid.update_grid()

            elif event.key == pygame.K_SPACE:
                playing = True
                if not grid.blocks_state:
                    grid.create_blocks_state()

                while playing:

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            settings.running = False
                            quit()

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                grid.generation = 0
                                playing = False
                                utils.clear_screen(screen.screen)
                                grid.create_grid()

                            elif event.key == pygame.K_m:
                                if settings.manual:
                                    settings.manual = False
                                else:
                                    settings.manual = True

                            elif event.key == pygame.K_d:
                                step = 1

                            elif event.key == pygame.K_f:
                                step = 10

                    settings.display_hud(hud_surface, screen.screen, grid)

                    if settings.manual:
                        settings.manual_control(grid, history)

                    for i in range(int(math.fabs(settings.step))):
                        history.history.append(grid.blocks_state)
                        grid.blocks_state = grid.calculate_grid(grid.blocks_state)

                    history.manage_history()

                    grid.generation += settings.step
                    grid.update_grid()
                    clock.tick_busy_loop(10)

    grid.beginning_state()
    pygame.display.update()
    clock.tick_busy_loop(120)

# bugfixy: dodatkowy blok zamalowany przy wstawianiu glidera

# 40 0,38 1,40 1,30 0,2 1 <-- zapisywanie plikow w ten sposob
# uzytkownik moze zdefiniowac do jakiej generacji chce przejsc


