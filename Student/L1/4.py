from turtle import * 
color("blue")
pensize(5)
shape('turtle')
speed(0)
for j in range(4):
    left(45)
    begin_fill()
    fillcolor("green")

    for i in range(4):

        forward(100)
        left(90)
    end_fill()
    penup()
    right(45)
    forward(100)
    pendown()
    
mainloop()