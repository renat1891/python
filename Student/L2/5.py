

import pgzrun
import random
import sys

WIDTH = 400
HEIGHT = 600

LANE_LEFT = WIDTH // 4
LANE_RIGHT = WIDTH * 3 // 4
LANES = [LANE_LEFT, LANE_RIGHT]


class Game:
    def __init__(self):
        self.lives = 3
        self.score = 0
        self.player = Player(WIDTH // 2, HEIGHT - 100, self)
        self.enemy = Enemy(random.choice(LANES), -100, self)
        self.items = []

        
        clock.schedule_interval(self.spawn_item, 5.0)

    def draw(self):
        screen.blit("background", (0, 0))
        self.player.draw()
        self.enemy.draw()

        for i in range(self.lives):
            screen.blit("heart", (10 + i * 40, 10))

        for item in self.items:
            item.draw()

        screen.draw.text(f"SCORE: {self.score}", topright=(WIDTH - 10, 10), color="white")

    def update(self):
        self.player.update()
        self.enemy.update()

        for item in self.items[:]:
            item.update()
            if item.y > HEIGHT:
                self.items.remove(item)
            elif self.player.colliderect(item):
                if item.image == "heart":
                    self.lives += 1
                elif item.image == "bomb":
                    self.lives -= 1
                    if self.lives <= 0:
                        sys.exit()  
                self.items.remove(item)

        if self.enemy.y > HEIGHT:
            self.score += 1

    def reset_enemy(self):
        self.enemy.reset()

    def spawn_item(self):
        lane = random.choice([0, 1])
        x = LANES[lane]
        y = -50
        image = "heart" if random.random() < 0.5 else "bomb"
        self.items.append(Item(image, x, y))


class Player(Actor):
    def __init__(self, x, y, game):
        super().__init__("player_car", (x, y))
        self.speed = 5
        self.game = game

    def update(self):
        self.control()
        self.border()
        self.check_collision()

    def control(self):
        if keyboard.left:
            self.x -= self.speed
        if keyboard.right:
            self.x += self.speed

    def border(self):
        if self.x < 50:
            self.x = 50
        if self.x > WIDTH - 50:
            self.x = WIDTH - 50

    def check_collision(self):
        if self.colliderect(self.game.enemy):
            self.game.lives -= 1
            if self.game.lives <= 0:
                sys.exit()
            else:
                self.game.reset_enemy()


class Enemy(Actor):
    def __init__(self, x, y, game):
        super().__init__("enemy_car", (x, y))
        self.speed = 5
        self.game = game

    def update(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.reset()

    def reset(self):
        self.x = random.choice(LANES)
        self.y = -100


class Item(Actor):
    def __init__(self, image, x, y):
        super().__init__(image, (x, y))
        self.speed = 3

    def update(self):
        self.y += self.speed
game = Game()


def draw():
    game.draw()


def update():
    game.update()


pgzrun.go()
