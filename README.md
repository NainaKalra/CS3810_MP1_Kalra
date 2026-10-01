# CS3810 Mini-Project 1: Search Algorithms for a Cleaning Robot

## Overview

This project implements and compares search algorithms for a cleaning robot operating in a grid environment.

The robot moves through the grid, avoids obstacles, and cleans all dirty cells. The project compares Depth-First Search (DFS), A*, and Iterative Deepening A* (IDA*) using different heuristics.

## Files

- `vacuum_world.py` - Defines the cleaning robot environment, states, actions, and action costs.
- `search.py` - Contains the DFS, A*, and IDA* search algorithms.
- `heuristics.py` - Contains the h0, h1, and h2 heuristics.
- `experiments.py` - Runs the experiments and generates the results.
- `results.csv` - Contains the experimental results.
- `figures/` - Contains the generated plots.
- `report.pdf` - Final project report.
- `AI_USE.md` - Describes how AI tools were used during the project.

## Requirements

Python 3 is required to run the project.

The project uses standard Python libraries.

## Running the Tests

Run:

```bash
python run_tests.py
```

The tests should complete without failures.

## Running the Experiments

Run:

```bash
python experiments.py
```

The results are saved to `results.csv` and the generated figures are saved in the `figures/` directory.

## Algorithms

### DFS

Depth-First Search uses a stack to explore the search space. An explored set is used to avoid cycles.

### A*

A* uses:

```text
f(n) = g(n) + h(n)
```

where `g(n)` is the cost from the start state and `h(n)` is the heuristic estimate of the remaining cost.

### IDA*

IDA* uses repeated depth-first searches with an increasing `f`-cost threshold.

## Heuristics

- `h0` - Returns 0 and provides no additional heuristic information.
- `h1` - Returns the number of dirty cells remaining.
- `h2` - Uses the Manhattan distance to the nearest dirty cell plus the number of dirty cells remaining.

The optional `h3` heuristic was not implemented.

## Experimental Results

The experiments record:

- Solution cost
- Nodes expanded
- Maximum frontier size
- IDA* iterations
- Runtime

Experiments were performed on six grid environments using the required timeout.

## Reproducing the Results

1. Make sure Python 3 is installed.
2. Run the tests:

```bash
python run_tests.py
```

3. Run the experiments:

```bash
python experiments.py
```

4. Check `results.csv` for the experimental results.
5. Check `figures/` for the generated plots.

## Project Structure

```text
CS3810_MP1/
├── vacuum_world.py
├── search.py
├── heuristics.py
├── experiments.py
├── results.csv
├── figures/
│   ├── heuristics.png
│   └── scaling.png
├── report.pdf
├── README.md
└── AI_USE.md
```
