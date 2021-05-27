import pygame
import colors


class Grid:

    blocks = []
    blocks_state = []
    generation = 0
    blocks_alive = 0

    def __init__(self, settings, screen, Block, Wall):
        self.settings = settings
        self.screen = screen
        self.Block = Block
        self.Wall = Wall

    def create_grid(self):

        self.blocks = []

        for x in range(self.settings.window_width // self.settings.block_size):
            row = []
            for y in range((self.settings.window_height-200) // self.settings.block_size):

                if y == 0 or y == ((self.settings.window_height-200) // self.settings.block_size) -1 or x == 0 or x == (self.settings.window_width // self.settings.block_size) -1:
                    row.append(self.Wall(x * self.settings.block_size, y * self.settings.block_size, self.screen, self.settings))
                    continue

                block = self.Block(x * self.settings.block_size, y * self.settings.block_size, self.screen, self.settings)
                block.create()

                row.append(block)

                pygame.draw.rect(self.screen, colors.white, block.visual_repr, 1)
            self.blocks.append(row)
        pygame.display.update()

        self.update_grid()

    def create_blocks_state(self):
        self.blocks_state = []
        row = []
        for i in self.blocks:
            for block in i:
                if isinstance(block, self.Wall):
                    row.append(None)
                elif isinstance(block, self.Block):
                    row.append(block.alive)
            self.blocks_state.append(row)
            row = []

    def update_grid(self):
        for i_1, row in enumerate(self.blocks_state):
            for i_2, block_state in enumerate(row):
                if block_state is None:
                    self.blocks[i_1][i_2] = block_state
                else:
                    self.blocks[i_1][i_2].alive = block_state

        self.blocks_alive = 0
        for row in self.blocks:
            for block in row:
                if block is not None:
                    block.draw()
                    if block.alive:
                        self.blocks_alive += 1

    def print_blocks(self):
        print(self.blocks)

    def draw_glider(self):
        placed = False
        while not placed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.settings.running = False
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x = (pygame.mouse.get_pos()[0]//self.settings.block_size)
                    mouse_y = (pygame.mouse.get_pos()[1]//self.settings.block_size)

                    glider = [self.blocks[mouse_x-1][mouse_y-1],
                              self.blocks[mouse_x][mouse_y-1],
                              self.blocks[mouse_x+1][mouse_y-1],
                              self.blocks[mouse_x-1][mouse_y],
                              None,
                              None,
                              None,
                              self.blocks[mouse_x][mouse_y+1],
                              None,
                              ]

                    for glider_element in glider:
                        if glider_element is not None:
                            glider_element.alive = True
                            glider_element.draw()
                            pygame.display.update()

                    placed = True

    def find_block(self, pos):
        for row in self.blocks:
            for block in row:
                if block.visual_repr.collidepoint(pos):
                    return block

    def calculate_grid(self, grid):
        updated_grid = []
        updated_row = []
        for i_1, row in enumerate(grid):
            for i_2, block in enumerate(row):

                neighbour_count = 0
                if block is None:
                    updated_row.append(block)
                    continue

                neighbours = [grid[i_1][i_2 - 1], grid[i_1][i_2 + 1], grid[i_1 - 1][i_2 - 1],
                              grid[i_1 + 1][i_2 - 1], grid[i_1 + 1][i_2], grid[i_1 - 1][i_2],
                              grid[i_1 + 1][i_2 + 1], grid[i_1 - 1][i_2 + 1]]

                for neighbour in neighbours:
                    if isinstance(neighbour, self.Wall):
                        continue
                    elif neighbour:
                        neighbour_count += 1

                if neighbour_count in (2, 3) and block:
                    updated_row.append(True)

                elif neighbour_count not in (2, 3) and block:
                    updated_row.append(False)

                elif not block and neighbour_count == 3:
                    updated_row.append(True)

                else:
                    updated_row.append(False)

            updated_grid.append(updated_row)
            updated_row = []

        return updated_grid

    def beginning_state(self):
        left_mouse_button = pygame.mouse.get_pressed(3)[0]
        right_mouse_button = pygame.mouse.get_pressed(3)[2]
        if left_mouse_button or right_mouse_button:
            try:
                block = self.find_block(pygame.mouse.get_pos())
                if left_mouse_button:
                    block.alive = True
                elif right_mouse_button:
                    block.alive = False
                block.draw()
            except AttributeError:
                pass

    def save(self):
        save_file = open("save", "a")
        save_file.truncate(0)
        for row in self.blocks_state:
            for i, element in enumerate(row):
                if element is None:
                    save_file.write("2")
                    continue

                if i == 1:
                    previous_element = int(element)
                    element_count = 0
                else:
                    previous_element = int(row[i-1])

                if previous_element == element:
                    element_count += 1

                elif previous_element != element or i == (len(row) - 1):
                    save_file.write(f"{element_count}, {previous_element} ")
                    element_count = 1

                if i == (len(row) - 1):
                    save_file.write(f"{element_count}, {int(element)} ")

            save_file.write("\n")
        save_file.close()

    def read(self):
        blocks_state = []
        save_file = open("save", "r")
        for line in save_file.readlines():
            row = []
            for word in line.split():
                if word == "0":
                    row.append(False)
                elif word == "1":
                    row.append(True)
                elif word == "2":
                    row.append(None)
            blocks_state.append(row)

        return blocks_state

