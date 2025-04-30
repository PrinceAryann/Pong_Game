from turtle import Turtle

SCORE = 0  # Global variable to track the score (not used directly in the class)

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()  # Hide the turtle cursor
        self.pu()  # Lift the pen
        self.color("white")  # Set the color for the scoreboard
        self.l_score = 0  # Left player score
        self.r_score = 0  # Right player score
        self.display()  # Display initial scores
    
    def display(self):
        """Display the current scores on the screen"""
        self.clear()  # Clear previous score display
        self.goto(-100, 200)  # Position the left score
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))  # Write left score
        self.goto(100, 200)  # Position the right score
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))  # Write right score
    
    def l_increment(self):
        """Increment left player's score and update the display"""
        self.l_score += 1
        self.display()

    def r_increment(self):
        """Increment right player's score and update the display"""
        self.r_score += 1
        self.display()
