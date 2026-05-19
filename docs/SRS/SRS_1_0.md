# Table of Contents

- [Introduction](#introduction)
	- [Purpose](#purpose)
	- [Scope](#scope)
	- [Definitions, acronyms and abbreviations](#definitions-acronyms-and-abbreviations)
	- [References](#references)
	- [Overview](#overview)
- [Overall description](#overall-description)
	- [Product Perspective](#product-perspective)
	- [Product Functions](#product-functions)
	- [User Characteristics](#user-characteristics)
	- [Constraints](#constraints)
	- [Assumptions and Dependencies](#assumptions-and-dependencies)
- [Specific Requirements](#specific-requirements)
	- [Functional Requirements](#functional-requirements)
		- [Maze Generation and Display](#maze-generation-and-display)
		- [Player Controls](#player-controls)
		- [Ai Rival](#ai-rival)
		- [Game Logic](#game-logic)
	- [Non Functional Requirements](#non-functional-requirements)

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

- Product features
- Models
- User Characteristics
- Constraints
- Assumptions
- Functional requirements

# Overall Description

## Product Perspective

The _Memory Maze - Human vs AI Pathfinding Game_ is a standalone desktop application built using `Python` and the `PyGame` library. It integrates maze generation, AI pathfinding, and real-time gameplay in a single environment.

## Product Functions

- Generate and display random mazes.
- Run player and AI navigation concurrently.
- Handle player controls and power-ups.
- Track scores, levels, and performance metrics.
- Manage game states (pause, restart, exit).

## User Characteristics

- Player
	- <span id="UC_1">UC1</span>: Basic familiarity with keyboard controls and maze logic.
- Developer
	- <span id="UC_2">UC2</span>: Should understand `Python` and `PyGame` library.
- Supervisor
	- <span id="UC_3">UC3</span>: Evaluates performance and functionality.

## Constraints

- Developed using `Python` and `PyGame` only.
- Runs on desktop
	- `Windows`
- Algorithm(s) for maze generation
	- Recursive Backtracking
	- `Prim`'s Algorithm
- Algorithm(s) for path finding
	- `A*` with `Manhattan Distance heuristic`
- Maze difficulties
	- Small
	- Medium
	- Large

## Assumptions and Dependencies

- Adequate hardware resources for real-time graphics rendering.
	- Monitor
	- Graphics Card
- Operating system should be installed
	- `Windows`
- `Python 3.13.0+` and `PyGame` are installed.
- Single-player mode only (one human vs. one AI).

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

- <span id="NFA_1">NFA1</span>: The game shall support 30 frames per second.
- <span id="NFA_2">NFA2</span>: The game shall be designed primarily for Windows environments and is not required to support other operating systems.
- <span id="NFA_3">NFA3</span>: The game shall maintain stable gameplay without crashes during a continuous session of 30 minutes.
- <span id="NFA_4">NFA4</span>: The game interface shall provide clear visual feedback for player actions and game state changes.
- <span id="NFA_5">NFA5</span>: The system shall support single-player gameplay only, involving one human player competing against one AI agent.