# Import Turtle and Screen classes from turtle module
from turtle import Turtle, Screen
# Import random module
import random
# Define race conditions
race_started = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtle_list = []
# Create instances of different colored turtles to arrive at starting line
for turtle_index in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[turtle_index])
    turtle.pu()
    turtle.goto(-230, y_positions[turtle_index])
    turtle_list.append(turtle)
# Wait for user bet input before starting the race
if user_bet:
    race_started = True
# While loop to create race actions
while race_started:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
                exit()
            if winning_color != user_bet:
                print(f"You've lost! The {winning_color} turtle is the winner!")
                exit()
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
# Program will exit if user clicks on screen
screen.exitonclick()
