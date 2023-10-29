from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.penup()
        self.hideturtle()
        self.l_score = 0  # Initialize the player's score to zero
        self.update_scoreboard()  # Call the initial scoreboard update

    def update_scoreboard(self):
        """
        Update the scoreboard with the player's score.
        """
        self.clear()  # Clear the previous score display
        self.goto(200, 180)  # Set the position of the score display
        self.write(f"{self.l_score}/50", align="center", font=("Courier", 40, "normal"))

    def add_score(self):
        """
        Increase the player's score by 1 and update the scoreboard.
        """
        self.l_score += 1  # Increment the player's score by 1
        self.update_scoreboard()  # Update the scoreboard with the new score
