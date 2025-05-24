<img width="389" alt="image" src="https://github.com/user-attachments/assets/1ef8274f-2d06-4119-b6bc-09ac516ed051" />

# Snake Game 🚀
- ***A slithering adventure in Python and Pygame!***

```
     /^\/^\
   _|__|  O|
 \/     \/ \|
  \  ___  /  |
   \/   \/\  |
      ||   ||
      ||   ||
```

[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/pygame-2.1+-green)](https://www.pygame.org/news)

## 🎮 Live Demo (Local Preview)
![Gameplay Preview](assets/images/gameplay.gif)

## Table of Contents
- [Features](#features)
- [Screenshots & Assets](#screenshots--assets)
- [High Score System](#high-score-system)
- [Technologies & Requirements](#technologies--requirements)
- [Setup & Installation](#setup--installation)
- [How to Play](#how-to-play)
- [Future Enhancements](#future-enhancements)
- [Credits](#credits)

## Features
- Classic snake gameplay with smooth controls and dynamic speed.
- Grow, survive, and set new records! 🏆
- Persistent **High Score** saved across sessions.
- Customizable assets: swap images & sounds easily.
- Restart or quit on Game Over.

## Screenshots & Assets
Assets are organized under `assets/images` and `assets/sounds`.
- `assets/images/gameplay.gif`: Animated demo.
- `assets/images/snake.png`, `food.png`: Optional custom sprites.
- `assets/sounds/eat.wav`, `gameover.wav`: Sound effects for added immersion.

## High Score System
A persistent **HighScore** module stores your best score in `highscore.txt`.
Each game updates the record if you beat your previous best! 🔥

## Technologies & Requirements
- Python 3.10+
- Pygame 2.1+

All dependencies are tracked in `requirements.txt`:

```bash
pygame>=2.1
```

## Setup & Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd snake-game
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your custom assets (optional):
   - Place `.png` sprites in `assets/images/`.
   - Place `.wav` files in `assets/sounds/`.
4. Run the game:
   ```bash
   cd code
   python main.py
   ```

## How to Play
- **Arrow Keys** or **WASD** to move the snake.
- Eat the red blocks to grow and earn points.
- Avoid walls and your own tail.
- **R** to Restart, **Q** to Quit on Game Over.

## Future Enhancements
- **Difficulty Levels**: Easy, Medium, Hard.
- **Obstacles**: Random barriers on the map.
- **Skins**: Unlockable snake appearances.
- **Power-ups**: Speed boost, score multipliers.
- **Mobile Support**: Touch controls for on-the-go fun.

## Credits
Created with ❤️ by Snake Enthusiasts.
Contributions welcome! 🐍

