import heapq

class Node:
    def __init__(self, x, y, g, h):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.parent = None

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(mapa, start, goal):
    custo_lateral = 10
    custo_diagonal = 14


    open_set = []
    heapq.heappush(open_set, Node(start[0], start[1], 0, manhattan_distance(start[0], start[1], goal[0], goal[1])))

    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.x == goal[0] and current_node.y == goal[1]:
            return reconstruct_path(current_node)

        closed_set.add((current_node.x, current_node.y))

        for dx, dy, custo in [(0, 1, custo_lateral), (1, 0, custo_lateral), (0, -1, custo_lateral),
                              (-1, 0, custo_lateral),
                              (1, 1, custo_diagonal), (1, -1, custo_diagonal), (-1, 1, custo_diagonal),
                              (-1, -1, custo_diagonal)]:
            x = current_node.x + dx
            y = current_node.y + dy

            if 0 <= x < len(mapa) and 0 <= y < len(mapa[0]) and mapa[x][y] != 1:
                g = current_node.g + custo

                successor_node = Node(x, y, g, manhattan_distance(x, y, goal[0], goal[1]))

                if (x, y) not in closed_set or successor_node.g < open_set[0].g:
                    successor_node.parent = current_node

                    heapq.heappush(open_set, successor_node)

    return None


def reconstruct_path(node):

    path = []
    current_node = node

    while current_node:
        path.append((current_node.x, current_node.y))
        current_node = current_node.parent

    path.reverse()

    return path


mapa = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (5, 5)

caminho = a_star_search(mapa, start, goal)

print("Caminho encontrado:")
for x, y in caminho:
    print(f"({x}, {y})")