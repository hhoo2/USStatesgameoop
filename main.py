# Import necessary modules and classes
from timer import Timer  # Import the Timer class for managing the game timer
import turtle  # Import the turtle graphics library for drawing
import pandas as pd  # Import pandas for working with data
from scoreBoard import Scoreboard  # Import the Scoreboard class for keeping score

# Set up the turtle screen and load the background image
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read the state data from the CSV file
data = pd.read_csv('50_states.csv')

# Create a set to keep track of guessed states
guessed_states = set()

# Create a Scoreboard object to keep track of the player's score
score = Scoreboard()

# Initialize the game timer with a 10-minute countdown (600 seconds)
# Start the game timer
game_timer = Timer(600)
game_timer.start()

# Main game loop: Continue until all states are guessed or the timer runs out
while len(guessed_states) < len(data):
    # Check if the game timer has run out, end the game if timer run out
    if game_timer.check_time_out():
        break

    #prompt the user to enter a state name
    title = "Guess the State"
    prompt = "What's another state's name?"
    answer_state = screen.textinput(title=title, prompt=prompt).title()

    # Exit the game if the user enters "exit"
    if answer_state.lower() == 'exit':
        break

    # Check if the user's answer is a valid state name
    if answer_state in data['state'].values:
        if answer_state not in guessed_states:
            # If the answer is correct and hasn't been guessed before, the state name will show on the map
            guessed_states.add(answer_state)
            x = data.loc[data['state'] == answer_state, 'x'].values[0]
            y = data.loc[data['state'] == answer_state, 'y'].values[0]
            state_turtle = turtle.Turtle()
            state_turtle.penup()
            state_turtle.goto(x, y)
            state_turtle.write(answer_state, align="center")
            state_turtle.hideturtle()
            score.add_score()  # Increase the player's score
        else:
            print(f"You already guessed {answer_state}. Try another state.")
    else:
        print("That's not a valid state. Try again or type 'exit' to quit.")

# Check if the user guessed all 50 states
if len(guessed_states) == len(data):
    print("Congratulations! You guessed all 50 states!")

# Close the turtle graphics window when clicked
screen.exitonclick()
io