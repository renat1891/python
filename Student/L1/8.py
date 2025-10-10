# from turtle import*
# speed(1)
# begin_fill()
# fillcolor("red")
# goto(100, 0)
# goto(100, 50)
# goto(0, 50)
# goto(0, 0)
# end_fill()

# goto(0, 50)
# begin_fill()
# fillcolor("white")
# goto(100, 50)
# goto(100, 100)
# goto(0, 100)
# goto(0, 50)
# end_fill()

# mainloop()



# from turtle import*

# speed(10)
# begin_fill()
# fillcolor("blue")
# for i in range(5):
#     begin_fill()
#     fillcolor("blue")
#     forward(200)   
#     right(144) 
#     end_fill()


# mainloop()

# from turtle import*
# size = 50   
# for i in range(4):  
#     penup()
#     goto(-size/2, -size/2)  
#     pendown()
#     for j in range(4):
#         forward(size)
#         left(90)
#     size += 50  

# mainloop()

from turtle import *

size = 50

# for i in range(4):  
#     penup()
#     goto(0, -size/2)   
#     setheading(45)     
#     pendown()
#     for j in range(4):
#         forward(size)
#         left(90)
#     size += 50  
# mainloop()

# from turtle import *

# color("blue")
# pensize(3)
# shape('turtle')
# speed(0)

# size = 100  

# for j in range(4):
#     begin_fill()
#     fillcolor("green")
#     setheading(0)  
    
#     for i in range(3):
#         forward(size)
#         left(120)
    
#     end_fill()
#     penup()
#     forward(size)  
#     pendown()

# mainloop()

# from turtle import * 
# color("blue")
# pensize(5)
# shape('turtle')
# speed(7)
# for j in range(4):
#     left(45)
#     begin_fill()
#     fillcolor("green")

#     for i in range(4):

#         forward(100)
#         left(90)
#     end_fill()
#     penup()
#     right(45)
#     forward(100)
#     pendown()
    
# mainloop()
# from turtle import *

# color("blue")
# pensize(5)
# shape('turtle')
# speed(0)

# for j in range(4):
#     left(30)

#     for i in range(3):  
#         forward(100)
#         left(120)
    
#     penup()
#     right(30)
#     forward(50)
#     pendown()
    
# mainloop()


# from turtle import *
# speed(0)
# size = 200   
# sides = 8    
# shift = 0    
# colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# while sides >= 3:
#     penup()
#     goto(0, -size/2 + shift)
#     # setheading(0)
#     pendown()
    
#     fillcolor(colors[8 - sides])  
#     begin_fill()
#     for _ in range(sides):
#         forward(size)
#         left(360 / sides)
#     end_fill()
    
#     # size -= 20
#     sides -= 1
#     # shift += 10
# mainloop()




# from turtle import*
# num_lines = 7
# line_length = 100
# gap = 30

# for i in range(num_lines):
#     goto(i * gap, 0)  
#     pendown()
#     setheading(90)
#     forward(line_length - i * 15)
#     penup()
# mainloop()


# from turtle import *
# import random
# color("blue")


# num_steps = 600

# for _ in range(num_steps):
#     step_length = random.randint(1, 10) 
#     turn_angle = random.uniform(-180, 180) 
#     left(turn_angle)
#     forward(step_length)
# mainloop()

# from turtle import *

# speed(0)
# length = 5
# angle = 30

# for i in range(200):
#     forward(length)
#     left(angle)
#     length += 3 
# mainloop()



