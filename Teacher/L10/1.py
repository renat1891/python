import pgzrun

WIDTH = 600
HEIGHT = 400

def draw():
    screen.draw.line((100, 100), (200, 200), "red")
    screen.draw.circle((300, 200), 50, "blue")
    screen.draw.filled_circle((500, 200), 50, "blue")
    screen.draw.rect(Rect((100, 300), (50, 50)), "green")
    screen.draw.filled_rect(Rect((200, 300), (50, 50)), "green")
    screen.draw.text("Hello, Pygame Zero!", (200, 50), color="white", fontsize=40)



def update():
    ...


pgzrun.go()