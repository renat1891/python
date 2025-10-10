# import pgzrun

# WIDTH = 800
# HEIGHT = 600

# player = Actor("apple", (WIDTH//2, HEIGHT//2))
# player.speedX = 3
# player.speedY = 3
# plat = Actor("stone", (400, 500))
# stones = []

# for j in range(3):
#     for i in range(5):
#         stone = Actor("stone", (i * 150 + 100, j*50+100))
#         stones.append(stone)

# def draw():
#     screen.blit('bg', (0, 0))
#     player.draw()
#     plat.draw()
#     for stone in stones:
#         stone.draw()

# def update():
#     player.x += player.speedX
#     player.y += player.speedY
    
#     if player.right > WIDTH or player.left < 0:
#         player.speedX = -player.speedX
#     if player.bottom> HEIGHT or player.top < 0:
#         player.speedY = -player.speedY


#     if keyboard.left:
#         plat.x -= 5
#     if keyboard.right:
#         plat.x += 5
    
#     if player.colliderect(plat) and player.speedY > 0:
#         player.speedY = -player.speedY
    
#     for stone in stones:
#         if player.colliderect(stone):
#             player.speedY = -player.speedY
#             stones.remove(stone)
#             break

# pgzrun.go()





# import pgzrun

# WIDTH = 800
# HEIGHT = 600

# player = Actor("apple", (WIDTH//2, HEIGHT//2))
# player.speedX = 3
# player.speedY = 3
# player.score = 0
# player.life = 20

# plat = Actor("stone", (400, 500))

# stones = []

# for j in range(3):
#     for i in range(5):
#         stone = Actor("stone", (i * 150 + 100, j*50+100))
#         stones.append(stone)

# def draw():
#     screen.blit("bg", (0, 0))
#     player.draw()
#     plat.draw()
#     for stone in stones:
#         stone.draw()
#     screen.draw.text(f"Score: {player.score }", (WIDTH-100, 20), color="green", fontsize=32)
#     # screen.draw.text(f"Life: {player.life }", (20, 20), color="red", fontsize=32)
#     for i in range(player.life):
#         screen.blit("heart", (20 + i*20, 20))


# def update():
#     player.x += player.speedX
#     player.y += player.speedY

#     if player.right > WIDTH or player.left < 0:
#         player.speedX = -player.speedX
#     if player.top < 0:
#         player.speedY = -player.speedY
#     if player.bottom > HEIGHT:
#         player.life -= 1
#         player.x = WIDTH//2
#         player.y = HEIGHT//2
#         player.speedY = -player.speedY
 

#     if keyboard.left:
#         plat.x -= 5
#     if keyboard.right:
#         plat.x += 5

#     if player.colliderect(plat) and player.speedY > 0:
#         player.speedY = -player.speedY

#     for stone in stones:
#         if player.colliderect(stone):
#             player.score += 10
#             player.speedY = -player.speedY
#             stones.remove(stone)
#             break



# pgzrun.go()











# import pgzrun
# import random

# WIDTH = 400
# HEIGHT = 600

# LANE_LEFT = WIDTH // 4
# LANE_RIGHT = WIDTH * 3 // 4
# LANES = [LANE_LEFT, LANE_RIGHT]

# player = Actor("player_car", (WIDTH//2, HEIGHT - 100))  
# player.speed = 5   

# enemy = Actor("enemy_car", (LANE_RIGHT, -100))  
# enemy.lane = 1
# enemy.speed = 4


# lives = 3
# game_over = False

# falling_items = []

# def draw():
#     screen.blit("background", (0, 0))  

#     player.draw()
#     enemy.draw()

   
#     for i in range(lives):
#         screen.blit("heart", (10 + i * 40, 10))

   
#     for item in falling_items:
#         item.draw()

#     if game_over:
#         screen.draw.text("GAME OVER", center=(WIDTH//2, HEIGHT//2), color="red")


# def update():
#     global enemy, lives, game_over, falling_items

#     if game_over:
#         return

 
#     if keyboard.left:
#         player.x -= player.speed
#     if keyboard.right:
#         player.x += player.speed

    
#     if player.x < 50:
#         player.x = 50
#     if player.x > WIDTH - 50:
#         player.x = WIDTH - 50

    
#     enemy.y += enemy.speed
#     if enemy.y > HEIGHT:
#         reset_enemy()

    
#     if player.colliderect(enemy):
#         lives -= 1
#         if lives <= 0:
#             game_over = True
#         else:
#             reset_enemy()

    
#     for item in falling_items[:]:
#         item.y += 3  

#         if item.y > HEIGHT:
#             falling_items.remove(item)

#         if player.colliderect(item):
#             if item.image == "heart":
#                 lives += 1
#             elif item.image == "bomb":
#                 lives -= 1
#                 if lives <= 0:
#                     game_over = True
#             falling_items.remove(item)

# def reset_enemy():
#     enemy.lane = random.choice([0, 1])
#     enemy.x = LANES[enemy.lane]
#     enemy.y = -100

# def spawn_item():
#     lane = random.choice([0, 1])
#     x = LANES[lane]
#     y = -50
#     if random.random() < 0.5:
#         item = Actor("heart", (x, y))
#     else:
#         item = Actor("bomb", (x, y))
#     falling_items.append(item)

# def time_event():
#     if not game_over:
#         spawn_item()

# clock.schedule_interval(time_event, 5.0)

# pgzrun.go()





# import pgzrun
# import random

# WIDTH = 800
# HEIGHT = 600

# player = Actor("apple", (WIDTH//2, HEIGHT//2))
# player.speedX = 3
# player.speedY = 3
# player.score = 0
# player.life = 20

# plat = Actor("stone", (400, 500))

# stones = []

# for j in range(3):
#     for i in range(5):
#         stone = Actor("stone", (i * 150 + 100, j*50+100))
#         stones.append(stone)

# falling_items = []  

# def draw():
#     screen.blit("bg", (0, 0))
#     player.draw()
#     plat.draw()
#     for stone in stones:
#         stone.draw()
#     for item in falling_items:
#         item.draw()
#     screen.draw.text(f"Score: {player.score}", (WIDTH-150, 20), color="green", fontsize=32)
#     for i in range(player.life):
#         screen.blit("heart", (20 + i*20, 20))

# def update():
#     player.x += player.speedX
#     player.y += player.speedY

#     if player.right > WIDTH or player.left < 0:
#         player.speedX = -player.speedX
#     if player.top < 0:
#         player.speedY = -player.speedY
#     if player.bottom > HEIGHT:
#         player.life -= 1
#         player.x = WIDTH//2
#         player.y = HEIGHT//2
#         player.speedY = -player.speedY

#     if keyboard.left:
#         plat.x -= 5
#     if keyboard.right:
#         plat.x += 5

#     if player.colliderect(plat) and player.speedY > 0:
#         player.speedY = -player.speedY

#     for stone in stones[:]:
#         if player.colliderect(stone):
#             player.score += 10
#             player.speedY = -player.speedY
#             spawn_item(stone.x, stone.y)  
#             stones.remove(stone)
#             break
#     for item in falling_items[:]:
#         item.y += 1  
#         if item.y > HEIGHT:
#             falling_items.remove(item)  
#         elif plat.colliderect(item):
#             if item.image == "heart":
#                 player.life += 1
#             elif item.image == "bomb":
#                 player.life -= 1
#             falling_items.remove(item)

# def spawn_item(x, y):
#     if random.random() < 0.5:
#         item = Actor("heart", (x, y))
#     else:
#         item = Actor("bomb", (x, y))
#     falling_items.append(item)

# pgzrun.go()
