import turtle
def draw_square():
    window=turtle.Screen()
    window.bgcolor("red")
    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(10)

    for i in range(36):
        
        for n in range(4):
            brad.forward(100)
            brad.right(90)
        brad.right(10)
    
    window.exitonclick()

draw_square()
