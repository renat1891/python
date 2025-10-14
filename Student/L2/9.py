
import pgzrun
import random
from playsound3 import playsound


WIDTH = 800
HEIGHT = 600


class Game:
    def __init__(self):
        self.score = 0
        self.lives = 3
        self.game_over = False
        self.win = False
        playsound("./sounds/background.mp3", block=False)

    def draw_hud(self):
        screen.draw.text(f"Score: {self.score}", (20, 20), color="white", fontsize=36)
        screen.draw.text(f"Lives: {self.lives}", (20, 60), color="red", fontsize=36)
        if self.game_over:
            screen.draw.text("GAME OVER", center=(WIDTH//2, HEIGHT//2), color="yellow", fontsize=80)
        elif self.win:
            screen.draw.text("YOU WIN!", center=(WIDTH//2, HEIGHT//2), color="green", fontsize=80)


class Player(Actor):
    def __init__(self, x, y):
        super().__init__("stone", (x, y))
        self.speed = 7
        self.blink_timer = 0      
        self.visible = True       

    def move(self):
        if keyboard.left:
            self.x -= self.speed
        if keyboard.right:
            self.x += self.speed
        self.x = max(40, min(WIDTH - 40, self.x))

    def start_blink(self):
        self.blink_timer = 60  

    def update_blink(self):
        if self.blink_timer > 0:
            self.blink_timer -= 1
            if self.blink_timer % 5 == 0:
                self.visible = not self.visible
        else:
            self.visible = True

    def draw(self):
        if self.visible:
            super().draw()


class Falling(Actor):
    def __init__(self, image, speed_min, speed_max):
        super().__init__(image, (random.randint(40, WIDTH - 40), -50))
        self.speed = random.randint(speed_min, speed_max)

    def fall(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.off_screen()

    def off_screen(self):
        self.y = -50
        self.x = random.randint(40, WIDTH - 40)


game = Game()
player = Player(WIDTH // 2, HEIGHT - 50)

stars = [Falling("coin", 2, 4) for _ in range(3)]
bombs = [Falling("bomb", 4, 6) for _ in range(2)]
hearts = [Falling("heart", 2, 4) for _ in range(1)]


def draw():
    screen.fill((10, 20, 40))
    player.draw()
    for s in stars:
        s.draw()
    for b in bombs:
        b.draw()
    for h in hearts:
        h.draw()
    game.draw_hud()


def update():
    if game.game_over or game.win:
        return

    player.move()
    player.update_blink()

    for s in stars:
        s.fall()
        if player.colliderect(s):
            game.score += 1
            s.off_screen()
            playsound('.\sounds\collect.mp3', block=False)

    for b in bombs:
        b.fall()
        if player.colliderect(b):
            game.lives -= 1
            b.off_screen()

    for h in hearts:
        h.fall()
        if player.colliderect(h):
            game.lives += 1
            h.off_screen()
            player.start_blink()  

    if game.lives <= 0:
        game.game_over = True

    if game.score >= 10:
        game.win = True


pgzrun.go()
