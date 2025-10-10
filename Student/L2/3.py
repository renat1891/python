import pgzrun
import random

WIDTH = 400
HEIGHT = 600

LANE_LEFT = WIDTH // 4
LANE_RIGHT = WIDTH * 3 // 4
LANES = [LANE_LEFT, LANE_RIGHT]
class Player(Actor):
    def __init__(self, x, y):
        super().__init__("player_car", (x, y))
        self.speed = 5

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
    
    def collide_enemy(self):
        if self.colliderect(enemy):
            lives -= 1
        if lives <= 0:
                game_over = True
        else:
                reset_enemy()

player = Player(WIDTH//2, HEIGHT - 100)  


class Game():
    lives = 3
    score = 0
    over = False


class Enemy(Actor):
    def __init__(self, x, y):
        super().__init__("enemy_car", (x, y))
        self.speed = 5
        self.lane = 1

enemy = Enemy(LANE_RIGHT, -100) 




lives = 3
game_over = False

falling_items = []

def draw():
    screen.blit("background", (0, 0))  

    player.draw()
    enemy.draw()

   
    for i in range(lives):
        screen.blit("heart", (10 + i * 40, 10))

   
    for item in falling_items:
        item.draw()

    if game_over:
        screen.draw.text("GAME OVER", center=(WIDTH//2, HEIGHT//2), color="red")


def update():

    if Game.over:
        return

 
    player.control()

    
    player.border()

    
    enemy.y += enemy.speed
    if enemy.y > HEIGHT:
        reset_enemy()

    
    player.collide_enemy()

    
    for item in falling_items[:]:
        item.y += 3  

        if item.y > HEIGHT:
            falling_items.remove(item)

        if player.colliderect(item):
            if item.image == "heart":
                lives += 1
            elif item.image == "bomb":
                lives -= 1
                if lives <= 0:
                    Game.over = True
            falling_items.remove(item)

def reset_enemy():
    enemy.lane = random.choice([0, 1])
    enemy.x = LANES[enemy.lane]
    enemy.y = -100

def spawn_item():
    lane = random.choice([0, 1])
    x = LANES[lane]
    y = -50
    if random.random() < 0.5:
        item = Actor("heart", (x, y))
    else:
        item = Actor("bomb", (x, y))
    falling_items.append(item)

def time_event():
    if not Game.over:
        spawn_item()

clock.schedule_interval(time_event, 5.0)

pgzrun.go()