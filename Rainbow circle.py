import turtle
colors=['red','blue','purple','green','orange','yellow']
loadWindow=turtle.Screen()
turtle.speed(50)
for i in range(20):
    turtle.circle(10*i)
    turtle.circle(-10*i)
    turtle.left(i)
    turtle.pencolor(colors[i%6])
    turtle.width(i//100+1)
    turtle.forward(i)
    turtle.left(59)
    turtle.fillcolor("orange")
    turtle.pensize(10)
    turtle.shape("circle")
    turtle.bgcolor('black')

turtle.exitonclick()