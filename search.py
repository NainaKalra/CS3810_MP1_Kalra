"""
CS3810 Mini-Project 1 - Part 2: The Search Algorithms (100 points)
==================================================================

Implement dfs_search, astar_search, and idastar_search below. Do not change
the signatures or the return shapes: run_tests.py and the grading harness
unpack them exactly as documented.

You may NOT use a library implementation of DFS, A*, or IDA* (networkx,
simpleai, aima-python, ...). Using heapq, collections.deque, and the
provided PriorityQueue is expected and fine.

Metric definitions - use these, and say which you used in your report:

    nodes_expanded      A node is EXPANDED when it is removed from the
                        frontier and its successors are generated. Do not
                        count nodes that were merely generated.

    max_frontier_size   The largest number of live entries the frontier
                        ever held. For the PriorityQueue helper this is
                        len(queue), not len(queue.heap).

    iterations          (IDA* only) The number of depth-limited passes,
                        i.e. how many times the f-cost threshold was set.
                        A search that succeeds on the first threshold has
                        iterations == 1.

Suggested order of work: DFS first, then A*, then IDA*.
"""

import math

from priority_queue import PriorityQueue

# Sentinel used by the IDA* recursion to report success. Returning a plain
# number means "the smallest f-value I saw above the threshold".
FOUND = 'FOUND'


def dfs_search(problem):
    start = problem.initial_state()
    stack = [(start, [])] #(current state, path taken)
    explored = set() 
    nodes_expanded = 0 #for efficiency
    max_frontier_size = 1  #for memory
#dfs uses stack 
    while stack:
        max_frontier_size = max(max_frontier_size,len(stack))
        state, path = stack.pop()
        
        if problem.is_goal(state):
            return (path, nodes_expanded, max_frontier_size)
    
        if state not in explored: #to avoid infinite loops
            explored.add(state)
            nodes_expanded += 1
        
            actions_list = problem.get_actions(state)
        #reversed cz stack uses lifo 
            for act in reversed(actions_list):
                next_state = problem.result(state, act)
        
                if next_state not in explored:
                    new_path = path + [act]
            
                    stack.append((next_state, new_path))
            
    return (None, nodes_expanded, max_frontier_size)
    

def astar_search(problem, heuristic):
    start = problem.initial_state()
    frontier = PriorityQueue()
    g = {start: 0}  # Best cost so far
    came_from = {}
    frontier.push(start, heuristic(start, problem))
    nodes_expanded = 0
    max_frontier_size = 1

    while frontier:
        max_frontier_size = max(max_frontier_size, len(frontier))
        state = frontier.pop()
        
        # Goal checking 
        if problem.is_goal(state):
            path = _reconstruct(came_from, state)
            return (path, nodes_expanded, max_frontier_size)
        
        nodes_expanded += 1
        
        for action in problem.get_actions(state):
            successor = problem.result(state, action)
            new_cost = g[state] + problem.action_cost(state, action)
            
            #if it didnt see the state earlier or got a new way this time 
            if successor not in g or new_cost < g[successor]:
                g[successor] = new_cost
                came_from[successor] = (state, action)
                
                priority = new_cost + heuristic(successor, problem)
                frontier.push(successor, priority)
                
    return (None, nodes_expanded, max_frontier_size)

#helper _reconstruct - 
def _reconstruct(came_from, state):
    path = []
    while state in came_from:
        parent, action = came_from[state]
        path.append(action)
        state = parent
    path.reverse()
    return path



def idastar_search(problem, heuristic):
    """
    Perform Iterative Deepening A* Search.

    Args:
        problem: VacuumWorld instance
        heuristic: Function h(state, problem) -> estimated cost to goal

    Returns:
        Tuple (solution_path, nodes_expanded, iterations)
        iterations: Number of depth-limited iterations performed

    Requirements:
        * Iterative deepening on an f-cost THRESHOLD, not on depth. The
          next threshold is the smallest f-value that exceeded the current
          one.
        * Linear space: no explored set carried across iterations. You may
          track the states on the current path to avoid immediate cycles.
        * Returns an optimal solution.

    Structure that works (write DFS and A* first - this will make far more
    sense once you have both):

        threshold = h(start)
        loop:
            result = search(start, g=0, threshold)
            if result is FOUND:    return the path
            if result is infinite: return None (no solution)
            threshold = result

    where search(state, g, threshold) returns FOUND, or the smallest
    f-value it saw that exceeded the threshold, or math.inf.
    """
    raise NotImplementedError("Part 2c: implement idastar_search")


if __name__ == "__main__":
    # Quick manual check once you have implemented an algorithm:
    from test_grids import EXAMPLE, parse_grid
    from vacuum_world import VacuumWorld
    from heuristics import h2

    grid, start, dirty = parse_grid(EXAMPLE)
    problem = VacuumWorld(grid, start, dirty)

    path, expanded, frontier = astar_search(problem, h2)
    print("A* on the example grid (optimal cost is 14)")
    print("  cost     :", len(path) if path else None)
    print("  expanded :", expanded)
    print("  frontier :", frontier)
    print("  plan     :", path)
