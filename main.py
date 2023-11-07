import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Config
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
TILL_SIZE = 32
ROWS = WINDOW_HEIGHT // TILL_SIZE
COLS = WINDOW_WIDTH // TILL_SIZE
GRID = [[0 for _ in range(COLS)] for _ in range(ROWS)]


class Generator():
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Dungeons Generator")
        self.new_map(10, 0)
        self.main_loop()

    def new_map(self, path_length, side_rooms):
        self.screen.fill((255, 255, 255))
        column = 8
        row = 8
        for n in range(path_length):
            while True:
                direction = random.randint(0, 3)
                if direction == 0:
                    column -= 1
                elif direction == 1:
                    row -= 1
                elif direction == 2:
                    column += 1
                elif direction == 3:
                    row += 1

                if GRID[row][column]:
                    continue
                else:
                    GRID[row][column] = 1
                    break

            pygame.draw.rect(self.screen, (0,0,0), (column * TILL_SIZE, row * TILL_SIZE, TILL_SIZE, TILL_SIZE))
        pygame.display.flip()


    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


if __name__ == "__main__":
    Generator()