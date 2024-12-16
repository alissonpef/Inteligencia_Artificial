import random

# Gera um puzzle aleatório com números de 0 a 8, onde 0 é o espaço vazio
def gerar_puzzle_aleatorio():
    puzzle = list(range(9))
    random.shuffle(puzzle)  # Embaralha os números
    return [puzzle[:3], puzzle[3:6], puzzle[6:]]  # Forma uma matriz 3x3

# Encontra a posição correta de cada número no puzzle
def posicao_correta(numero):
    if numero == 0:
        return (2, 2)  # Posição do espaço vazio
    return (numero - 1) // 3, (numero - 1) % 3  # Calcula linha e coluna corretas

# Calcula a distância total de cada peça até seu lugar certo e a distância individual
def calcular_distancia_total(puzzle):
    distancias = {}  # Dicionário para armazenar a distância de cada peça
    soma_total = 0
    for i in range(3):
        for j in range(3):
            numero = puzzle[i][j]
            if numero != 0:  # Ignora o espaço vazio
                linha_final, coluna_final = posicao_correta(numero)
                distancia = abs(i - linha_final) + abs(j - coluna_final)  # Calcula a distância
                distancias[numero] = distancia  # Armazena a distância de cada peça
                soma_total += distancia  # Soma a distância total
    return distancias, soma_total

# Mostra o puzzle de forma legível, substituindo 0 por "_"
def print_puzzle(puzzle):
    for linha in puzzle:
        elementos = []
        for n in linha:
            if n != 0:
                elementos.append(str(n))  # Se o número não for 0, adicionar o número
            else:
                elementos.append('_')  # Se o número for 0, adicionar o underline
        print(' '.join(elementos))  # Junta e imprime os elementos da linha

# Gera o puzzle, calcula distâncias e exibe os resultados
puzzle = gerar_puzzle_aleatorio()
print("Puzzle:")
print_puzzle(puzzle)

# Calcula a distância de cada peça para a posição correta e a soma total
distancias, distancia_total = calcular_distancia_total(puzzle)

# Exibe a distância de cada peça
print("\nDistância de cada peça até a posição correta:")
for numero, distancia in distancias.items(): # Retorna pares de chave-valor
    print(f"Peça {numero}: {distancia} casas")

# Exibe a soma total das distâncias
print(f"\nSoma total das distâncias: {distancia_total} casas")
