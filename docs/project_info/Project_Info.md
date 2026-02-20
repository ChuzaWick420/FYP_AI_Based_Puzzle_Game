# Introduction
This project aims to develop a competitive maze-solving game where a human player competes against an AI rival. At the beginning, the maze is displayed fully for a few seconds, after which parts of it disappear. The player must rely on memory and strategy to find the exit. Simultaneously, the AI rival uses the A* Search Algorithm (Manhattan Distance heuristic) to navigate the maze efficiently.

The game tests human cognitive skills against algorithmic precision, providing engaging experience and demonstrating pathfinding, algorithm design, and AI vs human performance comparison. Additional complexity is introduced by multiple maze sizes, increasing difficulty levels, and power-ups that can help or hinder progress.

## Functional Requirements
### Maze Generation & Display
- FR1: The system shall generate random mazes using recursive backtracking or Prim’s algorithm.
- FR2: The maze shall be fully visible for a defined time (e.g., 5–10 seconds).
- FR3: After the reveal time, walls shall disappear partially, requiring the player to rely on memory.
- FR4: Maze complexity (size and branching factor) shall increase with levels.

### Player Controls
- FR5: The player shall move using keyboard arrow keys.
- FR6: The player shall be allowed to collect power-ups (e.g., reveal part of maze, slow down AI).
- FR7: The player shall be penalized for hitting dead ends (e.g., time penalty).

### AI Rival
- FR8: The AI rival shall use the A* Search Algorithm with Manhattan Distance heuristic to compute its shortest path.
- FR9: The AI shall update its path dynamically if obstacles appear or change.
- FR10: The AI’s speed shall increase with higher levels to maintain difficulty.

### Game Logic
- FR11: The game shall run both player and AI simultaneously, updating positions in real-time.
- FR12: The game shall declare a winner when either player or AI reaches the exit first.
- FR13: The game shall maintain a scoreboard (wins, losses, fastest completion times).
- FR14: The game shall support multiple difficulty levels (small, medium, large mazes).
- FR15: The system shall allow the player to restart, pause, and exit at any time.

### Tools
- `Python`
- `Pygame` Library (for maze graphics and controls)
- Pathfinding Algorithm: `A*` with `Manhattan Distance heuristic` (optimal for grid-based mazes)
- Random Library (for maze generation)
- Time Module (for visibility and penalties)

## Supervisor

|Field|Data|
|---|---|
|Name|Safid Ullah Shah
|Email ID|safid.ullah@vu.edu.pk|
|MS Teams ID|a015194@gmail.com|
