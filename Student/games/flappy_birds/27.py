import pgzrun
import random
from pgzero.builtins import Actor, Rect

WIDTH = 800
HEIGHT = 500
CELL = 10

GRID_W = WIDTH // CELL
GRID_H = HEIGHT // CELL

class Player:
    """Гравець"""
    def __init__(self, image, pid, color, left_limit, right_limit):
        self.actor = Actor(image)
        self.actor.x = random.randint(left_limit, right_limit)
        self.actor.y = random.randint(50, HEIGHT-50)
        self.vx = random.choice([-3, 3])
        self.vy = random.choice([-3, 3])
        self.pid = pid
        self.color = color
        self.left_limit = left_limit
        self.right_limit = right_limit

    def move(self):
        self.actor.x += self.vx
        self.actor.y += self.vy
        if self.actor.left < self.left_limit or self.actor.right > self.right_limit:
            self.vx = -self.vx
        if self.actor.top < 0 or self.actor.bottom > HEIGHT:
            self.vy = -self.vy

    def bounce_back(self, other):
        if self.actor.colliderect(other.actor):
            if self.vx * other.vx > 0:
                self.vx = -self.vx
            if self.vy * other.vy > 0:
                self.vy = -self.vy

    def draw(self):
        self.actor.draw()

class Game:
    def __init__(self):
        self.grid = [[1 if x < GRID_W//2 else 2 for y in range(GRID_H)] for x in range(GRID_W)]
        self.sun = Player("bird", 1, (255,255,0), 0, WIDTH//2-1)
        self.moon = Player("bird", 2, (120,120,255), WIDTH//2, WIDTH-1)

    def capture_nearby_cells(self, player):
        radius = 2  
        gx = int(player.actor.x // CELL)
        gy = int(player.actor.y // CELL)
        for dx in range(-radius, radius + 1):
            for dy in range(-radius, radius + 1):
                nx, ny = gx + dx, gy + dy
                if 0 <= nx < GRID_W and 0 <= ny < GRID_H:
                    if self.grid[nx][ny] != player.pid:
                        self.grid[nx][ny] = player.pid
                        break

    def update(self):
        self.sun.move()
        self.moon.move()

        self.capture_nearby_cells(self.sun)
        self.capture_nearby_cells(self.moon)

        self.capture_cells(self.sun, self.moon)
        self.capture_cells(self.moon, self.sun)

        self.sun.bounce_back(self.moon)
        self.moon.bounce_back(self.sun)

    def capture_cells(self, player, other):
        if player.actor.colliderect(other.actor):
            count = random.randint(1,3)
            gx = int(player.actor.x // CELL)
            gy = int(player.actor.y // CELL)
            captured = 0
            for dx in [-1,0,1]:
                for dy in [-1,0,1]:
                    nx, ny = gx+dx, gy+dy
                    if 0 <= nx < GRID_W and 0 <= ny < GRID_H:
                        if self.grid[nx][ny] == other.pid and captured < count:
                            self.grid[nx][ny] = player.pid
                            captured += 1
                            

    def draw(self):
        screen.fill((0,0,0))
        for x in range(GRID_W):
            for y in range(GRID_H):
                owner = self.grid[x][y]
                if owner == 1:
                    screen.draw.filled_rect(Rect(x*CELL, y*CELL, CELL, CELL), self.sun.color)
                elif owner == 2:
                    screen.draw.filled_rect(Rect(x*CELL, y*CELL, CELL, CELL), self.moon.color)

        self.sun.draw()
        self.moon.draw()

        screen.draw.line((WIDTH//2,0), (WIDTH//2,HEIGHT), "white")

        sun_score = sum(row.count(1) for row in self.grid)
        moon_score = sum(row.count(2) for row in self.grid)
        screen.draw.text(f"Сонце: {sun_score}", (10,10), fontsize=30, color="yellow")
        screen.draw.text(f"Місяць: {moon_score}", (WIDTH-180,10), fontsize=30, color="lightblue")


game = Game()

def update():
    game.update()

def draw():
    game.draw()

pgzrun.go()
