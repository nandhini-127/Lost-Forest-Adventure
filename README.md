# 🌲 Adventure of the Lost Forest 🌲  
**AI-Based Interactive Storytelling Game using Python and Pygame**

## 📖 Introduction
"**Adventure of the Lost Forest**" is an interactive, text-based storytelling game where the player explores a mystical forest. Built using **Python** and **Pygame**, this game allows players to make decisions that directly affect how the story unfolds. Each decision influences the path, leading to different endings and outcomes.

This project demonstrates the power of **interactive storytelling** through simple **AI-driven choice tracking** and **state-based decision logic**.

---

## 🤖 AI Algorithm Involved

Though simple, the AI in this game simulates decision-making using rule-based systems:

- **Choice Tracking:** Remembers user decisions and adjusts the story accordingly.
- **State Transitions:** Each choice leads to a new game state (e.g., lake, exit path).
- **Decision Tree Logic:** Player input maps to specific branches in the narrative.

---

## 🛠 Tools and Technologies

- **Python 3**
- **Pygame Library**

---

## 🔁 Game Flow

```plaintext
Start
 |
 v
[INTRO: Enter Forest? (Y/N)]
 |           |
 |           v
 |       [GAME OVER]
 v
[FOREST: Follow Light? (Y/N)]
 |           |
 v           v
[LAKE]    [EXIT PATH]
 |           |
 |           v
 |       [GAME OVER]
 v
[LAKE: Drink or Talk? (1/2)]
 |         |
 v         v
[MAGIC] [KNOWLEDGE]
 |         |
 v         v
[GAME OVER]

```

## 📌 Conclusion

- This mini-project successfully showcases how **narrative logic**, **decision trees**, and **basic AI concepts** can be used to build an immersive storytelling game.

Through this project, you will learn:
- Event-driven game loops
- Handling user input and transitions
- Building state machines for game storytelling
- Applying logic to create different endings

---

## 🔮 Future Enhancements

- Add images, sound effects, and background music for richer immersion
- Expand story branches and add more choices or puzzles for replayability
- Implement save/load game state functionality
- Improve AI with memory-based decisions or sentiment-scoring mechanisms

## 📂 How to Run

### 1. Install dependencies

```bash
pip install pygame
```

### 2. Run the game

```bash
python lost_forest.py
```
## License
- This project is open-source and free to use under the MIT License.

## Author
- Developed by Nandhini S S



