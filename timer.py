from turtle import RawTurtle, Screen
import time

class Timer(RawTurtle):
    def __init__(self, duration):
        """
        Initializes the Timer object with a specified duration.

        Args:
            duration (int): The duration of the timer in seconds.
        """
        super().__init__(Screen())
        self.duration = duration
        self.end_time = time.time() + duration
        self.color("red")
        self.penup()
        self.hideturtle()
        self.goto(170, -200)  # Adjust the position to the upper center

    def update_timer_display(self):
        """
        Updates the timer display with the remaining time.
        """
        remaining_time = max(0, int(self.end_time - time.time()))
        minutes, seconds = divmod(remaining_time, 60)
        self.clear()
        self.write(f"Time remaining: {minutes:02d}:{seconds:02d}", align="center", font=("Arial", 24, "normal"))
        if remaining_time > 0:
            self.screen.ontimer(self.update_timer_display, 1000)  # Update every 1000 milliseconds (1 second)
        else:
            self.clear()
            self.write("Timer finished!", align="center", font=("Arial", 24, "normal"))

    def start(self):
        """
        Starts the timer and initiates the countdown display.
        """
        self.update_timer_display()

    def check_time_out(self):
        """
        Checks if the timer has run out.

        Returns:
            bool: True if the timer has run out, False otherwise.
        """
        return self.end_time <= time.time()
