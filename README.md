# Romania Map Search using BFS

This repository contains a Python implementation of the Breadth-First Search (BFS) algorithm to solve the Romania map problem. The goal is to find a path from a starting city (Arad) to a destination (Bucharest).

## Implementation Details
- **Algorithm:** Breadth-First Search (BFS).
- **Data Structure:** A custom Tree class to maintain parent-child relationships for path reconstruction.
- **Iteration:** The search is implemented using a `while` loop and a FIFO queue to ensure memory stability and prevent recursion depth errors.

## Project Files
- `main.py`: The core script containing the graph data and the BFS function.
- `tree.py`: A helper class for node management and tree construction.

## Usage
1. Clone the repository.
2. Run the main execution script:
   ```bash
   python main.py