    
import pgzrun
import random

WIDTH = 288
HEIGHT = 512

class Game:
    def __init__(self):
        self.score = 0
        self.game_over = False

    def reset(self):
        self.score = 0
        self.game_over = False

    def draw(self):
        screen.draw.text(f"Score: {self.score}", (20, 20), color="white", fontsize=36)
        if self.game_over:
            screen.draw.text("GAME OVER", center=(WIDTH//2, HEIGHT//2), color="yellow", fontsize=60)
            screen.draw.text("Press SPACE to restart", center=(WIDTH//2, HEIGHT//2 + 60), color="white", fontsize=30)


class Bird(Actor):
    def __init__(self, x, y):
        super().__init__("bird", (x, y))
        self.images = ["bird", "bird0", "bird1", "bird2"]
        self.image_index = 0
        self.vy = 0
        self.angle = 0
        self.space_pressed = False

    def move(self):
        if keyboard.space and not self.space_pressed:
            self.vy = -4
            self.space_pressed = True
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]
            self.angle = -45
        elif not keyboard.space:
            self.space_pressed = False
        self.vy += 0.25
        self.y += self.vy
        self.y = max(0, min(self.y, HEIGHT - 20))

        if self.y == 0 or self.y == HEIGHT - 20:
            self.vy = 0
        self.angle += 2 if self.vy > 0 else -2
        self.angle = max(-45, min(self.angle, 45))



class PipePair:
    def __init__(self, x):
        self.x = x
        self.reset()

    def reset(self):
        self.gap_y = random.randint(150, 350)
        self.top = Actor("pipe-top", (self.x, self.gap_y - 200))
        self.bottom = Actor("pipe-down", (self.x, self.gap_y + 200))
        self.passed = False

    def move(self):
        self.x -= 2
        self.top.x = self.bottom.x = self.x

        
        if self.x < -50:
            other_pipe = [p for p in pipes if p != self][0]
            self.x = other_pipe.x + 500  
            self.reset()

game = Game()
bird = Bird(100, 250)
pipes = [PipePair(WIDTH + 150), PipePair(WIDTH + 650)]  


def draw():
    screen.blit("background-day", (0, 0))
    for pipe in pipes:
        pipe.top.draw()
        pipe.bottom.draw()
    bird.draw()
    game.draw()

def update():
    if game.game_over:
        if keyboard.space:
            restart_game()
        return

    bird.move()
    for pipe in pipes:
        pipe.move()
        if bird.colliderect(pipe.top) or bird.colliderect(pipe.bottom):
            game.game_over = True
        if not pipe.passed and pipe.x + pipe.top.width/2 < bird.x:
            pipe.passed = True
            game.score += 1

    if bird.y >= HEIGHT - 20:
        game.game_over = True

def restart_game():
    game.reset()
    bird.x, bird.y, bird.vy, bird.angle = 100, 250, 0, 0
    for i, pipe in enumerate(pipes):
        pipe.x = WIDTH + 150 + i*500  
        pipe.reset()

pgzrun.go()

