import heapq
import math
class Node:
    def __init__(self, position, parent=None):
        self.position = tuple(position)
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

    def __repr__(self):
        return f"{self.position} - g: {self.g}, h: {self.h}, f: {self.f}"

    def __hash__(self):
        return hash(self.position)

def astar(start, end, grid):
    # Create the open and closed sets
    open_set = []
    closed_set = set()

    # Add the start node
    heapq.heappush(open_set, start)

    # Loop until the open set is empty
    while open_set:
        # Get the node with the lowest f score
        current_node = heapq.heappop(open_set)

        # If we found the goal, return the path
        if current_node == end:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = current_node.parent
            return path[::-1]

        # Add the current node to the closed set
        closed_set.add(current_node)

        # Get the neighbors of the current node
        neighbors = current_node.get_neighbors(grid)

        for neighbor in neighbors:
            # If the neighbor is in the closed set, skip it
            if neighbor in closed_set:
                continue

            # Calculate the tentative g score
            tentative_g_score = current_node.g + current_node.get_distance(neighbor)

            # If the neighbor is not in the open set, add it
            if neighbor not in open_set:
                heapq.heappush(open_set, neighbor)
            # If the tentative g score is greater than the neighbor's g score, skip it
            elif tentative_g_score >= neighbor.g:
                continue

            # Update the neighbor's g, h, and f scores
            neighbor.parent = current_node
            neighbor.g = tentative_g_score
            neighbor.h = neighbor.get_distance(end)
            neighbor.f = neighbor.g + neighbor.h

    # If we get here, there is no path
    return None