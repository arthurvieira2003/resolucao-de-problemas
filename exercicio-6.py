import heapq

class Graph:
    def __init__(self, graph, heuristics, costs):
        self.graph = graph
        self.heuristics = heuristics
        self.costs = costs

    def get_neighbors(self, node):
        return self.graph[node]

    def a_star_search(self, start, goal):
        priority_queue = []
        heapq.heappush(priority_queue, (self.heuristics[start], start, 0, []))

        min_costs = {start: 0}

        while priority_queue:
            _, current_node, current_cost, path = heapq.heappop(priority_queue)

            path = path + [current_node]

            if current_node == goal:
                print(f"Caminho: {' -> '.join(path)}")
                return path

            neighbors = self.get_neighbors(current_node)
            for neighbor in neighbors:
                g_cost = current_cost + self.costs[(current_node, neighbor)]
                f_cost = g_cost + self.heuristics[neighbor]

                if neighbor not in min_costs or g_cost < min_costs[neighbor]:
                    min_costs[neighbor] = g_cost
                    heapq.heappush(priority_queue, (f_cost, neighbor, g_cost, path))

        return None

graph = {
    'Arad': ['Zerind', 'Timisoara', 'Sibiu'],
    'Zerind': ['Oradea'],
    'Oradea': ['Sibiu'],
    'Timisoara': ['Lugoj'],
    'Lugoj': ['Mehadia'],
    'Mehadia': ['Drobeta'],
    'Drobeta': ['Craiova'],
    'Craiova': ['Rimnicu', 'Pitesti'],
    'Sibiu': ['Fagaras', 'Rimnicu'],
    'Fagaras': ['Bucharest'],
    'Rimnicu': ['Pitesti', 'Craiova'],
    'Pitesti': ['Bucharest'],
    'Bucharest': []
}

heuristics = {
    'Arad': 366,
    'Zerind': 374,
    'Oradea': 380,
    'Timisoara': 329,
    'Lugoj': 244,
    'Mehadia': 241,
    'Drobeta': 242,
    'Craiova': 160,
    'Sibiu': 253,
    'Fagaras': 176,
    'Rimnicu': 193,
    'Pitesti': 100,
    'Bucharest': 0
}

costs = {
    ('Arad', 'Zerind'): 75,
    ('Arad', 'Timisoara'): 118,
    ('Arad', 'Sibiu'): 140,
    ('Zerind', 'Oradea'): 71,
    ('Oradea', 'Sibiu'): 151,
    ('Timisoara', 'Lugoj'): 111,
    ('Lugoj', 'Mehadia'): 70,
    ('Mehadia', 'Drobeta'): 75,
    ('Drobeta', 'Craiova'): 120,
    ('Craiova', 'Rimnicu'): 146,
    ('Craiova', 'Pitesti'): 138,
    ('Sibiu', 'Fagaras'): 99,
    ('Sibiu', 'Rimnicu'): 80,
    ('Fagaras', 'Bucharest'): 211,
    ('Rimnicu', 'Pitesti'): 97,
    ('Rimnicu', 'Craiova'): 146,
    ('Pitesti', 'Bucharest'): 101
}

g = Graph(graph, heuristics, costs)

g.a_star_search('Arad', 'Bucharest')
