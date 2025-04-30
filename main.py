from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

RIGHT_PADDLE = (360, 0)  # Right paddle position
LEFT_PADDLE = (-360, 0)  # Left paddle position

s = Screen()  # Create a screen for the game
s.setup(width=800, height=600)  # Set screen size
s.bgcolor('black')  # Set background color to black
s.title("Pong Game")  # Set the window title
s.tracer(0)  # Turn off automatic screen updates for better performance

# Create the left and right paddles, the ball, and the scoreboard
l_paddle = Paddle(LEFT_PADDLE)
r_paddle = Paddle(RIGHT_PADDLE)
ball = Ball()
score = Scoreboard()

s.listen()  # Start listening for user input

# Set up key bindings to move paddles
s.onkeypress(l_paddle.go_up, "w")
s.onkeypress(l_paddle.go_down, "s")
s.onkeypress(l_paddle.go_up, "W")
s.onkeypress(l_paddle.go_down, "S")
s.onkeypress(r_paddle.go_up, "Up")
s.onkeypress(r_paddle.go_down, "Down")

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.pace)  # Delay between ball moves (game speed)
    s.update()  # Update the screen to reflect changes
    ball.move()  # Move the ball

    # Check for collisions with the right wall (point for left player)
    if ball.xcor() > 380:
        ball.reset_position()  # Reset the ball to the center
        score.l_increment()  # Increment left player's score

    # Check for collisions with the left wall (point for right player)
    if ball.xcor() < -380:
        ball.reset_position()  # Reset the ball to the center
        score.r_increment()  # Increment right player's score

    # Check for collisions with the top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()  # Bounce the ball vertically

    # Check for collisions with paddles
    if (ball.xcor() > 320 and ball.distance(r_paddle) < 50 and ball.ycor() < r_paddle.ycor() + 50 and ball.ycor() > r_paddle.ycor() - 50) or \
       (ball.xcor() < -320 and ball.distance(l_paddle) < 50 and ball.ycor() < l_paddle.ycor() + 50 and ball.ycor() > l_paddle.ycor() - 50):
        ball.bounce_x()  # Bounce the ball horizontally

# Exit when clicked
s.exitonclick()
 