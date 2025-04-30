from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position) -> None:
        super().__init__()
        self.color("white")  # Set the paddle color
        self.speed(2)  # Set paddle movement speed
        self.shape("square")  # Use square shape for paddle
        self.shapesize(stretch_len=1, stretch_wid=5)  # Stretch the square to make it a rectangular paddle
        self.pu()  # Lift the pen so it doesn't draw
        self.goto(position)  # Move the paddle to the given position

    def go_up(self):
        """Move the paddle up, but not out of bounds"""
        if self.ycor() < 250:  # Prevent the paddle from going out of the top screen boundary
            new_y = self.ycor() + 20  # Move up by 20 units
            self.goto(self.xcor(), new_y)  # Update paddle position

    def go_down(self):
        """Move the paddle down, but not out of bounds"""
        if self.ycor() > -240:  # Prevent the paddle from going out of the bottom screen boundary
            new_y = self.ycor() - 20  # Move down by 20 units
            self.goto(self.xcor(), new_y)  # Update paddle position
