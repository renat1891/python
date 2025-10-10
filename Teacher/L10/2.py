import pgzrun

WIDTH = 600
HEIGHT = 400

circle = {
    "x": 100,
    "y": 100,
    "radius": 10,
    "color": "blue",
    "speedX": 3,
    "speedY": 3
}

def draw():
    screen.clear()
    screen.draw.filled_circle((circle["x"], circle["y"]), circle["radius"], circle["color"])


def update():
    circle["x"] += circle["speedX"]
    # circle["y"] += circle["speedY"]

    if circle["x"] > WIDTH:
        circle["speedX"] = -circle["speedX"]


pgzrun.go()