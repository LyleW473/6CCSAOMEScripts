from dataset import (
    graph_positive, expected_positive, 
    graph_negative_no_cycle, expected_negative_no_cycle,
    graph_negative_cycle, expected_negative_cycle,
    graph_disconnected, expected_disconnected
)

def bellman_ford(graph):
    parent_dict = {}
    distances_dict = {"s": 0}
    for node in graph:
        if node != "s":
            distances_dict[node] = float("inf")
    queue = ["s"]

    update_count = {node: 0 for node in graph} # Keep track of how many times we have updated the distance to each node

    while queue:
        current_node = queue.pop(0)
        neighbour_nodes = graph[current_node]

        for neighbour_node, weight in neighbour_nodes:
            new_distance = distances_dict[current_node] + weight

            if new_distance < distances_dict[neighbour_node]: # If moving along this edge is smallest

                distances_dict[neighbour_node] = new_distance
                parent_dict[neighbour_node] = current_node
                update_count[neighbour_node] += 1

                if update_count[neighbour_node] >= len(graph): # If we have updated the distance to this node more times than there are nodes in the graph, we have a negative cycle
                    return_dict = {node: float("inf") for node in graph}
                    return_dict["s"] = 0
                    return return_dict
                
                if neighbour_node not in queue:
                    queue.append(neighbour_node)
    
    return distances_dict

def check_result(result, expected, name):
    for node in expected:
        if result[node] != expected[node]:
            print(f"Test failed for node {node}: expected {expected[node]}, got {result[node]} [{name}]")
            return
    print("Test passed!")

if __name__ == "__main__":

    for graph, expected, name in [
        (graph_positive, expected_positive, "positive"),
        (graph_negative_no_cycle, expected_negative_no_cycle, "negative_no_cycle"),
        (graph_negative_cycle, expected_negative_cycle, "negative_cycle"),
        (graph_disconnected, expected_disconnected, "disconnected")
    ]:
        result = bellman_ford(graph)
        check_result(result, expected, name)