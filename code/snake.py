import pygame
from constants import BLOCK_SIZE, LIGHT_GREEN, DARK_GREEN, SCREEN_WIDTH, SCREEN_HEIGHT, BLACK

class Snake:
    def __init__(self, start_x, start_y):
        self.block_size = BLOCK_SIZE
        self.body = [(start_x, start_y)]
        self.direction = (1, 0)  # Initial direction: right (dx, dy)
        self.color_body = LIGHT_GREEN
        self.color_head = DARK_GREEN
        self.grow_pending = False

    def move(self):
        curr_x, curr_y = self.body[0]
        dx, dy = self.direction
        
        new_head = (curr_x + dx * self.block_size, curr_y + dy * self.block_size)
        self.body.insert(0, new_head)

        if self.grow_pending:
            self.grow_pending = False
        else:
            self.body.pop()

    def grow(self):
        self.grow_pending = True

    def change_direction(self, new_direction):
        # Prevent reversing direction directly
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction

    def draw(self, surface):
        for i, segment in enumerate(self.body):
            color = self.color_head if i == 0 else self.color_body
            pygame.draw.rect(surface, color, (segment[0], segment[1], self.block_size, self.block_size))
            # Optional: draw a border for better visibility
            pygame.draw.rect(surface, BLACK, (segment[0], segment[1], self.block_size, self.block_size), 1)

    def get_head_position(self):
        return self.body[0]

    def check_collision_with_self(self):
        head = self.get_head_position()
        return head in self.body[1:]

    def check_collision_with_walls(self):
        head_x, head_y = self.get_head_position()
        if not (0 <= head_x < SCREEN_WIDTH and 0 <= head_y < SCREEN_HEIGHT):
            return True
        return False
    
    def reset(self, start_x, start_y):
        self.body = [(start_x, start_y)]
        self.direction = (1, 0)
        self.grow_pending = False
