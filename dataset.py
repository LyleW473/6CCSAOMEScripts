import math

# Graph format:
# graph[u] = list of (v, weight) edges from u to v


# ------------------------------------------------------------
# 1. Non-negative graph
# Good for testing Dijkstra and Bellman-Ford
# ------------------------------------------------------------

graph_positive = {
    "s": [("a", 4), ("b", 1)],
    "a": [("c", 1)],
    "b": [("a", 2), ("c", 5)],
    "c": [("d", 3)],
    "d": []
}

expected_positive = {
    "s": 0,
    "a": 3,   # s -> b -> a = 1 + 2
    "b": 1,   # s -> b
    "c": 4,   # s -> b -> a -> c = 1 + 2 + 1
    "d": 7    # s -> b -> a -> c -> d = 1 + 2 + 1 + 3
}


# ------------------------------------------------------------
# 2. Negative edges but no negative cycle
# Good for Bellman-Ford, but NOT Dijkstra
# ------------------------------------------------------------

graph_negative_no_cycle = {
    "s": [("t", 6), ("y", 7)],
    "t": [("x", 5), ("y", 8), ("z", -4)],
    "y": [("x", -3), ("z", 9)],
    "x": [("t", -2)],
    "z": [("s", 2), ("x", 7)]
}

expected_negative_no_cycle = {
    "s": 0,
    "t": 2,    # s -> y -> x -> t = 7 + (-3) + (-2)
    "y": 7,    # s -> y
    "x": 4,    # s -> y -> x = 7 + (-3)
    "z": -2    # s -> y -> x -> t -> z = 7 + (-3) + (-2) + (-4)
}


# ------------------------------------------------------------
# 3. Reachable negative cycle
# Bellman-Ford should detect this
# ------------------------------------------------------------

graph_negative_cycle = {
    "s": [("a", 1)],
    "a": [("b", -1)],
    "b": [("c", -1)],
    "c": [("a", -1), ("d", 2)],
    "d": []
}

# Cycle:
# a -> b -> c -> a
# weight = -1 + -1 + -1 = -3
#
# This is reachable from s, so there is no finite shortest path
# to a, b, c, or d.


# ------------------------------------------------------------
# 4. Disconnected graph
# Some vertices are unreachable from s
# ------------------------------------------------------------

graph_disconnected = {
    "s": [("a", 2)],
    "a": [("b", 3)],
    "b": [],
    "x": [("y", 1)],
    "y": []
}

expected_disconnected = {
    "s": 0,
    "a": 2,
    "b": 5,
    "x": math.inf,
    "y": math.inf
}