# Classic Snake Game

A Python implementation of the classic Snake game using the Pygame library.

## Table of Contents
- [Features](#features)
- [Screenshots](#screenshots)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [How to Play](#how-to-play)
- [Future Enhancements](#future-enhancements)

## Features
- Classic snake gameplay: control a snake to eat food and grow longer.
- Increasing difficulty: the snake grows with each piece of food eaten.
- Collision detection: game ends if the snake hits the walls or its own body.
- Score tracking: displays the current score.
- Restart option: allows playing again after a game over.
- Simple and intuitive controls.

## Screenshots
*(Add a GIF or screenshots of your game in action here!)*

**Example Screenshot Placeholder:**
![Snake Game Screenshot](https://via.placeholder.com/600x400.png?text=Snake+Game+In+Action)
*Replace the above URL with a link to an actual screenshot of your game.*

## Technologies Used
- **Python 3**: Core programming language.
- **Pygame**: A cross-platform set of Python modules designed for writing video games.

## Project Structure
The project is organized into several Python files within the `code/` directory:
```
/Users/venom/snake-game/
├── code/
│   ├── main.py             # Main script to run the game
│   ├── game.py             # Game class, handles main game loop and logic
│   ├── snake.py            # Snake class, manages snake behavior
│   ├── food.py             # Food class, manages food properties
│   ├── score.py            # Score class, manages score display
│   └── constants.py        # Stores all constant values (colors, screen size, etc.)
└── README.md               # This file
```

## Setup and Installation
1.  **Clone the repository (or download the files):**
    ```bash
    # If you were using Git
    # git clone <repository-url>
    # cd snake-game
    ```
    Ensure all files are within a directory, for example, `snake-game/`. The Python scripts should be inside a `code/` subdirectory as shown in the Project Structure.

2.  **Install Pygame:**
    If you don't have Pygame installed, you can install it using pip:
    ```bash
    pip install pygame
    ```

3.  **Navigate to the code directory:**
    Open your terminal or command prompt and navigate to the `code` directory where `main.py` is located.
    ```bash
    cd /path/to/your/snake-game/code/
    ```
    Replace `/path/to/your/snake-game/` with the actual path to where you've saved the project. For example, if your project is in `/Users/venom/snake-game/`, you would use:
    ```bash
    cd /Users/venom/snake-game/code/
    ```

4.  **Run the game:**
    Execute the `main.py` script:
    ```bash
    python main.py
    ```

## How to Play
-   Use the **Arrow Keys** (Up, Down, Left, Right) or **WASD Keys** to control the direction of the snake.
-   The objective is to eat the **red food blocks** that appear on the screen.
-   Each time the snake eats food, it grows longer, and your score increases.
-   The game ends if the snake collides with the boundaries of the game window or with its own body.
-   After a "Game Over", you can press:
    -   **R** to Restart the game.
    -   **Q** to Quit the game.

## Future Enhancements
-   Different difficulty levels (e.g., faster snake, more obstacles).
-   High score saving and display.
-   Power-ups (e.g., temporarily slow down, shrink snake).
-   Sound effects and background music.
-   More visual themes or skins for the snake and food.

---

Enjoy the game!

