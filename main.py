from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
which_color = 0
y_position = -100

screen = Screen()
screen.setup(width=500, height=400)


def create_turtle():
    global which_color
    global y_position
    turtle_name = Turtle(shape="turtle")
    turtle_name.penup()
    turtle_name.color(colors[which_color])
    which_color += 1
    turtle_name.setposition(x=-230, y=y_position)
    y_position += 40
    return turtle_name


puck = create_turtle()
duck = create_turtle()
muck = create_turtle()
luck = create_turtle()
tuck = create_turtle()
huck = create_turtle()

bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? (pick a color)").lower()
turtles = [puck, duck, muck, luck, tuck, huck]

end_of_race = False
while not end_of_race:
    for turtle in turtles:
        if not end_of_race:
            step = random.randint(0, 10)
            turtle.forward(step)
            if turtle.xcor() >= 220:
                end_of_race = True
                winner = turtle
                if winner == bet:
                    print(f"You win :)\nThe winner is the {winner.pencolor()} turtle indeed ^-^")
                else:
                    print(f"You lose :(\nThe winner is the {winner.pencolor()} turtle")


screen.exitonclick()
