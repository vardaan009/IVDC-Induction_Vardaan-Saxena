import numpy as np
from collections import deque

grid = np.array([
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,1,1,1,0,0,0,0,0],
    [0,0,0,0,1,0,1,1,0,0],
    [0,1,1,0,0,0,0,1,0,0],
    [0,0,0,0,1,1,0,0,0,0],
    [0,0,1,0,0,0,0,1,0,0],
    [0,0,1,0,1,1,0,1,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,0,0,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0]
])

start = (0, 0)
goal = (9, 9)

# Define the four possible directions
directions = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1)    # Right
]

# Function to find valid neighboring cells
def get_neighbors(position):
    row, col = position
    neighbors = []

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        # Check if the cell is inside the grid
        if 0 <= new_row < 10 and 0 <= new_col < 10:

            # Check if the cell is free
            if grid[new_row][new_col] == 0:
                neighbors.append((new_row, new_col))

    return neighbors


def bfs(start, goal):

    queue = deque([start])

    visited = {start}

    parent = {start: None}

    explored = []

    while queue:

        current = queue.popleft()

        explored.append(current)

        if current == goal:
            break

        for neighbor in get_neighbors(current):

            if neighbor not in visited:

                visited.add(neighbor)

                parent[neighbor] = current

                queue.append(neighbor)

    return parent, explored


def reconstruct_path(parent, start, goal):

    # Check whether BFS reached the goal
    if goal not in parent:
        return []

    path = []
    current = goal

    # Follow parent cells backward
    while current is not None:
        path.append(current)
        current = parent[current]

    # Reverse the path to get start -> goal
    path.reverse()

    return path

parent, explored = bfs(start, goal)

path = reconstruct_path(parent, start, goal)

print("Cells explored:", len(explored))
print("Shortest path:", path)

if path:
    print("Path length:", len(path) - 1)
else:
    print("No path found!")
parent, explored = bfs(start, goal)

print("Number of explored cells:", len(explored))
print("Goal reached:", goal in parent)

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


# Create a copy of the grid for visualization
visual_grid = grid.copy()

# Mark explored cells with value 2
for row, col in explored:
    if (row, col) != start and (row, col) != goal:
        visual_grid[row, col] = 2

# Mark the final path with value 3
for row, col in path:
    if (row, col) != start and (row, col) != goal:
        visual_grid[row, col] = 3

# Define colours
# 0 = White (free)
# 1 = Black (obstacle)
# 2 = Light blue (explored)
# 3 = Yellow (final path)

cmap = ListedColormap([
    "white",
    "black",
    "lightblue",
    "yellow"
])

# Create the figure
plt.figure(figsize=(8, 8))

# Display the updated grid
plt.imshow(visual_grid, cmap=cmap, vmin=0, vmax=3)

# Mark start and goal
plt.scatter(start[1], start[0],
            color="green", s=200, label="Start")

plt.scatter(goal[1], goal[0],
            color="red", s=200, label="Goal")

# Add row and column numbers
plt.xticks(range(10))
plt.yticks(range(10))

# Draw grid lines at cell boundaries
plt.gca().set_xticks(np.arange(-0.5, 10, 1), minor=True)
plt.gca().set_yticks(np.arange(-0.5, 10, 1), minor=True)

plt.grid(which="minor", color="gray", linewidth=0.5)
plt.grid(which="major", visible=False)

# Add labels and title
plt.xlabel("Column")
plt.ylabel("Row")
plt.title("BFS Path Planning Visualization")

# Add legend
from matplotlib.patches import Patch

legend_elements = [
    Patch(facecolor="white", edgecolor="gray", label="Free"),
    Patch(facecolor="black", label="Obstacle"),
    Patch(facecolor="lightblue", label="Explored"),
    Patch(facecolor="yellow", label="Final Path")
]

plt.legend(handles=legend_elements, loc="upper left",
           bbox_to_anchor=(1.02, 1))

# Display the result
plt.show()