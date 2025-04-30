from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")  # Set the ball color
        self.shape("circle")  # Set the ball shape to circle
        self.pu()  # Lift the pen so the ball doesn't draw
        self.x_move = 10  # Initial movement speed on the x-axis
        self.y_move = 10  # Initial movement speed on the y-axis
        self.pace = 0.1  # The time delay between each movement (game speed)

    def move(self):
        """Move the ball in the current direction (x_move, y_move)"""
        new_x = self.xcor() + self.x_move  # Calculate new x position
        new_y = self.ycor() + self.y_move  # Calculate new y position
        self.goto(new_x, new_y)  # Move the ball to the new position
    
    def bounce_y(self):
        """Bounce the ball in the y direction"""
        self.y_move *= -1  # Reverse the direction of y-axis movement

    def bounce_x(self):
        """Bounce the ball in the x direction and speed up over time"""
        self.x_move *= -1  # Reverse the direction of x-axis movement
        if self.pace > 0.03:  # Increase game speed after each bounce
            self.pace *= 0.9

    def reset_position(self):
        """Reset the ball to the center of the screen"""
        self.goto(0, 0)  # Move the ball back to the center
        self.bounce_x()  # Reverse the x direction after reset
        self.pace = 0.1  # Reset the pace (game speed)
