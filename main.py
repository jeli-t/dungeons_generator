import pygame
import sys
import random
from pygame.math import Vector2

# Initialize Pygame
pygame.init()

# Config
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 960
TILL_SIZE = 64
TILL_COLOR = (160, 160, 160)
WALL_THICKNES = 5
WALL_COLOR = (90, 90, 90)
MIN_PATH = 4
MAX_PATH = 20
MIN_ROOMS = 0
MAX_ROOMS = 20


class Room():
    def __init__(self, x, y):
        self.position = Vector2(x, y)
        self.left_door = True
        self.top_door = True
        self.right_door = True
        self.bottom_door = True


class Map():
    def __init__(self):
        self.rooms = []
        self.walls = []
        self.x_offset = 6 * TILL_SIZE
        self.y_offset = 6 * TILL_SIZE

    def init_walls(self):
        self.walls = []
        for room in self.rooms:
            if room.left_door:
                wall_1 = pygame.Rect(room.position.x * TILL_SIZE + self.x_offset, room.position.y * TILL_SIZE + self.y_offset, WALL_THICKNES, TILL_SIZE / 4 + WALL_THICKNES)
                wall_2 = pygame.Rect(room.position.x * TILL_SIZE + self.x_offset, room.position.y * TILL_SIZE + self.y_offset + 3 * (TILL_SIZE / 4), WALL_THICKNES, TILL_SIZE / 4)
                self.walls.append(wall_1)
                self.walls.append(wall_2)
            else:
                wall = pygame.Rect(room.position.x * TILL_SIZE + self.x_offset, room.position.y * TILL_SIZE + self.y_offset, WALL_THICKNES, TILL_SIZE)
                self.walls.append(wall)
            if room.top_door:
                wall_1 = pygame.Rect(room.position.x * TILL_SIZE + self.x_offset, room.position.y * TILL_SIZE + self.y_offset, TILL_SIZE / 4 + WALL_THICKNES, WALL_THICKNES)
                wall_2 = pygame.Rect(room.position.x * TILL_SIZE + self.x_offset + 3 * (TILL_SIZE / 4), room.position.y * TILL_SIZE + self.y_offset, TILL_SIZE / 4, WALL_THICKNES)
                self.walls.append(wall_1)
                self.walls.append(wall_2)
            else:
                wall = pygame.Rect(room.position.x * TILL_SIZE + self.x_offset, room.position.y * TILL_SIZE + self.y_offset, TILL_SIZE, WALL_THICKNES)
                self.walls.append(wall)
            if room.right_door:
                wall_1 = pygame.Rect(room.position.x * TILL_SIZE + self.x_offset + TILL_SIZE, room.position.y * TILL_SIZE + self.y_offset, WALL_THICKNES, TILL_SIZE / 4 + WALL_THICKNES)
                wall_2 = pygame.Rect(room.position.x * TILL_SIZE + self.x_offset + TILL_SIZE, room.position.y * TILL_SIZE + self.y_offset + 3 * (TILL_SIZE / 4), WALL_THICKNES, TILL_SIZE / 4)
                self.walls.append(wall_1)
                self.walls.append(wall_2)
            else:
                wall = pygame.Rect(room.position.x * TILL_SIZE + self.x_offset + TILL_SIZE, room.position.y * TILL_SIZE + self.y_offset, WALL_THICKNES, TILL_SIZE)
                self.walls.append(wall)
            if room.bottom_door:
                wall_1 = pygame.Rect(room.position.x * TILL_SIZE + self.x_offset, room.position.y * TILL_SIZE + self.y_offset + TILL_SIZE, TILL_SIZE / 4 + WALL_THICKNES, WALL_THICKNES)
                wall_2 = pygame.Rect(room.position.x * TILL_SIZE + self.x_offset + 3 * (TILL_SIZE / 4), room.position.y * TILL_SIZE + self.y_offset + TILL_SIZE, TILL_SIZE / 4 + WALL_THICKNES, WALL_THICKNES)
                self.walls.append(wall_1)
                self.walls.append(wall_2)
            else:
                wall = pygame.Rect(room.position.x * TILL_SIZE + self.x_offset, room.position.y * TILL_SIZE + self.y_offset + TILL_SIZE, TILL_SIZE + WALL_THICKNES, WALL_THICKNES)
                self.walls.append(wall)

    def draw(self, screen):
        for room in self.rooms:
            pygame.draw.rect(screen, TILL_COLOR, (room.position.x * TILL_SIZE + self.x_offset, room.position.y * TILL_SIZE + self.y_offset, TILL_SIZE, TILL_SIZE))
        for wall in self.walls:
            pygame.draw.rect(screen, WALL_COLOR, wall)


class Generator():
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Dungeons Generator")
        self.font = pygame.font.Font(None, 24)
        self.map = Map()
        self.path_length = 10
        self.side_rooms = 6
        self.slider1_in_use = False
        self.slider2_in_use = False
        self.generate_button = pygame.Rect(20, 130, 100, 30)
        self.new_map(self.path_length, self.side_rooms)
        self.main_loop()


    def new_map(self, path_length, side_rooms):
        self.map.rooms = []
        x_index = 1
        y_index = 1
        previous_room = 'left'
        self.map.rooms.append(Room(x_index, y_index))

        for n in range(path_length - 1):
            while True:
                direction = random.choice(['left', 'right', 'up', 'down'])
                if direction == previous_room:
                    continue
                elif direction == 'left':
                    x_index -= 1
                    previous_room = 'right'
                elif direction == 'right':
                    x_index += 1
                    previous_room = 'left'
                elif direction == 'up':
                    y_index -= 1
                    previous_room = 'down'
                elif direction == 'down':
                    y_index += 1
                    previous_room = 'up'

                new_room = Room(x_index, y_index)

                already_exists = False
                for room in self.map.rooms:
                    if room.position == new_room.position:
                        already_exists = True
                        break

                if already_exists:
                    continue
                else:
                    self.map.rooms.append(new_room)
                    break

        self.map.init_walls()


    def render(self):
        self.screen.fill((255, 255, 255))

        # render map
        self.map.draw(self.screen)

        # render menu
        pygame.draw.rect(self.screen, (200,200,200), (0, 0, 240, 180))
        text = self.font.render(f"Path length: {self.path_length}", True, (0,0,0))
        self.screen.blit(text, (20, 20))
        pygame.draw.rect(self.screen, (100,100,100), (20, 40, 200, 20))
        button_x = int(20 + (self.path_length - MIN_PATH) / (MAX_PATH - MIN_PATH) * 200 - 20 / 2)
        pygame.draw.rect(self.screen, (0,0,0), (button_x, 40, 20, 20))
        text = self.font.render(f"Side rooms: {self.side_rooms}", True, (0,0,0))
        self.screen.blit(text, (20, 70))
        pygame.draw.rect(self.screen, (100,100,100), (20, 90, 200, 20))
        button_x = int(20 + (self.side_rooms - MIN_ROOMS) / (MAX_ROOMS - MIN_ROOMS) * 200 - 20 / 2)
        pygame.draw.rect(self.screen, (0,0,0), (button_x, 90, 20, 20))
        pygame.draw.rect(self.screen, (100, 100, 100), self.generate_button)
        text = self.font.render("Generate", True, (0,0,0))
        text_rect = text.get_rect(center=self.generate_button.center)
        self.screen.blit(text, text_rect)

        pygame.display.flip()


    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.generate_button.collidepoint(event.pos):
                        self.new_map(self.path_length, self.side_rooms)
                    elif 20 <= event.pos[0] <= 20 + 200 and 40 <= event.pos[1] <= 40 + 20:
                        self.slider1_in_use = True
                    elif 20 <= event.pos[0] <= 20 + 200 and 90 <= event.pos[1] <= 90 + 20:
                        self.slider2_in_use = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.slider1_in_use = False
                    self.slider2_in_use = False

            if self.slider1_in_use:
                relative_position = max(0, min(1, (pygame.mouse.get_pos()[0] - 20) / 200))
                self.path_length = int(MIN_PATH + relative_position * (MAX_PATH - MIN_PATH))

            if self.slider2_in_use:
                relative_position = max(0, min(1, (pygame.mouse.get_pos()[0] - 20) / 200))
                self.side_rooms= int(MIN_ROOMS + relative_position * (MAX_ROOMS - MIN_ROOMS))

            self.render()
            pygame.time.Clock().tick(60)


if __name__ == "__main__":
    Generator()