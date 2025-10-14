import pgzrun
import random
from math import sin, cos, radians
import time

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


class Car(Actor):
    def __init__(self, x, y):
        super().__init__("enemy_car", (x, y))
        self.speed = 5
        self.angle = 0
        self.trail = []
        self.respawn_time = 0
        self.blink_duration = 2
        self.blink_interval = 0.2
        self.visible = True

    def move(self):
        if game.game_over:
            return

        
        if keyboard.left:
            self.angle += 3
        if keyboard.right:
            self.angle -= 3

        
        self.x += self.speed * -sin(radians(self.angle))
        self.y += self.speed * -cos(radians(self.angle))

        
        if self.x < 0 or self.x > WIDTH or self.y < 0 or self.y > HEIGHT:
            self.respawn()

        
        self.trail.append((self.x, self.y))
        if len(self.trail) > 100:
            self.trail.pop(0)

        
        if time.time() < self.respawn_time + self.blink_duration:
            if int((time.time() - self.respawn_time) / self.blink_interval) % 2 == 0:
                self.visible = False
            else:
                self.visible = True
        else:
            self.visible = True

    def respawn(self):
        game.lives -= 1
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.angle = 0
        self.trail.clear()
        self.respawn_time = time.time()


class Coin(Actor):
    def __init__(self, x, y):
        super().__init__("coin", (x, y))

    def random_move(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)

class Bomb(Actor):
    def __init__(self, x, y):
        super().__init__("bomb", (x, y))

    def random_move(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)

class Heart(Actor):
    def __init__(self, x, y):
        super().__init__("heart", (x, y))

    def random_move(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)


game = Game()
car = Car(WIDTH//2, HEIGHT//2)
coin = Coin(random.randint(0, WIDTH), random.randint(0, HEIGHT))
bombs = [Bomb(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(3)]
hearts = [Heart(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(2)]

last_bomb_spawn = time.time()
last_heart_spawn = time.time()


def draw():
    screen.fill((30, 30, 40))

    for pos in car.trail:
        screen.draw.filled_rect(Rect(pos, (10, 10)), (0, 200, 0))

    for bomb in bombs:
        bomb.draw()

    for heart in hearts:
        heart.draw()

    coin.draw()

    if car.visible:
        car.draw()

    game.draw_points()


def update():
    global last_bomb_spawn, last_heart_spawn

    if game.game_over:
        return

    car.move()

    if car.colliderect(coin):
        game.score += 10
        coin.random_move()
        car.trail.append((car.x, car.y))

    for heart in hearts:
        if car.colliderect(heart):
            game.lives += 1
            heart.random_move()

    for bomb in bombs:
        if car.colliderect(bomb):
            car.respawn()
            bomb.random_move()

    if time.time() - last_bomb_spawn > 5 and len(bombs) < 3:
        bombs.append(Bomb(random.randint(0, WIDTH), random.randint(0, HEIGHT)))
        last_bomb_spawn = time.time()

    if time.time() - last_heart_spawn > 10 and len(hearts) < 2:
        hearts.append(Heart(random.randint(0, WIDTH), random.randint(0, HEIGHT)))
        last_heart_spawn = time.time()

    if game.lives <= 0 or game.score >= 150:
        game.game_over = True

pgzrun.go()
