import pygame

class Score:
    def __init__(self, x, y, font_size=35, color=(255, 255, 255)):
        self.score = 0
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont(None, font_size)
        self.color = color

    def display(self, surface):
        score_text = self.font.render(f"Score: {self.score}", True, self.color)
        surface.blit(score_text, (self.x, self.y))

    def increase(self, points=1):
        self.score += points

    def reset(self):
        self.score = 0
