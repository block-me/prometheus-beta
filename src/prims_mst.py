import heapq
from typing import Dict, List, Tuple, Union

def prims_minimum_spanning_tree(graph: Dict[str, Dict[str, float]]) -> Union[List[Tuple[str, str, float]], None]:
    """
    Implement Prim's algorithm to find the minimum spanning tree of a graph.
    
    Args:
        graph (Dict[str, Dict[str, float]]): An adjacency list representation of the graph.
                                             Keys are nodes, values are dictionaries of neighboring nodes and edge weights.
    
    Returns:
        Union[List[Tuple[str, str, float]], None]: A list of edges in the minimum spanning tree, 
                                                   where each edge is (source, destination, weight).
                                                   Returns None if the graph is empty or disconnected.
    
    Raises:
        ValueError: If the input graph is not a valid adjacency list.
    """
    # Validate input
    if not graph:
        return None
    
    # Validate graph structure
    for node, neighbors in graph.items():
        if not isinstance(neighbors, dict):
            raise ValueError(f"Invalid graph structure for node {node}")
        for neighbor, weight in neighbors.items():
            if not isinstance(weight, (int, float)):
                raise ValueError(f"Invalid weight for edge {node} -> {neighbor}")
    
    # Check for nodes with no edges
    if all(len(neighbors) == 0 for neighbors in graph.values()):
        return []
    
    # Choose first node with connections as starting node
    start_node = next((node for node, neighbors in graph.items() if neighbors), None)
    
    if start_node is None:
        return None
    
    # Initialize data structures
    mst = []  # Minimum Spanning Tree edges
    visited = set([start_node])
    edges_heap = []
    
    # Add initial edges to the heap
    for neighbor, weight in graph[start_node].items():
        heapq.heappush(edges_heap, (weight, start_node, neighbor))
    
    # Run Prim's algorithm
    while edges_heap:
        weight, source, destination = heapq.heappop(edges_heap)
        
        # Skip if destination already visited
        if destination in visited:
            continue
        
        # Add edge to MST
        mst.append((source, destination, weight))
        visited.add(destination)
        
        # Add new edges from the newly visited node
        if destination in graph:
            for next_neighbor, next_weight in graph[destination].items():
                if next_neighbor not in visited:
                    heapq.heappush(edges_heap, (next_weight, destination, next_neighbor))
    
    # Check if all nodes are visited (graph is connected)
    if len(visited) != len(graph):
        return None
    
    return mst