import pygame
from snake import Snake 
from food import Food
from score import Score
from highscore import HighScore
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE, FPS, BLACK, RED, WHITE, FONT_SIZE_MESSAGE, FONT_SIZE_SCORE

class Game:
    def __init__(self, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, block_size=BLOCK_SIZE):
        pygame.init()
        self.width = width
        self.height = height
        self.block_size = block_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.fps = FPS
        self.game_over_flag = False
        self.font_message = pygame.font.SysFont(None, FONT_SIZE_MESSAGE)

        self.snake = Snake(self.width // 2 - (self.width // 2 % self.block_size), 
                           self.height // 2 - (self.height // 2 % self.block_size))
        self.food = Food(self.width, self.height, self.block_size)
        self.score = Score(10, 10, font_size=FONT_SIZE_SCORE)
        self.highscore = HighScore()
        self.font_highscore = pygame.font.SysFont(None, FONT_SIZE_SCORE)
        # Ensure food doesn't spawn on the snake initially
        while self.food.position in self.snake.body:
            self.food.respawn()


    def display_message(self, message, color=WHITE, duration=2000):
        text = self.font_message.render(message, True, color)
        text_rect = text.get_rect(center=(self.width / 2, self.height / 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        if duration > 0:
            pygame.time.wait(duration)

    def reset_game(self):
        self.snake.reset(self.width // 2 - (self.width // 2 % self.block_size),
                         self.height // 2 - (self.height // 2 % self.block_size))
        self.food.respawn()
        # Ensure food doesn't spawn on the snake after reset
        while self.food.position in self.snake.body:
            self.food.respawn()
        self.score.reset()
        self.game_over_flag = False


    def game_loop(self):
        running = True
        while running:
            while self.game_over_flag:
                self.display_message(f"Game Over! Score: {self.score.score}. Press R to Restart or Q to Quit", RED, 0)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        self.game_over_flag = False # to exit this inner loop
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            running = False
                            self.game_over_flag = False # to exit this inner loop
                        if event.key == pygame.K_r:
                            self.reset_game()
                            # game_over_flag is set to False in reset_game

            if not running: # If Q was pressed in game over screen
                break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.snake.change_direction((-1, 0))
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.snake.change_direction((1, 0))
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.snake.change_direction((0, -1))
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.snake.change_direction((0, 1))
            
            if not self.game_over_flag:
                self.snake.move()

                # Check if snake eats food
                if self.snake.get_head_position() == self.food.position:
                    self.score.increase()
                    self.food.respawn()
                    # Ensure new food doesn't spawn on snake
                    while self.food.position in self.snake.body:
                        self.food.respawn()
                    self.snake.grow()

                # Check for game over conditions
                if self.snake.check_collision_with_walls() or self.snake.check_collision_with_self():
                    self.highscore.update(self.score.score)
                    self.game_over_flag = True
                
                # Drawing
                self.screen.fill(BLACK)
                self.snake.draw(self.screen)
                self.food.draw(self.screen)
                self.score.display(self.screen)
                self.highscore.display(self.screen, self.font_highscore, 10, FONT_SIZE_SCORE + 10)
                pygame.display.flip()

            self.clock.tick(self.fps)

        pygame.quit()

if __name__ == '__main__':
    # This part is for testing the Game class directly.
    # Normally, you would run main.py
    game = Game()
    game.game_loop()
