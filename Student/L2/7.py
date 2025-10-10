import pgzrun
import random
from math import sin, cos, radians

WIDTH = 800
HEIGHT = 600

class Rocket(Actor):
    def __init__(self, x, y):
        super().__init__("ship", (x, y))  
        self.speed = 5

    def move(self):
        if keyboard.left:
            self.angle += 3
        if keyboard.right:
            self.angle -= 3
        if keyboard.up:
            self.x += self.speed * -sin(radians(self.angle))
            self.y += self.speed * -cos(radians(self.angle))
            

class Game():
    score = 0
    
    def draw_points(self):
        screen.draw.text(f"Score: {self.score}", (20, 20), color="white", fontsize=36)
        

class Coin(Actor):
    def __init__(self, x, y):
        super().__init__("coin", (x, y))

    def random_move(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)


rocket = Rocket(WIDTH // 2, HEIGHT // 2)
coin = Coin(100, 100)
game = Game()

def draw():
    screen.blit("bg", (0, 0))  
    rocket.draw()
    coin.draw()
    game.draw_points()

def update():
    rocket.move()
    
    if rocket.colliderect(coin):
        coin.random_move()
        game.score += 10


pgzrun.go()