import pgzrun

WIDTH = 800
HEIGHT = 600

player = Actor("apple", (WIDTH//2, HEIGHT//2))
player.speedX = 3
player.speedY = 3
player.score = 0
player.life = 20

plat = Actor("stone", (400, 500))

stones = []

for j in range(3):
    for i in range(5):
        stone = Actor("stone", (i * 150 + 100, j*50+100))
        stones.append(stone)

def draw():
    screen.blit("bg", (0, 0))
    player.draw()
    plat.draw()
    for stone in stones:
        stone.draw()
    screen.draw.text(f"Score: {player.score }", (WIDTH-100, 20), color="green", fontsize=32)
    # screen.draw.text(f"Life: {player.life }", (20, 20), color="red", fontsize=32)
    for i in range(player.life):
        screen.blit("heart", (20 + i*20, 20))


def update():
    player.x += player.speedX
    player.y += player.speedY

    if player.right > WIDTH or player.left < 0:
        player.speedX = -player.speedX
    if player.top < 0:
        player.speedY = -player.speedY
    if player.bottom > HEIGHT:
        player.life -= 1
        player.x = WIDTH//2
        player.y = HEIGHT//2
        player.speedY = -player.speedY
 

    if keyboard.left:
        plat.x -= 5
    if keyboard.right:
        plat.x += 5

    if player.colliderect(plat) and player.speedY > 0:
        player.speedY = -player.speedY

    for stone in stones:
        if player.colliderect(stone):
            player.score += 10
            player.speedY = -player.speedY
            stones.remove(stone)
            break



pgzrun.go()