import pgzrun
import random
import math

WIDTH = 800
HEIGHT = 600
TITLE = "Платформер"

class Player:
    def __init__(self):
        self.actor = Actor('bird')
        self.actor.x = WIDTH // 2
        self.actor.y = HEIGHT - 100
        self.vel_y = 0
        self.jumping = False
        self.speed = 5
        self.jump_power = 12
        self.gravity = 0.8
        self.score = 0
    
    def update(self):
        if keyboard.left:
            self.actor.x -= self.speed
        if keyboard.right:
            self.actor.x += self.speed
        
        self.vel_y += self.gravity
        self.actor.y += self.vel_y
        
        self.actor.x = max(20, min(WIDTH - 20, self.actor.x))
    
    def handle_collision(self, platform):
        platform_x = platform.actor.x
        platform_y = platform.actor.y
        
        platform_width = platform.actor.width
        
        platform_top = platform_y - platform.actor.height // 2
        
        distance_x = self.actor.x - platform_x
        if distance_x < 0:
            distance_x = -distance_x
        
        if distance_x > 20 + platform_width // 2:
            return False
        
    
        player_bottom = self.actor.y + 20
        
        if player_bottom < platform_top or self.actor.y - 20 > platform_top:
            return False
        
        if self.vel_y <= 0:
            return False
        
        self.actor.y = platform_top - 20
        self.vel_y = 0
        self.jumping = False
        return True
    
    def jump(self):
        if not self.jumping:
            self.vel_y = -self.jump_power
            self.jumping = True
    
    def check_coin_collision(self, coin):
        if not coin.collected and self.actor.colliderect(coin.actor):
            coin.collected = True
            self.score += 1
            return True
        return False
    
    def check_fall(self):
        return self.actor.y > HEIGHT + 100
    
    def reset(self):
        self.actor.x = WIDTH // 2
        self.actor.y = HEIGHT - 100
        self.vel_y = 0
        self.jumping = False
        self.score = 0
    
    def draw(self):
        self.actor.draw()

class Platform:
    def __init__(self, x, y):
        self.actor = Actor('stone', (x, y))
    
    def is_valid_position(self):
        return (50 < self.actor.y < HEIGHT - 50 and 
                50 < self.actor.x < WIDTH - 50)
    
    def draw(self):
        self.actor.draw()

class Coin:
    def __init__(self, platform):
        self.actor = Actor('coin', (platform.actor.x, platform.actor.y - 40))
        self.collected = False
        self.original_y = platform.actor.y - 40
    
    def update(self):
        if not self.collected:
            self.actor.y = self.original_y + math.sin(0.05 * 3) * 5
    
    def respawn(self, platforms):
        valid_platforms = [p for p in platforms if p.is_valid_position()]
        if valid_platforms:
            new_platform = random.choice(valid_platforms)
            self.actor.x = new_platform.actor.x
            self.actor.y = new_platform.actor.y - 40
            self.original_y = self.actor.y
            self.collected = False
    
    def draw(self):
        if not self.collected:
            self.actor.draw()


class Game:
    def __init__(self):
        self.player = Player()
        self.platforms = []
        self.coin = None
        self.generate_platforms()

    
    def generate_platforms(self):
        self.platforms.clear()
        
        self.platforms.append(Platform(WIDTH // 2, HEIGHT - 50))
        
        num_rows = random.randint(8, 10)
        vertical_spacing = 100
        
        for row in range(1, num_rows):
            y = HEIGHT - 50 - (row * vertical_spacing)
            
            if y < 50:
                break
                
            num_platforms_in_row = random.randint(2, 3)
            section_width = WIDTH // num_platforms_in_row
            
            for i in range(num_platforms_in_row):
                x = random.randint(
                    max(60, i * section_width + 50),
                    min(WIDTH - 60, (i + 1) * section_width - 50)
                )
                
                self.platforms.append(Platform(x, y))
        valid_platforms = [p for p in self.platforms if p.is_valid_position()]
        if valid_platforms:
            first_platform = random.choice(valid_platforms)
            self.coin = Coin(first_platform)
    
    def update(self):
        self.player.update()
        
        if self.coin:
            self.coin.update()
        on_ground = False
        for platform in self.platforms:
            if self.player.handle_collision(platform):
                on_ground = True
        
        self.player.jumping = not on_ground
        
        if keyboard.space and not self.player.jumping:
            self.player.jump()
        
        if self.coin and self.player.check_coin_collision(self.coin):
            self.coin.respawn(self.platforms)
        
        if self.player.check_fall():
            self.reset()
    
    def reset(self):
        self.player.reset()
        self.generate_platforms()
    
    def draw(self):
        screen.clear()
        screen.fill((135, 206, 235))
        
        for platform in self.platforms:
            platform.draw()
        
        if self.coin:
            self.coin.draw()
        
        self.player.draw()
        
        screen.draw.text(f"Монетки: {self.player.score}", (10, 10), fontsize=30, color="white")



game = Game()

def update():
    game.update()

def draw():
    game.draw()

pgzrun.go()