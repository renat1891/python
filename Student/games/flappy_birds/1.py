import pgzrun
import random

WIDTH = 800
HEIGHT = 600

class Game:
    def __init__(self):
        self.score = 0
        self.lives = 3
        self.game_over = False

    def draw_points(self):
        screen.draw.text(f"Score: {self.score}", (20, 20), color="white", fontsize=36)
        screen.draw.text(f"Lives: {self.lives}", (20, 60), color="red", fontsize=36)
        if self.game_over:
            screen.draw.text("GAME OVER", center=(WIDTH//2, HEIGHT//2), color="yellow", fontsize=80)
        
class Bird(Actor):
    def __init__(self, x, y):
        super().__init__("bird", (x, y))
        self.space_pressed = False

    
    def move(self):
        if keyboard.space:
            if not self.space_pressed:
                self.y -= 40
                self.space_pressed = True
        else:
            self.space_pressed = False
        self.y += 2
        

bird = Bird(100, 100)
def draw():
    screen.blit("background-day", (0, 0))
    bird.draw()

def update():
    bird.move()

pgzrun.go()
    
        
        
        