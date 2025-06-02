# Tic-Tac-Toe with MCTS-based Reinforcement Learning Agents

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

2. **Run the game:**
   ```bash
   python main.py
   ```

## Project Structure

```
- main.py                # Entry point for running the game
- mcts_agent.py          # MCTS-based RL agent implementation
- game.py                # Game logic and state representation
- README.md              # Project documentation
```

## Contributions

Contributions and suggestions are welcome! Please open issues or submit pull requests.

## License

This project is licensed under the MIT License.

---

Enjoy playing against a smart RL agent powered by MCTS!
