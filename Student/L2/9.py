import pgzrun
import random
from playsound3 import playsound

WIDTH = 960
HEIGHT = 540

# --- Клас гри ---
class Game:
    def __init__(self):
        self.score = 0
        self.game_over = False

    def reset(self):
        self.score = 0
        self.game_over = False

    def draw(self):
        screen.draw.text(f"Score: {self.score}", (20, 20), color="white", fontsize=36)
        if self.game_over:
            screen.draw.text("GAME OVER", center=(WIDTH // 2, HEIGHT // 2 - 20), color="yellow", fontsize=60)
            screen.draw.text("Press SPACE to restart", center=(WIDTH // 2, HEIGHT // 2 + 40), color="white", fontsize=30)

# --- Клас платформи ---
class Platform(Actor):
    def __init__(self, image, x, y, w):
        super().__init__(image, (x + w / 2, y + 20))
        self.x = x
        self.y = y
        self.width = w
        self.height = 40
        self._surf = pygame.transform.scale(self._surf, (self.width, self.height))

# --- Клас монетки ---
class Coin(Actor):
    def __init__(self, x, y):
        super().__init__("coin", (x, y))
        self.collected = False

# --- Клас гравця ---
class Player(Actor):
    def __init__(self, x, y):
        super().__init__("bird", (x, y))
        self.vx = 0
        self.vy = 0
        self.on_ground = False
        self.space_pressed = False

    def move(self, dt):
        speed = 250
        gravity = 900
        jump_speed = -520

        # Рух на стрілки
        if keyboard.left:
            self.vx = -speed
        elif keyboard.right:
            self.vx = speed
        else:
            self.vx = 0

        # Стрибок на пробіл
        if keyboard.space and self.on_ground and not self.space_pressed:
            self.vy = jump_speed
            self.on_ground = False
            self.space_pressed = True
            # playsound('.\\sounds2\\jump.mp3', block=False)
        elif not keyboard.space:
            self.space_pressed = False

        # Гравітація
        self.vy += gravity * dt
        if self.vy > 900:
            self.vy = 900

        # Рух
        self.x += self.vx * dt
        self.y += self.vy * dt

        # Межі екрана
        if self.x < 0:
            self.x = 0
        if self.x > WIDTH:
            self.x = WIDTH

        # Колізії з платформами
        self.on_ground = False
        for plat in platforms:
            if (self.x + self.width / 2 > plat.x and self.x - self.width / 2 < plat.x + plat.width and
                self.y + self.height / 2 > plat.y and self.y + self.height / 2 < plat.y + 20 and
                self.vy >= 0):
                self.y = plat.y - self.height / 2
                self.vy = 0
                self.on_ground = True

        # Якщо впав — гра закінчується
        if self.y > HEIGHT:
            game.game_over = True

# --- Ініціалізація ---
game = Game()
player = Player(100, 300)

# --- Генерація платформ ---
def spawn_platforms():
    platforms = []
    # нижня "земля"
    platforms.append(Platform("stone", 0, HEIGHT - 60, WIDTH))

    # випадкові платформи вище
    for _ in range(5):
        w = random.randint(150, 300)               # ширина платформи
        x = random.randint(0, WIDTH - w)           # позиція по X
        y = random.randint(120, HEIGHT - 150)      # позиція по Y
        platforms.append(Platform("stone", x, y, w))
    return platforms

platforms = spawn_platforms()

# --- Монетка ---
coin = None

def spawn_coin():
    """Створює монетку на випадковій платформі"""
    global coin
    plat = random.choice(platforms)
    x = random.randint(plat.x + 30, plat.x + plat.width - 30)
    y = plat.y - 40
    coin = Coin(x, y)

spawn_coin()

# --- Малювання ---
def draw():
    screen.blit("bg", (0, 0))
    for plat in platforms:
        plat.draw()
    if coin and not coin.collected:
        coin.draw()
    player.draw()
    game.draw()

# --- Оновлення ---
def update(dt):
    global coin
    if game.game_over:
        if keyboard.space:
            restart_game()
        return

    player.move(dt)

    # Збір монетки
    if coin and not coin.collected and player.colliderect(coin):
        coin.collected = True
        game.score += 1
        # playsound('.\\sounds2\\collect.mp3', block=False)
        spawn_coin()  # спавнимо нову монету одразу після збору

# --- Рестарт ---
def restart_game():
    global platforms
    game.reset()
    player.x, player.y = 100, 300
    player.vx, player.vy = 0, 0
    player.on_ground = False
    platforms = spawn_platforms()  # нові випадкові платформи
    spawn_coin()

pgzrun.go()
