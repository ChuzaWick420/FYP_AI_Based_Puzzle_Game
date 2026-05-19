# Memory Maze – Human Vs Ai Pathfinding Game Software Requirements Specification

## Version 1.1

![](./vu_logo.png){width=30%}

## Group Id: F25PROJECTB9784

## Supervisor Name: Safid Ullah Shah

# Table of Contents

- [Introduction](#introduction)
	- [Purpose](#purpose)
	- [Scope](#scope)
	- [Definitions, acronyms and abbreviations](#definitions-acronyms-and-abbreviations)
	- [References](#references)
	- [Overview](#overview)
- [Specific Requirements](#specific-requirements)
	- [Functional Requirements](#functional-requirements)
		- [Maze Generation and Display](#maze-generation-and-display)
		- [Player Controls](#player-controls)
		- [Ai Rival](#ai-rival)
		- [Game Logic](#game-logic)
	- [Non Functional Requirements](#non-functional-requirements)
- [Use case Diagram](#use-case-diagram)
- [Usage Scenarios](#usage-scenarios)
	- [Select Difficulty](#select-difficulty)
	- [Start Game](#start-game)
	- [Navigate Maze](#navigate-maze)
	- [Pause Game](#pause-game)
	- [Resume Game](#resume-game)
	- [Restart Game](restart-game)
	- [View Scores](#view-scores)
	- [Advance to Next Level](#advance-to-next-level)
	- [Quit](#quit)
	- [Exit](#exit)
- [Development Methodology](#development-methodology)
	- [Adopted Methodology](#adopted-methodology)
	- [Reasons for Chosen Methodology](#reasons-for-chosen-methodology)
- [Work Plan](#work-plan)

# Introduction

This document provides the foundation for the _Memory Maze - Human vs AI Pathfinding Game_ project.

## Purpose

This document specifies the requirements for the _Memory Maze - Human vs AI Pathfinding Game_, where a human player competes against an AI rival to solve dynamically generated mazes. It is intended for developers and supervisors involved in designing, implementing, and testing the system.

## Scope

_Memory Maze - Human vs AI Pathfinding Game_ aims to develop a competitive maze-solving game where a human player competes against an AI rival. At the beginning, the maze is displayed fully for a few seconds, after which parts of it disappear. The player must rely on memory and strategy to find the exit. Simultaneously, the AI rival uses the `A*` Search Algorithm (`Manhattan Distance heuristic`) to navigate the maze efficiently.

The game tests human cognitive skills against algorithmic precision, providing engaging experience and demonstrating pathfinding, algorithm design, and AI vs human performance comparison while keeping track of results. Additional complexity is introduced by multiple maze sizes, increasing difficulty levels, and power-ups, which can hinder or help in progress.

## Definitions, Acronyms and Abbreviations

- `UC`: User Characteristic (e.g. `UC1` means `user characteristic 1`)
- `FR`: Functional Requirement (e.g. `FR1` means `functional requirement 1`)
- `NFR`: Non Functional Requirement (e.g. `NFR1` means `non functional requirement 1`)
- `A*`: Path finding algorithm
- `Manhattan distance heuristic`: A calculation useful in grid based pathfinding algorithms
- `Python`: Programming language
- `PyGame`: A library which integrates with `Python`

## References

- IEEE, _IEEE Recommended Practice for Software Requirements Specifications_,  
IEEE Std 830-1993, IEEE Computer Society, 1993. Available: https://ieeexplore.ieee.org/

## Overview

This document describes the 

- Functional requirements
- Non Functional requirements
- Use Case Diagram
- Use Case Scenarios
- Development Methodology
- Work Plan

# Specific Requirements

## Functional Requirements

### Maze Generation and Display

- <span id="FR_1">FR1</span>: The system shall generate random mazes using `recursive backtracking` or `Prim`’s algorithm.
- <span id="FR_2">FR2</span>: The maze shall be fully visible for a defined time (e.g., 5–10 seconds).
- <span id="FR_3">FR3</span>: After the reveal time, walls shall disappear partially, requiring the player to rely on memory.
- <span id="FR_4">FR4</span>: Maze complexity (size and branching factor) shall increase with levels.

### Player Controls

- <span id="FR_5">FR5</span>: The player shall move using keyboard arrow keys.
- <span id="FR_6">FR6</span>: The player shall be allowed to collect power-ups (e.g., reveal part of maze, slow down AI).
- <span id="FR_7">FR7</span>: The player shall be penalized for hitting dead ends (e.g., time penalty).

### Ai Rival

- <span id="FR_8">FR8</span>: The AI rival shall use the `A*` Search Algorithm with `Manhattan Distance heuristic` to compute its shortest path.
- <span id="FR_9">FR9</span>: The AI shall update its path dynamically if obstacles appear or change.
- <span id="FR_10">FR10</span>: The AI’s speed shall increase with higher levels to maintain difficulty.

### Game Logic

- <span id="FR_11">FR11</span>: The game shall run both player and AI simultaneously, updating positions in real-time.
- <span id="FR_12">FR12</span>: The game shall declare a winner when either player or AI reaches the exit first.
- <span id="FR_13">FR13</span>: The game shall maintain a scoreboard (wins, losses, fastest completion times).
- <span id="FR_14">FR14</span>: The game shall support multiple difficulty levels (small, medium, large mazes).
- <span id="FR_15">FR15</span>: The system shall allow the player to restart, pause, and exit at any time.

## Non Functional Requirements

- <span id="NFA_1">NFA1</span>: The game shall support 60 frames per second.
- <span id="NFA_2">NFA2</span>: The game shall be designed primarily for Windows environments and is not required to support other operating systems.
- <span id="NFA_3">NFA3</span>: The game shall maintain stable gameplay without crashes during a continuous session of 30 minutes.
- <span id="NFA_4">NFA4</span>: The game interface shall provide clear visual feedback for player actions and game state changes.
- <span id="NFA_5">NFA5</span>: The system shall support single-player gameplay only, involving one human player competing against one AI agent.

# Use case Diagram

![](./use_case_diagram.png){width=70%}

# Usage Scenarios

## Select Difficulty

**Use Case Name:** Select Difficulty  
**Use Case ID:** UseCase1  
**Actor:** Player  
**Summary:** This use case describes the scenario in which player selects the game difficulty.  
**Pre-Condition:** Player must be on the main menu.  
**Post-Condition:** Player is back on the main menu.  
**Extend:** N/A  
**Uses:** N/A  
**Normal Course of Events:** Player will trigger the `Select Difficulty` button, then trigger one of the difficulty buttons (`easy`, `medium`, `hard`) and will be taken back to main menu.  
**Alternative Path:** N/A  
**Exception:** N/A

## Start Game

**Use Case Name:** Start Game  
**Use Case ID:** UseCase2  
**Actor:** Player  
**Summary:** This use case describes the scenario in which player starts playing the game.  
**Pre-Condition:** Player must be on main menu.  
**Post-Condition:** Player can see the maze on playing screen.  
**Extend:** N/A  
**Uses:** N/A  
**Normal Course of Events:** Player triggers the `Play` button.  
**Alternative Path:** Player can trigger `Select Difficulty` button to select difficulty, come back on the main menu and then trigger `Play` button.  
**Exception:** N/A

## Navigate Maze

**Use Case Name:** Navigate Maze  
**Use Case ID:** UseCase3  
**Actor:** Player  
**Summary:** This use case describes the scenario in which player uses arrow keys to navigate through the maze.  
**Pre-Condition:** Maze must be visible.  
**Post-Condition:** Player can move the avatar around.  
**Extend:** N/A  
**Uses:** N/A  
**Normal Course of Events:** Player uses arrow keys to control movements.  
**Alternative Path:** N/A  
**Exception:** N/A

## Pause Game

**Use Case Name:** Pause Game  
**Use Case ID:** UseCase4  
**Actor:** Player  
**Summary:** This use case describes the scenario in which player pauses the game.  
**Pre-Condition:** Maze must be visible.  
**Post-Condition:** Player is taken to pause menu.  
**Extend:** Navigate Maze  
**Uses:** N/A  
**Normal Course of Events:** Player presses the `Escape` key and is taken to the pause menu.  
**Alternative Path:** N/A  
**Exception:** N/A

## Resume Game

**Use Case Name:** Resume Game  
**Use Case ID:** UseCase5  
**Actor:** Player  
**Summary:** This use case describes the scenario in which player can resume the paused game.  
**Pre-Condition:** Player must be on pause menu.  
**Post-Condition:** Maze is visible again.  
**Extend:** Pause Game  
**Uses:** N/A  
**Normal Course of Events:** Player triggers the `Resume` button and is taken back into the playing state.  
**Alternative Path:** Player presses the `Escape` key and is taken back into the playing state.  
**Exception:** N/A

## Restart Game

**Use Case Name:** Restart Game  
**Use Case ID:** UseCase6  
**Actor:** Player  
**Summary:** This use case describes the scenario in which player resets the whole level.  
**Pre-Condition:** Player must be on pause menu.  
**Post-Condition:** Maze is visible again but level is reset.  
**Extend:** Pause Game  
**Uses:** N/A  
**Normal Course of Events:** Player triggers the `Restart` button. Level is reset and game is resumed.  
**Alternative Path:** N/A  
**Exception:** N/A

## View Scores

**Use Case Name:** View Scores  
**Use Case ID:** UseCase7  
**Actor:** Player  
**Summary:** This use case describes the scenario in which player can view their scores.  
**Pre-Condition:** Player must be on main menu or result menu.  
**Post-Condition:** Scoreboard is visible.  
**Extend:** N/A  
**Uses:** N/A  
**Normal Course of Events:** Player triggers the `Scoreboard` button on the result screen and is taken to the scoreboard menu.  
**Alternative Path:** Player triggers the `Scoreboard` button on the main menu and is taken to the scoreboard menu.  
**Exception:** N/A

## Advance to next Level

**Use Case Name:** Advance to Next Level  
**Use Case ID:** UseCase8  
**Actor:** Player  
**Summary:** This use case describes the scenario in which player advances the levels.  
**Pre-Condition:** Player must be on result menu.  
**Post-Condition:** Next level is visible.  
**Extend:** N/A  
**Uses:** N/A  
**Normal Course of Events:** On the result menu, player triggers the `Next Level` button and is taken to the next level.  
**Alternative Path:** N/A  
**Exception:** N/A

## Quit

**Use Case Name:** Quit  
**Use Case ID:** UseCase9  
**Actor:** Player  
**Summary:** This use case describes the scenario in which player is taken to the main menu.  
**Pre-Condition:** Player must be on any of the menus.  
**Post-Condition:** Main menu is visible.  
**Extend:** Pause, View Scores  
**Uses:** N/A  
**Normal Course of Events:** From any menu, player triggers the `Quit` button and is taken to the main menu.  
**Alternative Path:** N/A  
**Exception:** N/A

## Exit

**Use Case Name:** Exit  
**Use Case ID:** UseCase10  
**Actor:** Player  
**Summary:** This use case describes the scenario in which player terminates the game.  
**Pre-Condition:** Player must be on the main menu.  
**Post-Condition:** Game terminates.  
**Extend:** N/A  
**Uses:** N/A  
**Normal Course of Events:** Player triggers the `Exit` button and game is terminated.  
**Alternative Path:** N/A  
**Exception:** N/A

# Development Methodology

Software development process often refers to the high-level process that governs the development of a software system from its beginning to its end of life – known as a methodology, model or framework.

Various methodologies have been devised, including waterfall, spiral, agile, rapid prototyping, incremental and synchronize and stabilize.

## Adopted Methodology

The `iterative methodology` was chosen for the `Memory Maze - Human vs AI Pathfinding Game`.

The basic idea behind this method is to develop a system through repeated cycles (iterative) and in smaller portions at a time (incremental), allowing software developers to take advantage of what was learned during development of earlier parts or versions of the system. Learning comes from both the development and use of the system, where possible key steps in the process start with a simple implementation of a subset of the software requirements and iteratively enhance the evolving versions until the full system is implemented

## Reasons for Chosen Methodology

- Features can be developed independently and integrated gradually.
- The approach allows continuous testing and debugging.
- It provides flexibility for improving gameplay experience.
- It allows developer to get familiar with the tools.

# Work Plan

![](./chart.png)