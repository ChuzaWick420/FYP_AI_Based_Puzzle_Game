# Memory Maze — Human vs AI Pathfinding Game

<div align="center">

![Python](https://img.shields.io/badge/Python-3.13%2B-blue?logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-2.x-green?logo=pygame)
![License](https://img.shields.io/badge/License-Academic-lightgrey)
![Status](https://img.shields.io/badge/Status-Prototype-orange)

*A competitive maze-solving game where human memory and strategy face off against AI algorithmic precision.*

</div>

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Screenshots](#screenshots)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Algorithms](#algorithms)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Game](#running-the-game)
- [Gameplay](#gameplay)
- [Difficulty Levels](#difficulty-levels)
- [Scoreboard](#scoreboard)
- [Running Tests](#running-tests)
- [Roadmap](#roadmap)
- [Documentation](#documentation)
- [Academic Information](#academic-information)

---

## Overview

**Memory Maze** is a Final Year Project (FYP) that pits a human player against an AI rival in a dynamically generated maze. At the start of each round the full maze is displayed for a brief window (5–10 seconds); the player must memorise the layout before portions of the walls disappear. The player then navigates using keyboard controls while the AI simultaneously solves the maze using the **A\* Search Algorithm** with a **Manhattan Distance heuristic**.

The project demonstrates core concepts in:

- Graph theory and data structures (adjacency-matrix representation)
- Minimum Spanning Tree generation via **Prim's Algorithm**
- AI pathfinding (**A\* with Manhattan Distance**)
- Real-time game-loop architecture with **Pygame**

---

## Features

### Implemented (Prototype)

| Feature | Description |
|---|---|
| Game Engine | Pygame-based main loop with event handling, rendering, and state management |
| Main Menu | Play and Quit buttons rendered via the `MainMenu` component |
| Graph Data Structure | Adjacency-matrix `Graph` class with `add_edge` and `add_vertex_data` helpers |
| Maze Population | Random weighted grid graph generation via `populate_graph` |
| Prim's Algorithm | MST-based maze generation ensuring every cell is reachable (no unsolvable mazes) |
| Level → Graph Mapping | `level_to_graph` converts a level number to a correctly sized `Graph` |
| Input Handling | `InputHandler` captures mouse clicks and window-close events as typed `SystemEvents` |
| Scoreboard Data | JSON scoreboard (`assets/scoreboard.json`) tracking wins, losses, and completion times |
| Difficulty Tiers | `MazeType` enum (SMALL / MEDIUM / LARGE) mapped to grid sizes 3×3, 9×9, 12×12 |

### Planned

- Full maze rendering on a Pygame canvas
- Timed maze reveal followed by partial wall disappearance
- Player movement via arrow keys
- AI rival using A\* with Manhattan Distance heuristic
- Power-ups (reveal area, slow AI, etc.)
- Dead-end time penalties
- Difficulty selection menu
- Pause and result screens
- Live scoreboard display

---

## Screenshots

> *Screenshots will be added as the visual game screens are implemented.*

---

## Architecture

```
main.py
  └── Engine (engine.py)
        ├── InputHandler  (prototype/presentation_layer/InputHandler.py)
        └── MainMenu      (prototype/menus/main_menu.py)
              ├── TextElement  (prototype/entities/TextElement.py)
              └── Button       (prototype/entities/Button.py)

Maze Generation Pipeline
  level_to_graph(level)          → Graph (sized by MazeType / Type_Size_Map)
  populate_graph(graph, size)    → fills adjacency matrix with random weights
  prims_algorithm(graph)         → reduces to a Minimum Spanning Tree (valid maze)
```

The engine runs a standard game loop:

1. **Process Events** — `InputHandler.processEvents()` maps raw Pygame events to `SystemEvents` constants.
2. **Update State** — button clicks and game-state transitions are handled.
3. **Render** — the active menu / game screen is drawn to the Pygame surface.
4. **Flip** — `pygame.display.flip()` presents the frame.

---

## Project Structure

```
FYP_AI_Based_Puzzle_Game/
├── main.py                          # Entry point
├── engine.py                        # Core game engine & main loop
│
├── prototype/
│   ├── algorithms/
│   │   └── prims_algo.py            # Prim's MST algorithm
│   ├── data/
│   │   ├── Global.py                # Global constants (e.g. WINDOW_RESOLUTION)
│   │   └── SystemEvents.py          # Typed system event codes
│   ├── entities/
│   │   ├── Graph.py                 # Adjacency-matrix graph data structure
│   │   ├── Button.py                # Clickable UI button component
│   │   ├── TextElement.py           # Pygame text rendering helper
│   │   ├── maze_type.py             # MazeType enum (SMALL / MEDIUM / LARGE)
│   │   └── type_to_size_map.py      # Maps MazeType name → grid node count
│   ├── menus/
│   │   ├── main_menu.py             # Main menu screen
│   │   ├── difficulty_menu.py       # Difficulty selection screen (planned)
│   │   ├── pause_menu.py            # Pause overlay (planned)
│   │   └── result_menu.py           # Round result screen (planned)
│   ├── presentation_layer/
│   │   └── InputHandler.py          # Pygame → SystemEvents translation layer
│   └── services/
│       ├── level_to_graph.py        # Level number → Graph factory
│       └── populate_graph.py        # Random weighted grid-graph population
│
├── tests/
│   ├── MST_generation.py            # Validates Prim's algorithm output
│   └── Level_dependency.py          # Validates level → graph size mapping
│
├── experiments/
│   └── main.py                      # Stand-alone prototype / sandbox
│
├── assets/
│   ├── scoreboard.json              # Persistent scoreboard data
│   ├── Adjacent_matrix.png          # Adjacency matrix diagram
│   ├── Proj_FYP_Graph_example.png   # Graph theory visual aid
│   └── Proj_FYP_Prim's_Algorithm.png # Prim's algorithm state diagram
│
└── docs/
    ├── SRS/                         # Software Requirements Specification
    ├── graph.md                     # Graph theory reference
    ├── Adjacent_Matrix.md           # Adjacency matrix reference
    ├── Prim's_algorithm.md          # Prim's algorithm reference
    └── project_info/                # Deliverables, milestones, todo lists
```

---

## Algorithms

### Prim's Algorithm — Maze Generation

Prim's algorithm is used to generate a **Minimum Spanning Tree (MST)** from a fully connected, randomly weighted grid graph. The MST becomes the maze layout, which guarantees:

- Every cell is reachable from every other cell (no isolated regions).
- There is exactly one path between any two cells (no loops), creating a classic maze.
- The start and exit are always connected.

**Steps:**

1. Create a grid graph where every adjacent pair of cells shares a randomly weighted edge.
2. Run Prim's algorithm to extract the MST, keeping only the minimum-weight edges.
3. The resulting adjacency matrix defines the navigable corridors of the maze.

Reference: [Wikipedia — Prim's Algorithm](https://en.wikipedia.org/wiki/Prim%27s_algorithm)

### A\* Search Algorithm — AI Pathfinding *(Planned)*

The AI rival will navigate the maze in real-time using the **A\* Search Algorithm** with a **Manhattan Distance heuristic**, which is optimal for grid-based pathfinding. The AI's speed scales with the selected difficulty level.

```
f(n) = g(n) + h(n)
  g(n) = cost from start to node n
  h(n) = Manhattan distance from n to the goal
```

---

## Getting Started

### Prerequisites

| Requirement | Version |
|---|---|
| Python | 3.13.0 or higher |
| Pygame | 2.x |

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/ChuzaWick420/FYP_AI_Based_Puzzle_Game.git
cd FYP_AI_Based_Puzzle_Game
```

**2. (Recommended) Create and activate a virtual environment**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install pygame
```

### Running the Game

```bash
python main.py
```

The game window (800 × 600) will open showing the main menu with **Play** and **Quit** buttons.

---

## Gameplay

| Step | Description |
|---|---|
| 1 | Launch the game and select a difficulty from the main menu |
| 2 | The generated maze is displayed in full for a few seconds — **memorise it!** |
| 3 | Walls begin to disappear; navigate to the exit using the **arrow keys** |
| 4 | The AI rival simultaneously solves the maze; reach the exit before it does |
| 5 | The result screen shows the winner, completion times, and an option to replay |

### Controls

| Key | Action |
|---|---|
| ↑ Arrow | Move Up |
| ↓ Arrow | Move Down |
| ← Arrow | Move Left |
| → Arrow | Move Right |
| `Esc` | Pause game |

---

## Difficulty Levels

| Level | Maze Type | Grid Size | Notes |
|---|---|---|---|
| 1, 4, 7, … | SMALL | 3 × 3 | Introductory |
| 2, 5, 8, … | MEDIUM | 9 × 9 | Moderate complexity |
| 3, 6, 9, … | LARGE | 12 × 12 | Challenging |

Difficulty cycles every three levels. AI speed and maze complexity increase as the level number rises.

---

## Scoreboard

Game results are persisted to `assets/scoreboard.json`:

```json
{
  "wins": 0,
  "loses": 0,
  "completion_times": [
    { "player": 0, "ai": 0 },
    ...
  ]
}
```

The scoreboard tracks the player's total wins and losses as well as per-round completion times for both the player and the AI.

---

## Running Tests

The `tests/` directory contains standalone verification scripts. Run them from the project root:

```bash
# Verify Prim's algorithm produces a valid MST
python tests/MST_generation.py

# Verify level-to-graph size mapping
python tests/Level_dependency.py
```

The `experiments/main.py` file is a self-contained sandbox used during early development and can be run independently:

```bash
python experiments/main.py
```

---

## Roadmap

- [x] Core game engine and Pygame loop
- [x] Main menu with Play / Quit buttons
- [x] Graph data structure (adjacency matrix)
- [x] Random weighted grid-graph population
- [x] Prim's algorithm for MST-based maze generation
- [x] Level → graph size mapping
- [x] Scoreboard data model
- [ ] Maze rendering on Pygame canvas
- [ ] Timed maze reveal + partial wall fade
- [ ] Player movement (arrow keys)
- [ ] AI rival (A\* with Manhattan Distance)
- [ ] Power-ups system
- [ ] Dead-end penalty system
- [ ] Difficulty selection menu
- [ ] Pause menu
- [ ] Result / scoreboard screen
- [ ] Persistent high-score display

---

## Documentation

| Document | Location |
|---|---|
| Software Requirements Specification (SRS) | [`docs/SRS/SRS Document.md`](docs/SRS/SRS%20Document.md) |
| Graph Theory Reference | [`docs/graph.md`](docs/graph.md) |
| Adjacency Matrix Reference | [`docs/Adjacent_Matrix.md`](docs/Adjacent_Matrix.md) |
| Prim's Algorithm Reference | [`docs/Prim's_algorithm.md`](docs/Prim's_algorithm.md) |
| Prototype Todo List | [`docs/project_info/prototype_todo.md`](docs/project_info/prototype_todo.md) |
| Final Deliverables | [`docs/project_info/Final_deliverables.md`](docs/project_info/Final_deliverables.md) |

---

## Academic Information

| Field | Details |
|---|---|
| Project Type | Final Year Project (FYP) |
| Institution | Virtual University of Pakistan |
| Supervisor | Safid Ullah Shah |
| Supervisor Email | safid.ullah@vu.edu.pk |
| Submission Deadline | 28 April 2026 |
