from collections import deque

class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

    def __str__(self):
        return str(self.state)

def get_empty_tile_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_possible_actions(state):
    actions = []
    empty_row, empty_col = get_empty_tile_position(state)
    if empty_row > 0:
        actions.append("UP")
    if empty_row < 2:
        actions.append("DOWN")
    if empty_col > 0:
        actions.append("LEFT")
    if empty_col < 2:
        actions.append("RIGHT")
    return actions

def apply_action(state, action):
    empty_row, empty_col = get_empty_tile_position(state)
    new_state = [row[:] for row in state]
    if action == "UP":
        new_state[empty_row][empty_col] = new_state[empty_row - 1][empty_col]
        new_state[empty_row - 1][empty_col] = 0
    elif action == "DOWN":
        new_state[empty_row][empty_col] = new_state[empty_row + 1][empty_col]
        new_state[empty_row + 1][empty_col] = 0
    elif action == "LEFT":
        new_state[empty_row][empty_col] = new_state[empty_row][empty_col - 1]
        new_state[empty_row][empty_col - 1] = 0
    elif action == "RIGHT":
        new_state[empty_row][empty_col] = new_state[empty_row][empty_col + 1]
        new_state[empty_row][empty_col + 1] = 0
    return new_state

def bfs(initial_state, goal_state):
    queue = deque([Node(initial_state)])
    visited = set()

    while queue:
        current_node = queue.popleft()
        if current_node.state == goal_state:
            return reconstruct_path(current_node)

        visited.add(tuple(map(tuple, current_node.state)))
        for action in get_possible_actions(current_node.state):
            new_state = apply_action(current_node.state, action)
            if tuple(map(tuple, new_state)) not in visited:
                new_node = Node(new_state, current_node, action, current_node.cost + 1)
                queue.append(new_node)

    return None

def reconstruct_path(node):
    path = []
    while node:
        path.append((node.action, node.state))
        node = node.parent
    path.reverse()
    return path

# Example usage
initial_state = [[4, 2, 7], [0, 8, 6], [3, 5, 1]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

solution = bfs(initial_state, goal_state)
if solution:
    print("Solution found:")
    for action, state in solution:
        print(f"Action: {action}, State: {state}")
else:
    print("No solution found.")