import pgzrun
import random

WIDTH = 800
HEIGHT = 600

class Player(Actor):
    def __init__(self, x, y):
        super().__init__("apple", (x, y))
        self.speedX = 3
        self.speedY = 3
        self.score = 0
        self.life = 20

    def move(self):
        self.x += self.speedX
        self.y += self.speedY

    def collide(self, obj):
        if self.colliderect(obj) and self.speedY > 0:
            self.speedY = -self.speedY

    def collide_side(self):
        if self.right > WIDTH or self.left < 0:
            self.speedX = -self.speedX
        if self.top < 0:
            self.speedY = -self.speedY
        if self.bottom > HEIGHT:
            self.life -= 1
            self.x = WIDTH//2
            self.y = HEIGHT//2
            self.speedY = -self.speedY

    def draw_score(self):
        screen.draw.text(f"Score: {self.score}", (WIDTH-150, 20), color="green", fontsize=32)

    def draw_lifes(self):
        for i in range(self.life):
            screen.blit("heart", (20 + i*20, 20))

class Plat(Actor):
    def __init__(self, x, y):
        super().__init__("stone", (x, y))

    def control(self):
        if keyboard.left:
            self.x -= 5
        if keyboard.right:
            self.x += 5

class Stone(Actor):
    def __init__(self, x, y):
        super().__init__("stone", (x, y))


class Stones():
    stones = []

    def __init__(self):
        for j in range(3):
            for i in range(5):
                stone = Stone(i * 150 + 100, j*50+100)
                self.stones.append(stone)

    def draw(self):
        for stone in self.stones:
            stone.draw()

    def collide(self, obj):
        for stone in self.stones[:]:
            if obj.colliderect(stone):
                obj.score += 10
                obj.speedY = -obj.speedY
                bonus.spawn(stone.x, stone.y)  
                self.stones.remove(stone)
                break

class Bonus():
    items = []  

    def draw(self):
        for item in self.items:
            item.draw()

    def collide(self, obj):
        for item in self.items[:]:
            item.y += 1  
            if item.y > HEIGHT:
                self.items.remove(item)  
            elif plat.colliderect(item):
                if item.image == "heart":
                    obj.life += 1
                elif item.image == "bomb":
                    obj.life -= 1
                self.items.remove(item)

    def spawn(self, x, y):
        if random.randint(0, 10) == 0:
            item = Actor("heart", (x, y))
        elif random.randint(0, 3) == 0:
            item = Actor("bomb", (x, y))
        else:
            return
        bonus.items.append(item)

player = Player(400, 500)

plat = Plat(400, 500)

stones = Stones()

bonus = Bonus()

def draw():
    screen.blit("bg", (0, 0))
    player.draw()
    plat.draw()
    stones.draw()
    bonus.draw()
    player.draw_score()
    player.draw_lifes()

def update():
    player.move()

    player.collide_side()

    plat.control()

    player.collide(plat)

    stones.collide(player)

    bonus.collide(player)


pgzrun.go()
