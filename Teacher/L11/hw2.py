import pgzrun
import random

WIDTH = 400
HEIGHT = 600

LANE_LEFT = WIDTH // 4
LANE_RIGHT = WIDTH * 3 // 4
LANES = [LANE_LEFT, LANE_RIGHT]

class Game():
    score = 0
    lives = 3
    over = False

player = Actor("player_car", (WIDTH//2, HEIGHT - 100))  
player.speed = 5   

enemy = Actor("enemy_car", (LANE_RIGHT, -100))  
enemy.lane = 1
enemy.speed = 4
enemy.angle = 180
# print(dir(enemy))
# exit()


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

 
    if keyboard.left:
        player.x -= player.speed
    if keyboard.right:
        player.x += player.speed

    
    if player.x < 50:
        player.x = 50
    if player.x > WIDTH - 50:
        player.x = WIDTH - 50

    
    enemy.y += enemy.speed
    if enemy.y > HEIGHT:
        reset_enemy()

    
    if player.colliderect(enemy):
        lives -= 1
        if lives <= 0:
            game_over = True
        else:
            reset_enemy()

    
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
    if not game_over:
        spawn_item()

clock.schedule_interval(time_event, 5.0)

pgzrun.go()