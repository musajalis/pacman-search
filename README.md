# Pacman Search Project
UC Berkeley CS 188: Introduction to Artificial Intelligence, Spring 2020

## Overview
This is an implementation of various search algorithms for the Pacman Search project from UC Berkeley's CS 188: Introduction to Artificial Intelligence course. The project focuses on implementing graph search algorithms to help Pacman navigate mazes and find optimal paths to goals.

Project Description
In this project, Pacman must find paths through mazes to reach particular locations and collect food efficiently. The project implements general search algorithms including:

Depth-First Search (DFS)
Breadth-First Search (BFS)
Uniform Cost Search (UCS)
A Search*

These algorithms are tested on various maze configurations and search problems, demonstrating different pathfinding strategies and their efficiency trade-offs.
Files
Core Implementation Files

search.py - Contains implementations of search algorithms (DFS, BFS, UCS, A*)
searchAgents.py - Contains search-based agents and problem definitions

Supporting Files (Provided by UC Berkeley)

pacman.py - Main file that runs Pacman games
game.py - Logic for the Pacman world (agents, game states, directions)
util.py - Useful data structures (Stack, Queue, PriorityQueue)
graphicsDisplay.py - Graphics for Pacman
layout.py - Code for reading and storing maze layouts

Test and Utility Files

eightpuzzle.py - Eight-puzzle search problem for testing algorithms
searchTestClasses.py - Testing framework
commands.txt - Sample commands to run the project

Key Features
Search Algorithms Implemented

Depth-First Search (DFS)

Explores deepest nodes first
Uses a stack (LIFO) data structure
Not guaranteed to find optimal solution


Breadth-First Search (BFS)

Explores shallowest nodes first
Uses a queue (FIFO) data structure
Finds optimal solution for unweighted graphs


Uniform Cost Search (UCS)

Explores least-cost nodes first
Uses a priority queue ordered by path cost
Finds optimal solution for weighted graphs


A Search*

Uses both path cost and heuristic function
Priority queue ordered by f(n) = g(n) + h(n)
Optimal if heuristic is admissible and consistent



Search Problems

Position Search Problem - Find path to specific location
Corners Problem - Visit all four corners of maze
Food Search Problem - Collect all food dots efficiently

Usage
Running Basic Search Algorithms
bash# Run DFS on tiny maze
python pacman.py -l tinyMaze -p SearchAgent -a fn=depthFirstSearch

# Run BFS on medium maze
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs

# Run UCS on medium maze
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs

# Run A* with Manhattan heuristic
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
Testing Eight Puzzle
bashpython eightpuzzle.py
```

### Running with Different Layouts

Available layouts include:
- `tinyMaze` - Small test maze
- `mediumMaze` - Medium-sized maze
- `bigMaze` - Large maze
- `openMaze` - Open space
- `testMaze` - Custom test maze

## Implementation Highlights

### Graph Search
All algorithms implement graph search (not tree search) to avoid exploring the same state multiple times. This is achieved by maintaining a set of visited/explored states.

### Cost Functions
The project supports custom cost functions for different scenarios:
- **Uniform cost** - Each step costs 1
- **StayEast** - Penalizes positions on west side (cost = 0.5^x)
- **StayWest** - Penalizes positions on east side (cost = 2^x)

### Heuristics
Implemented heuristics for A* search:
- **Manhattan Distance** - |x₁ - x₂| + |y₁ - y₂|
- **Euclidean Distance** - √((x₁ - x₂)² + (y₁ - y₂)²)
- **Null Heuristic** - Always returns 0 (A* becomes UCS)

## Key Concepts

### Admissibility
A heuristic h(n) is admissible if it never overestimates the cost to reach the goal:
```
h(n) ≤ h*(n)  (where h* is the true cost)
```

### Consistency
A heuristic is consistent if:
```
h(n) ≤ cost(n, n') + h(n')  (for all successors n' of n)
Educational Value
This project teaches:

Implementation of classic search algorithms
Trade-offs between search strategies (completeness, optimality, time, space)
Importance of data structures in algorithm efficiency
Heuristic design and evaluation
Problem formulation for search

This implementation demonstrates fundamental search techniques that form the foundation for more advanced pathfinding algorithms used in AI, robotics, and navigation systems.
