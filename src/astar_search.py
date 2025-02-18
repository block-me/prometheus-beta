import heapq
from typing import List, Tuple, Callable, Any

def astar_search(
    start: Any, 
    is_goal: Callable[[Any], bool], 
    get_neighbors: Callable[[Any], List[Tuple[Any, float]]], 
    heuristic: Callable[[Any], float]
) -> List[Any]:
    """
    Implements the A* search algorithm.
    
    :param start: The starting node
    :param is_goal: A function that checks if a node is the goal
    :param get_neighbors: A function that returns neighboring nodes and their costs
    :param heuristic: A heuristic function that estimates the cost to the goal
    :return: A path from start to goal, or None if no path is found
    """
    # Priority queue to store nodes to explore
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    # Track the best path to each node
    came_from = {}
    
    # Cost to reach each node from the start
    g_score = {start: 0}
    
    # Estimated total cost through each node
    f_score = {start: heuristic(start)}
    
    while open_set:
        # Get the node with the lowest f_score
        current_f, current = heapq.heappop(open_set)
        
        # Check if we've reached the goal
        if is_goal(current):
            # Reconstruct the path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return list(reversed(path))
        
        # Explore neighbors
        for neighbor, cost in get_neighbors(current):
            # Calculate tentative g_score
            tentative_g_score = g_score[current] + cost
            
            # If this path to neighbor is better than any previous one
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                # Update tracking
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor)
                
                # Add to open set
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    # No path found
    return None