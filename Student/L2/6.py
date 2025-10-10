import pgzrun
import random

WIDTH = 800
HEIGHT = 600


class Rocket(Actor):
    def __init__(self, x, y):
        super().__init__("ship", (x, y))  
        self.speed = 5
        self.lives = 3
        self.score = 0

    def move(self):
        if keyboard.left and self.left > 0:
            self.x -= self.speed
        if keyboard.right and self.right < WIDTH:
            self.x += self.speed
        if keyboard.up and self.top > 0:
            self.y -= self.speed
        if keyboard.down and self.bottom < HEIGHT:
            self.y += self.speed

    def draw_hud(self):
        screen.draw.text(f"Score: {self.score}", (20, 20), color="white", fontsize=36)
        screen.draw.text(f"Lives: {self.lives}", (20, 60), color="red", fontsize=32)


class Meteor(Actor):
    def __init__(self, x, y, speed):
        super().__init__("meteor_02", (x, y))  
        self.speed = speed

    def fall(self):
        self.y += self.speed
        if self.y > HEIGHT + 50:
            meteors.remove(self)


class Heart(Actor):
    def __init__(self, x, y, speed):
        super().__init__("heart", (x, y))   
        self.speed = speed

    def fall(self):
        self.y += self.speed
        if self.y > HEIGHT + 50:
            hearts.remove(self)

rocket = Rocket(WIDTH // 2, HEIGHT - 100)
meteors = []
hearts = []


def draw():
    screen.blit("bg", (0, 0))  
    rocket.draw()
    for m in meteors:
        m.draw()
    for h in hearts:
        h.draw()
    rocket.draw_hud()

    if rocket.lives <= 0:
        screen.draw.text("GAME OVER", center=(WIDTH//2, HEIGHT//2), color="red", fontsize=72)

def update():
    if rocket.lives <= 0:
        return

    rocket.move()
    if random.randint(0, 30) == 0:
        spawn_meteor()
    if random.randint(0, 200) == 0: 
        spawn_heart()

    for m in meteors[:]:
        m.fall()
        if rocket.colliderect(m):
            rocket.lives -= 1
            meteors.remove(m)

    for h in hearts[:]:
        h.fall()
        if rocket.colliderect(h):
            rocket.lives += 1
            hearts.remove(h)

def spawn_meteor():
    x = random.randint(50, WIDTH - 50)
    y = -50
    speed = random.randint(3, 6)
    meteors.append(Meteor(x, y, speed))

def spawn_heart():
    x = random.randint(50, WIDTH - 50)
    y = -50
    speed = random.randint(2, 4)
    hearts.append(Heart(x, y, speed))

pgzrun.go()
