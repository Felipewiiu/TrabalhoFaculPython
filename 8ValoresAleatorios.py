grupoNotas = []
nota = 0
tamanho = 0

while nota != -1:
    nota= float(input("Didite uma nota ou -1 para sair do programa: "))
    if nota != -1:
        grupoNotas.append(nota)
        tamanho += 1

tamanhoArray = len(grupoNotas)
somaArray = sum(grupoNotas)
arrayRevet = grupoNotas[::-1]
media = somaArray / tamanho

print("Quantidades de valores lidos: ", tamanhoArray)
print("Conjunto de valores: ", grupoNotas)
print("Conjunto de valores na ordem inversa: ", arrayRevet)
print("Soma dos valores: ", somaArray)
print("Média dos valores: ", media)


