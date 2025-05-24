import json
import os

class HighScore:
    def __init__(self, file_path="highscore.txt"):
        self.file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), file_path)
        self.highscore = self.load_highscore()

    def load_highscore(self):
        if not os.path.exists(self.file_path):
            return 0
        try:
            with open(self.file_path, "r") as f:
                return int(f.read().strip())
        except ValueError:
            return 0

    def save_highscore(self):
        with open(self.file_path, "w") as f:
            f.write(str(self.highscore))

    def update(self, score):
        if score > self.highscore:
            self.highscore = score
            self.save_highscore()

    def display(self, surface, font, x, y, color=(255,255,0)):
        text_surface = font.render(f"High Score: {self.highscore}", True, color)
        surface.blit(text_surface, (x, y))
