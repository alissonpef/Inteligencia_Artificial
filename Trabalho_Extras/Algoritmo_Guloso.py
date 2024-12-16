grafo = {
    'Araranguá-SC': {'Meleiro-SC': 30, 'Criciúma-SC': 60},
    'Meleiro-SC': {'Içara-SC': 50},
    'Criciúma-SC': {'Içara-SC': 20, 'Tubarão-SC': 45},
    'Içara-SC': {'Tubarão-SC': 30, 'Jaguaruna-SC': 25},
    'Tubarão-SC': {'Jaguaruna-SC': 35},
    'Jaguaruna-SC': {}  
}

def metodo_guloso(grafo, origem, destino):
    caminho = [origem]  # Lista para armazenar o caminho percorrido.
    atual = origem  # Cidade atual, começa na origem.
    distancia_total = 0  # Variável que acumula a distância total percorrida.
    distancias = []  # Lista para armazenar as distâncias entre cada par de cidades.

    # Loop que continua até chegar na cidade de destino.
    while atual != destino:
        if not grafo[atual]:  # Verifica se a cidade atual não tem vizinhos
            return None, None  # Se não houver caminho possível, retorna None
        
        # Escolhe o próximo nó (cidade) baseado na menor distância a partir da cidade atual.
        proximo = min(grafo[atual], key=grafo[atual].get) # Seleciona a cidade vizinha mais próxima com base na menor distância. 
        distancia = grafo[atual][proximo]  # Obtém a distância para a próxima cidade.
        distancias.append(distancia)  # Armazena a distância percorrida nesse passo.
        distancia_total += distancia  # Atualiza a distância total.
        caminho.append(proximo)  # Adiciona a próxima cidade ao caminho.
        atual = proximo  # A cidade atual se torna a próxima cidade.
    
    return caminho, distancias, distancia_total  # Retorna o caminho, as distâncias e a distância total.

origem = 'Araranguá-SC'  
destino = 'Içara-SC' 
caminho_guloso, distancias, distancia_total = metodo_guloso(grafo, origem, destino)

print("Caminho percorrido:")
# Exibe cada par de cidades e a distância entre elas
for i in range(len(caminho_guloso) - 1):  # ignora o ultimo elemento
    cidade_atual = caminho_guloso[i]
    proxima_cidade = caminho_guloso[i + 1]
    distancia = distancias[i]
    print(f'{cidade_atual} -> {proxima_cidade} : {distancia} km')

# Exibe a distância total percorrida
print(f'Distância total: {distancia_total} km')

