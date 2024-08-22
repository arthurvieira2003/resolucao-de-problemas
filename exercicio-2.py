from collections import deque


# Definição das ações possíveis
def enche1(state):
    x, y = state
    if x < 3:
        return (3, y)
    return state


def enche2(state):
    x, y = state
    if y < 4:
        return (x, 4)
    return state


def esvazia1(state):
    x, y = state
    if x > 0:
        return (0, y)
    return state


def esvazia2(state):
    x, y = state
    if y > 0:
        return (x, 0)
    return state


def transfere1para2(state):
    x, y = state
    if x > 0:
        if x + y <= 4:
            return (0, x + y)
        elif y < 4 and x + y > 4:
            return (x + y - 4, 4)
    return state


def transfere2para1(state):
    x, y = state
    if y > 0:
        if x + y <= 3:
            return (x + y, 0)
        elif x < 3 and x + y > 3:
            return (3, x + y - 3)
    return state


# Função para gerar todos os estados possíveis a partir do estado atual
def successors(state):
    return [
        enche1(state),
        enche2(state),
        esvazia1(state),
        esvazia2(state),
        transfere1para2(state),
        transfere2para1(state),
    ]


# Verifica se o estado atual é o estado objetivo (jarro de 4 litros com exatamente 2 litros)
def goal_test(state):
    return state[1] == 2


# Implementação do algoritmo de busca em largura (BFS)
def bfs(initial_state):
    frontier = deque([initial_state])
    explored = set()
    path = {initial_state: None}

    while frontier:
        state = frontier.popleft()

        if goal_test(state):
            # Reconstruir o caminho da solução
            solution_path = []
            while state is not None:
                solution_path.append(state)
                state = path[state]
            return solution_path[::-1]

        explored.add(state)

        for next_state in successors(state):
            if next_state not in explored and next_state not in frontier:
                frontier.append(next_state)
                path[next_state] = state

    return None


# Estado inicial: ambos os jarros vazios [0, 0]
initial_state = (0, 0)

# Executando o algoritmo
solution = bfs(initial_state)

# Exibindo a solução encontrada
print("Solução encontrada:")
for step in solution:
    print(step)
