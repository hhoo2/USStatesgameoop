# U.S. States Game
## Introduction
Author -  Hay Oo
  
Welcome to the U.S. States Game! This Python-based game challenges you to guess the names of all 50 U.S. states on a blank map of the United States. The game includes a timer and a score tracker to add an element of challenge and fun.

![alt text](/program.png)

<b><a href="https://replit.com/@HayOo1/OOP-US-States-Game" style="color:purple;">Click here to play this program in Replit</a></b>

## Getting Started

Follow these step-by-step instructions to get started with the U.S. States Game:

### 1. Clone the Repository

First, clone this GitHub repository to your computer using the following command in your terminal:

```bash
git clone https://github.com/yourusername/us-states-game.git
```

Alternatively, you can download the source code files as a ZIP archive and extract them to a folder on your computer.

### 2. Install Python

Ensure that you have Python installed on your computer. If you don't have Python installed, you can download it from the official Python website: [python.org](https://www.python.org/downloads/).

### 3. Install Required Packages

Open a terminal or command prompt and navigate to the directory where you cloned or extracted the repository. Install the required Python packages using `pip`:

```bash
pip install pandas turtle
```

### 4. Prepare the Data

Make sure you have the `50_states.csv` data file in the same directory as the game script (`us_states_game.py`). This CSV file contains information about U.S. states, including their names and coordinates.

### 5. Run the Game

To start the game, run the Python script `us_states_game.py` by executing the following command in your terminal:

```bash
python us_states_game.py
```

## How to Play

Once the game is running, follow these steps to play:

1. The game window will open with a blank map of the United States.

2. Guess the names of U.S. states one by one. Type the state's name and press Enter. If your guess is correct, the state's name will appear on the map.

3. If you want to exit the game at any time, simply type 'exit' and press Enter.

4. You have a 10-minute time limit to guess all 50 states. The timer will start automatically when you begin the game.

5. Keep guessing until you've guessed all the states or the timer runs out.

6. If you successfully guess all 50 states, you win!

## Custom Classes

### `Timer` Class

The `Timer` class is used to manage the game timer. It starts counting down when you begin the game and checks if the time has run out.

### `Scoreboard` Class

The `Scoreboard` class keeps track of your score as you guess states correctly. It increases your score and displays it on the screen.

## Data Source

The game uses data from the `50_states.csv` file to validate your guesses and display the correct state names on the map. The CSV file contains information about each state's name and coordinates.

## Acknowledgments

This game was created for educational and entertainment purposes and was inspired by various programming tutorials and projects.

Enjoy the U.S. States Game, and have fun testing your knowledge of U.S. geography! If you have any feedback or suggestions for improvement, feel free to submit an issue or pull request on GitHub.

```
