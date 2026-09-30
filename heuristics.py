"""
CS3810 Mini-Project 1 - Part 3: Heuristics (25 points, +10 bonus)
=================================================================

Every heuristic takes (state, problem) and returns a NUMBER: an estimate of
the remaining cost to clean all remaining dirty cells. Keep the signature
even where you do not need `problem` - the search functions call them all
the same way.

Remember what the cost model is. Every move costs 1 AND every CLEAN costs 1,
so a state with k dirty cells remaining always costs at least k. A heuristic
that forgets the CLEAN actions is admissible but weak.

Writing the code is the small half of this part. The report must argue that
h1 and h2 are admissible: say exactly what lower bound each one computes and
why the true remaining cost can never be smaller than it.
"""


def manhattan(a, b):
    row1, col1 = a
    row2, col2 = b
    return abs(row1 - row2) + abs(col1 - col2)

def h0(state, problem):
    return 0

def h1(state, problem):
    pos, dirty_set = state
    return len(dirty_set)

def h2(state, problem):
    pos, dirty_set = state
    if not dirty_set:  
        return 0
    distances = []
    for d in dirty_set:
        dist = manhattan(pos, d)
        distances.append(dist)
    nearest_distance = min(distances)
    
    total_dirt_count = len(dirty_set)
    return nearest_distance + total_dirt_count

def h3(state, problem):
    """YOUR heuristic (optional, up to 10 bonus points).

    To earn the bonus it must be:
      1. Admissible - never overestimates the true remaining cost. You must
         argue this in the report. An inadmissible heuristic that finds
         short paths quickly is a different algorithm, not a better
         heuristic, and earns nothing.
      2. Dominant over h2 - h3(s) >= h2(s) for every state s.
      3. Supported by data - show the node counts next to h2's.

    If you are not attempting the bonus, leave this raising NotImplementedError
    and run_tests.py will skip it.

    A place to start thinking: h2 only ever looks at one dirty cell. After
    the robot reaches that cell it still has to get to all the others. What
    is a cheap-to-compute lower bound on THAT remaining travel?
    """
    raise NotImplementedError("Part 3 bonus: implement h3 (optional)")


# Used by experiments.py and run_tests.py. Do not rename.
HEURISTICS = {'h0': h0, 'h1': h1, 'h2': h2, 'h3': h3}
