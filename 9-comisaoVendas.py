salarios = [470, 320, 600, 780, 900, 430, 550, 670, 1100, 870, 250, 790, 380]
contadores = [0] * 9 + [0]  # Inicializa a lista de contadores com 9 zeros e um último zero para os salários de $1000 em diante

for salario in salarios:
    posicao = min(int((salario - 200) // 100), 8)  # Fórmula para obter a posição na lista de contadores a partir do salário
    contadores[posicao] += 1  # Adiciona 1 à contagem correspondente à posição da lista

# Imprime os resultados
for i in range(len(contadores)):
    if i < 8:
        print(f"${i*100+200}-${i*100+299}: {contadores[i]}")
    else:
        print(f"$1000 ou mais: {contadores[i]}")