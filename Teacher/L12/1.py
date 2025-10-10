import pgzrun
import random
from math import sin, cos, radians

WIDTH = 800
HEIGHT = 600

class Rocket(Actor):
    def __init__(self, x, y):
        super().__init__("ship", (x, y))  
        self.speed = 5
        self.lives = 3
        self.score = 0

    def move(self):
        # left, right, only up

        if keyboard.left:
            self.angle += 3
        if keyboard.right:
            self.angle -= 3
        if keyboard.up:
            self.x += self.speed * -sin(radians(self.angle))
            self.y += self.speed * -cos(radians(self.angle))

        # if keyboard.left and self.left > 0:
        #     self.x -= self.speed
        # if keyboard.right and self.right < WIDTH:
        #     self.x += self.speed
        # if keyboard.up and self.top > 0:
        #     self.y -= self.speed
        # if keyboard.down and self.bottom < HEIGHT:
        #     self.y += self.speed

    def check_bottom(self):
        if self.bottom >= HEIGHT:
            self.lives -= 1
            self.x = WIDTH // 2
            self.y = HEIGHT // 2

    def draw_hud(self):
        screen.draw.text(f"Score: {self.score}", (20, 20), color="white", fontsize=36)
        screen.draw.text(f"Lives: {self.lives}", (20, 60), color="red", fontsize=32)


class FallingObject(Actor):
    def __init__(self, image, x, y, speed, kind):
        super().__init__(image, (x, y))
        self.speed = speed
        self.kind = kind  

    def fall(self):
        self.y += self.speed
        if self.y > HEIGHT + 20:
            objects.remove(self)


rocket = Rocket(WIDTH // 2, HEIGHT // 2)
objects = []  


def draw():
    screen.blit("bg", (0, 0))  
    rocket.draw()
    for obj in objects:
        obj.draw()
    rocket.draw_hud()

    if rocket.lives <= 0:
        screen.draw.text("GAME OVER", center=(WIDTH//2, HEIGHT//2), color="red", fontsize=72)

def update():
    if rocket.lives <= 0:
        return

    rocket.move()
    rocket.check_bottom()

    
    for obj in objects:
        obj.fall()

    
    for obj in objects[:]:
        if rocket.colliderect(obj):
            if obj.kind == "coin":
                rocket.score += 10
            elif obj.kind == "bomb":
                rocket.lives -= 1
            elif obj.kind == "heart":
                rocket.lives += 1
            objects.remove(obj)

    
    if random.randint(0, 50) == 0:
        spawn_object()

def spawn_object():
    x = random.randint(40, WIDTH - 40)
    y = -20
    speed = random.randint(3, 6)
    r = random.random()
    if r < 0.25:  
        obj = FallingObject("bomb", x, y, speed, "bomb")
    elif r < 0.35:  
        obj = FallingObject("heart", x, y, speed, "heart")
    else:  
        obj = FallingObject("coin", x, y, speed, "coin")

    objects.append(obj)

pgzrun.go()