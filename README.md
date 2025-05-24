<img width="389" alt="image" src="https://github.com/user-attachments/assets/1ef8274f-2d06-4119-b6bc-09ac516ed051" />

# Snake Game 🚀
***A slithering adventure in Python and Pygame!***
<p align="center">
  <img width="350" src="https://github.com/user-attachments/assets/1ef8274f-2d06-4119-b6bc-09ac516ed051" alt="Snake Game Logo"/>
</p>

<h1 align="center">🐍 SNAKE GAME <br><sup><sub>by Snake Enthusiasts</sub></sup></h1>

<p align="center">
  <b>A slithering adventure in Python and Pygame!</b><br>
  <img src="https://img.shields.io/badge/python-3.10+-blue"/>
  <img src="https://img.shields.io/badge/pygame-2.1+-green"/>
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg"/>
</p>

<pre align="center">
     /^\/^\
   _|__|  O|
 \/     \/ \|
  \  ___  /  |
   \/   \/\  |
      ||   ||
      ||   ||
</pre>

---

<p align="center">
  <img src="assets/images/gameplay.gif" width="500" alt="Gameplay Preview"/>
</p>

## 🎮 Live Demo (Local Preview)
![Gameplay Preview](assets/images/gameplay.gif)

## 🗺️ Table of Contents
- [Features](#features)
- [Screenshots & Assets](#screenshots--assets)
- [High Score System](#high-score-system)
- [Technologies & Requirements](#technologies--requirements)
- [Setup & Installation](#setup--installation)
- [How to Play](#how-to-play)
- [Showcase](#showcase)
- [FAQ](#faq)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [Credits](#credits)

## ✨ Features
- Classic snake gameplay with smooth controls and dynamic speed.
- Grow, survive, and set new records! 🏆
- Persistent <b>High Score</b> saved across sessions.
- Customizable assets: swap images & sounds easily.
- Restart or quit on Game Over.
- Sound effects for eating and game over.
- <b>Beautiful retro visuals!</b>

## 🖼️ Screenshots & Assets
Assets are organized under <code>assets/images</code> and <code>assets/sounds</code>.

| ![Snake](assets/images/snake.png) | ![Food](assets/images/food.png) |
|:---:|:---:|
| Snake Sprite | Food Sprite |

- <code>assets/images/gameplay.gif</code>: Animated demo.
- <code>assets/sounds/eat.wav</code>, <code>gameover.wav</code>: Sound effects for added immersion.

## 🏅 High Score System
A persistent <b>HighScore</b> module stores your best score in <code>highscore.txt</code>.<br>
Each game updates the record if you beat your previous best! 🔥

## 🛠️ Technologies & Requirements
- Python 3.10+
- Pygame 2.1+

All dependencies are tracked in <code>requirements.txt</code>:

```bash
pygame>=2.1
```

## 🚀 Setup & Installation
<details>
<summary>Step-by-step Guide</summary>

1. <b>Clone the repository:</b>
   
   ```bash
   git clone &lt;repository-url&gt;
   cd snake-game
   ```
2. <b>Install dependencies:</b>
   
   ```bash
   pip install -r requirements.txt
   ```
3. <b>Add your custom assets (optional):</b>
   - Place <code>.png</code> sprites in <code>assets/images/</code>.
   - Place <code>.wav</code> files in <code>assets/sounds/</code>.
4. <b>Run the game:</b>
   
   ```bash
   cd code
   python main.py
   ```
</details>

## 🎮 How to Play
- <b>Arrow Keys</b> or <b>WASD</b> to move the snake.
- Eat the red blocks to grow and earn points.
- Avoid walls and your own tail.
- <b>R</b> to Restart, <b>Q</b> to Quit on Game Over.

<details>
<summary>Pro Tips & Fun Facts</summary>

- The snake gets faster as you grow!
- Try to beat your high score and share a screenshot in the [Showcase](SHOWCASE.md)!
- Customize your snake with your own sprites.
</details>

## 🌟 Showcase
See [SHOWCASE.md](SHOWCASE.md) for high scores, fan art, and community creations!

## ❓ FAQ
See [FAQ.md](FAQ.md) for common questions and answers.

## 🚧 Future Enhancements
- <b>Difficulty Levels:</b> Easy, Medium, Hard.
- <b>Obstacles:</b> Random barriers on the map.
- <b>Skins:</b> Unlockable snake appearances.
- <b>Power-ups:</b> Speed boost, score multipliers.
- <b>Mobile Support:</b> Touch controls for on-the-go fun.
- <b>Controller Support:</b> Play with a gamepad!

## 🤝 Contributing
We love contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for how to get started.

## 📝 Credits
Created with ❤️ by Snake Enthusiasts.<br>
See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for community guidelines.

---

<p align="center">
  <b>Ready to slither? Run <code>python main.py</code> and let the fun begin!</b>
</p>

