from dataset import (
    graph_positive, expected_positive, 
    graph_disconnected, expected_disconnected
)


def dijkstra(graph):
    """
    Dijkstra's algorithm for finding the shortest paths from a source node to all other nodes in a graph with non-negative edge weights.
    """
    distances_dict = {node: float("inf") for node in graph}
    distances_dict["s"] = 0

    visited = set()

    queue = [("s", 0)]

    while queue:
        
        queue = sorted(queue, key=lambda x: x[1]) # Sort the queue by distance (shortest distance first)
        current_node = queue.pop(0)

        current_node_name = current_node[0]
        if current_node_name in visited:
            continue

        for neighbour_node, edge_weight in graph[current_node_name]:

            if neighbour_node in visited:
                continue

            new_distance = distances_dict[current_node_name] + edge_weight
            if new_distance < distances_dict[neighbour_node]:
                distances_dict[neighbour_node] = new_distance
                queue.append((neighbour_node, new_distance))
        
    return distances_dict

def check_result(result, expected, name):
    """
    Check if the result from the algorithm matches the expected output.
    """
    for node in expected:
        if result[node] != expected[node]:
            print(f"Test failed for node {node}: expected {expected[node]}, got {result[node]} [{name}]")
            return
    print(f"Test passed for [{name}]")

if __name__ == "__main__":

    for graph, expected, name in [
        (graph_positive, expected_positive, "positive"),
        (graph_disconnected, expected_disconnected, "disconnected")
    ]:
        result = dijkstra(graph)
        check_result(result, expected, name + " (dijkstra)")