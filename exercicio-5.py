class Graph:
    def __init__(self, graph, heuristics):
        self.graph = graph
        self.heuristics = heuristics

    def get_neighbors(self, node):
        return self.graph[node]

    def greedy_best_first_search(self, start, goal):
        from heapq import heappush, heappop

        visited = []

        frontier = []
        heappush(frontier, (self.heuristics[start], start))

        while frontier:
            current_heuristic, current_node = heappop(frontier)

            visited.append(current_node)

            if current_node == goal:
                print(f"Caminho: {' -> '.join(visited)}")
                return visited

            neighbors = self.get_neighbors(current_node)
            for neighbor in neighbors:
                if neighbor not in visited:
                    heappush(frontier, (self.heuristics[neighbor], neighbor))

        print("Caminho não encontrado.")
        return None


graph = {
    'Arad': ['Zerind', 'Timisoara', 'Sibiu'],
    'Zerind': ['Oradea'],
    'Oradea': ['Sibiu'],
    'Timisoara': ['Rimnicu'],
    'Rimnicu': ['Sibiu'],
    'Sibiu': ['Fagaras'],
    'Fagaras': ['Bucharest'],
    'Bucharest': []
}

heuristics = {
    'Arad': 366,
    'Zerind': 374,
    'Oradea': 380,
    'Timisoara': 329,
    'Rimnicu': 193,
    'Sibiu': 253,
    'Fagaras': 176,
    'Bucharest': 0
}

g = Graph(graph, heuristics)

g.greedy_best_first_search('Arad', 'Bucharest')
