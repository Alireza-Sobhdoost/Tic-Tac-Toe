# Tic-Tac-Toe with MCTS-based Reinforcement Learning Agents

[![Language: Python](https://img.shields.io/badge/language-Python-3776ab?logo=python&logoColor=white)](https://www.python.org)
[![Topic: Reinforcement Learning](https://img.shields.io/badge/topic-Reinforcement%20Learning-blue)](#)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](#)


Welcome to the **Tic-Tac-Toe** project!  
This repository features a Tic-Tac-Toe game implementation that utilizes advanced AI techniques for autonomous gameplay and learning.

## Features

- **Classic Tic-Tac-Toe Game**: Play the timeless 3x3 game in your terminal or through a UI (if provided).
- **MCTS Algorithm**: The AI agents in this project are powered by the Monte Carlo Tree Search (MCTS) algorithm, a popular method in reinforcement learning (RL). MCTS enables agents to intelligently simulate possible future moves, evaluating the game tree to select the most promising action at each step.
- **Reinforcement Learning Agents**: Our implementation leverages RL principles, allowing the AI to improve its gameplay through simulated self-play and experience.

## What is MCTS?

**Monte Carlo Tree Search (MCTS)** is a search algorithm used extensively in game AI, especially for decision-making in environments with large or complex state spaces. It works by:

1. **Selection**: Traversing the tree to select a promising node.
2. **Expansion**: Expanding the tree by adding a new child node.
3. **Simulation**: Running random simulations (playouts) from the new node.
4. **Backpropagation**: Propagating the results of the simulation up the tree to update node statistics.

Through repeated simulations, MCTS builds a statistical model of the best moves, making it highly effective for games like Tic-Tac-Toe.

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Alireza-Sobhdoost/Tic-Tac-Toe.git
   cd Tic-Tac-Toe
   ```

2. **Install dependencies:**
   ```bash
   uv pip install -r req.txt
   ```

3. **Run the game:**
   ```bash
   python src/Main.py <Num_Of_Iterates>
   ```

   Or if you're on Linux and prefer a binary release:
   ```bash
   ./MCTSXO <Num_Of_Iterates>
   ```

## Project Structure

```
- src/Main.py        # Entry point for running the game
- src/Mcts.py        # MCTS-based RL agent implementation
- src/Game.py        # A CLI version of the Game 
- src/Board.py       # Game Board logic and utils
```

## Contributions

Contributions and suggestions are welcome! Please open issues or submit pull requests.

## License

This project is licensed under the MIT License.

---

Enjoy playing against a smart RL agent powered by MCTS!
