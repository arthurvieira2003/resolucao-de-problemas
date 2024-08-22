from collections import deque


# Definição das ações possíveis
def aspirar(state):
    pos, y, z, w = state
    if pos == 'sala1' and y == 1:
        return ('sala1', 0, z, w)
    elif pos == 'sala2' and z == 1:
        return ('sala2', y, 0, w)
    elif pos == 'sala3' and w == 1:
        return ('sala3', y, z, 0)
    return state


def entrar_sala1(state):
    pos, y, z, w = state
    if pos != 'sala1':
        return ('sala1', y, z, w)
    return state


def entrar_sala2(state):
    pos, y, z, w = state
    if pos != 'sala2':
        return ('sala2', y, z, w)
    return state


def entrar_sala3(state):
    pos, y, z, w = state
    if pos != 'sala3':
        return ('sala3', y, z, w)
    return state


# Função para gerar todos os estados possíveis a partir do estado atual
def successors(state):
    return [
        aspirar(state),
        entrar_sala1(state),
        entrar_sala2(state),
        entrar_sala3(state),
    ]


# Verifica se o estado atual é o estado objetivo (todas as salas limpas)
def goal_test(state):
    return state[1] == 0 and state[2] == 0 and state[3] == 0


# Implementação do algoritmo de busca em largura (BFS)
def bfs(initial_state):
    frontier = deque([initial_state])
    explored = set()

    while frontier:
        state = frontier.popleft()

        if goal_test(state):
            return state

        explored.add(state)

        for next_state in successors(state):
            if next_state not in explored and next_state not in frontier:
                frontier.append(next_state)

    return None


# Estado inicial: aspirador na sala1, todas as salas sujas
initial_state = ('sala1', 1, 1, 1)

# Executando o algoritmo
final_state = bfs(initial_state)
print("Estado final:", final_state)