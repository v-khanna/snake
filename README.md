# Snake Game

A classic Snake game implemented in Python using Pygame. Guide your snake to eat food, grow longer, and avoid colliding with itself. The game includes features like screen wrapping and high score saving.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [How to Run the Game](#how-to-run-the-game)
- [How to Play](#how-to-play)
- [Game Rules](#game-rules)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [Credits](#credits)
- [License](#license)

## Features

- **Classic Gameplay**: Enjoy the traditional snake game mechanics.
- **Screen Wrapping**: The snake wraps around the screen edges instead of the game ending.
- **Persistent High Score**: Your high score is saved between game sessions.
- **Simple Controls**: Easy-to-use keyboard controls.
- **Customizable Settings**: Modify game speed, colors, and screen size.

## Installation

Follow these steps to set up and run the game on your computer.

### Prerequisites

- **Python 3.x**: Download and install Python from the [official website](https://www.python.org/downloads/).
- **Pygame Library**: A set of Python modules designed for writing video games.

### Steps

1. **Install Python**

   - Download Python 3.x from [python.org](https://www.python.org/downloads/).
   - Install Python and ensure that the option to add Python to your system PATH is selected.

2. **Install Pygame**

   - Open your command prompt (Windows) or terminal (macOS/Linux).
   - Run the following command to install Pygame:
     ```bash
     pip install pygame
     ```

3. **Download the Game Code**

   - Create a new directory for the game.
   - Save the `snake_game.py` file into this directory. *(Copy the game code provided into this file.)*

4. **(Optional) Verify Installation**

   - To check if Pygame is installed correctly, run:
     ```bash
     python -m pygame.examples.aliens
     ```

## How to Run the Game

1. **Navigate to the Game Directory**

   - Open the command prompt or terminal.
   - Change the directory to where `snake_game.py` is saved:
     ```bash
     cd path_to_your_game_directory
     ```

2. **Run the Game Script**

   - Execute the game by running:
     ```bash
     python snake_game.py
     ```

3. **Start Playing**

   - The game window should open, displaying the main menu.

## How to Play

### Controls

- **Arrow Keys**: Use the Up, Down, Left, and Right arrow keys to control the direction of the snake.
  - **Up Arrow**: Move up
  - **Down Arrow**: Move down
  - **Left Arrow**: Move left
  - **Right Arrow**: Move right
- **Menu Navigation**:
  - **S Key**: Start the game from the main menu.
  - **H Key**: View the high score.
  - **Q Key**: Quit the game.
  - **B Key**: Go back to the main menu from the high score screen.
  - **C Key**: Continue playing after a game over.
  - **Q Key**: Quit after a game over.

### Objective

- **Eat Food**: Guide the snake to the red square (food) to eat it.
- **Grow Longer**: Each time the snake eats food, it grows longer.
- **Score Points**: Your score increases by one for each food item consumed.
- **Achieve High Score**: Try to beat the previous high score saved from earlier sessions.

## Game Rules

- **Avoid Collisions**: Do not let the snake collide with itself; otherwise, the game will end.
- **Screen Wrapping**: If the snake moves off one edge of the screen, it will appear on the opposite side.
- **Increasing Difficulty**: The snake's speed remains constant, but managing a longer snake becomes more challenging.

## Customization

You can customize various aspects of the game by modifying the `snake_game.py` file:

- **Snake Speed**: Adjust the `snake_speed` variable.
- **Screen Size**: Modify `SCREEN_WIDTH` and `SCREEN_HEIGHT`.
- **Colors**: Change the RGB values in the `Colors` section.
- **Snake Size**: Alter the `snake_block` variable for a larger or smaller snake.

## Troubleshooting

- **Pygame Not Found**: Ensure Pygame is installed correctly. Run `pip install pygame` and make sure you're using the correct version of Python.
- **Python Command Not Found**: Add Python to your system's PATH environment variable or use the full path to the Python executable.
- **Game Window Not Opening**: Check for any error messages in the terminal and ensure all dependencies are installed.

## Credits

- **Developer**: Vir Khanna
- **Inspiration**: Classic Snake game concept.
- **Libraries Used**: [Pygame](https://www.pygame.org/news)

### yes, of course that is my real high score

## License

This project is licensed under the [MIT License](LICENSE).

---

**Enjoy playing the Snake Game! If you have any feedback or encounter issues, please feel free to contribute or report them.**