
# import pgzrun

# WIDTH = 600
# HEIGHT = 400

# circle = {
#     "x": 100,
#     "y": 100,
#     "radius": 10,
#     "color": "blue",
#     "speedX": 3,
#     "speedY": 3
# }

# def draw():
#     screen.clear()
#     screen.draw.filled_circle((circle["x"], circle["y"]), circle["radius"], circle["color"])


# def update():
#     circle["x"] += circle["speedX"]
#     circle["y"] += circle["speedY"]

#     if circle["x"] > WIDTH or circle["x"] < 0:
#         circle["speedX"] = -circle["speedX"]
#     if  circle["y"] > HEIGHT or circle["y"] < 0:
#         circle["speedY"] = -circle["speedY"]
#         circle["radius"] += 10


# pgzrun.go()
 
# import pgzrun
# import random

# WIDTH = 600
# HEIGHT = 400

# circle = {
#     "x": 100,
#     "y": 100,
#     "radius": 10,
#     "color": "blue",
#     "speedX": 3,
#     "speedY": 3
# }

# trail = []  
# colors = ["red", "green", "blue", "yellow", "purple", "orange"]

# def draw():
#     screen.clear()
#     for t in trail:
#         screen.draw.filled_circle((t["x"], t["y"]), t["radius"], t["color"])
#     screen.draw.filled_circle((circle["x"], circle["y"]), circle["radius"], circle["color"])

# def update():
#     circle["x"] += circle["speedX"]
#     circle["y"] += circle["speedY"]

#     if circle["x"] > WIDTH or circle["x"] < 0:
#         circle["speedX"] = -circle["speedX"]
#         change_circle()
#     if circle["y"] > HEIGHT or circle["y"] < 0:
#         circle["speedY"] = -circle["speedY"]
#         change_circle()

#     trail.append({"x": circle["x"], "y": circle["y"], "radius": circle["radius"], "color": circle["color"]})
#     if len(trail) > 50:
#         trail.pop(0)

# def change_circle():
#     circle["color"] = random.choice(colors)
#     circle["radius"] = random.randint(5, 30)

# pgzrun.go()

