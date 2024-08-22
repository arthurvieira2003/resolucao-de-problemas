def fazendeiro(estado_atual, visitados):
    if estado_atual == ['d', 'd', 'd', 'd']:
        return []

    estado_tuple = tuple(estado_atual)
    if estado_tuple in visitados:
        return None
    visitados.add(estado_tuple)

    acoes = [
        ('vaiSozinho', [invert_lado(estado_atual[0]), estado_atual[1], estado_atual[2], estado_atual[3]]),
        ('levaRaposa', [invert_lado(estado_atual[0]), invert_lado(estado_atual[1]), estado_atual[2], estado_atual[3]]),
        ('levaGalinha', [invert_lado(estado_atual[0]), estado_atual[1], invert_lado(estado_atual[2]), estado_atual[3]]),
        ('levaMilho', [invert_lado(estado_atual[0]), estado_atual[1], estado_atual[2], invert_lado(estado_atual[3])]),
    ]

    for acao, estado_seguinte in acoes:

        if is_acao_valida(estado_seguinte):

            solucao = fazendeiro(estado_seguinte, visitados)

            if solucao is not None:
                return [acao] + solucao

    return None


def is_acao_valida(estado):
    if estado[0] != estado[1] and estado[1] == estado[2] and estado[0] != estado[2]:
        return False

    if estado[0] != estado[2] and estado[2] == estado[3] and estado[0] != estado[3]:
        return False

    return True


def invert_lado(lado):
    if lado == 'e':
        return 'd'
    elif lado == 'd':
        return 'e'
    else:
        raise ValueError(f'Lado inválido: {lado}')


estado_inicial = ['e', 'e', 'e', 'e']

visitados = set()
solucao = fazendeiro(estado_inicial, visitados)

if solucao is not None:
    print('Solução encontrada:')
    for acao in solucao:
        print(acao)
else:
    print('Não há solução.')