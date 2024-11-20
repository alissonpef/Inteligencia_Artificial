import os

# Função para desenhar o tabuleiro
def desenhar_tabuleiro(tabuleiro):
    os.system('cls')
    print("Jogo da Velha\n")
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("---+---+---")  
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---+---+---")  
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} \n")

# Verifica a vitória em cada uma das combinações possíveis
def verificar_vitoria(tabuleiro, jogador):
    combinacoes_vitoria = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
        [0, 4, 8], [2, 4, 6]              # Diagonais
    ]
    for combinacao in combinacoes_vitoria:
        if tabuleiro[combinacao[0]] == tabuleiro[combinacao[1]] == tabuleiro[combinacao[2]] == jogador:
            return True
    return False

# Função para verificar se houve empate
def verificar_empate(tabuleiro):
    return ' ' not in tabuleiro

# Função para a jogada do usuário
def jogada_usuario(tabuleiro):
    while True:
            posicao = int(input("Escolha uma posição de 1 a 9: ")) - 1
            if posicao < 0 or posicao > 8:
                print("Posição inválida! Deve ser entre 1 e 9.")
            elif tabuleiro[posicao] != ' ':
                print("Posição ocupada! Tente novamente.")
            else:
                return posicao

# Função para a jogada do computador usando Minimax
def jogada_computador(tabuleiro, jogador):
    melhor_valor = -float('inf')  # - infinito
    melhor_movimento = None
    for i in range(9):
        if tabuleiro[i] == ' ':
            tabuleiro[i] = jogador
            valor = minimax(tabuleiro, False, jogador)
            tabuleiro[i] = ' '
            if valor > melhor_valor:
                melhor_valor = valor
                melhor_movimento = i
    if melhor_movimento is not None:
        tabuleiro[melhor_movimento] = jogador  # Marca a posição com o jogador atual

# Função Minimax, avalia recursivamente todas as jogadas possíveis
def minimax(tabuleiro, is_maximizing, jogador):
    oponente = 'O' if jogador == 'X' else 'X' # Verifica o oponente
        # Verifica se o jogador atual venceu, perdeu ou empatou
    if verificar_vitoria(tabuleiro, jogador):
        return 1
    elif verificar_vitoria(tabuleiro, oponente):
        return -1
    elif verificar_empate(tabuleiro):
        return 0

    # Avalia o oponenente tentando minimizar o valor, true para maximizar e false para minimizar
    if is_maximizing:
        melhor_valor = -float('inf')
        for i in range(9):
            if tabuleiro[i] == ' ':
                tabuleiro[i] = jogador  # Faz uma jogada temporária
                valor = minimax(tabuleiro, False, jogador)  # Avalia essa jogada
                tabuleiro[i] = ' '  # Desfaz a jogada temporária
                melhor_valor = max(melhor_valor, valor)  # Escolhe o melhor valor
        return melhor_valor
    else:
        melhor_valor = float('inf')  
        for i in range(9):
            if tabuleiro[i] == ' ':
                tabuleiro[i] = oponente  # Faz uma jogada temporária do oponente
                valor = minimax(tabuleiro, True, jogador)  # Avalia essa jogada
                tabuleiro[i] = ' '  # Desfaz a jogada temporária
                melhor_valor = min(melhor_valor, valor)  # Escolhe o melhor valor
        return melhor_valor


tabuleiro = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
jogador_atual = 'X'  

# Função principal do jogo
while True:
    desenhar_tabuleiro(tabuleiro)
    
    if jogador_atual == 'X':
        print("Sua vez!")
        posicao = jogada_usuario(tabuleiro)
        tabuleiro[posicao] = jogador_atual
    else:
        print("Vez do computador!")
        jogada_computador(tabuleiro, jogador_atual)
    
    # Verifica vitória
    if verificar_vitoria(tabuleiro, jogador_atual):
        desenhar_tabuleiro(tabuleiro)
        vencedor = "Você" if jogador_atual == 'X' else "Computador"
        print(f"Parabéns, {vencedor} venceu!")
        break
    # Verifica empate
    elif verificar_empate(tabuleiro):
        desenhar_tabuleiro(tabuleiro)
        print("Empate!")
        break
    
    # Alterna jogador
    jogador_atual = 'O' if jogador_atual == 'X' else 'X'
