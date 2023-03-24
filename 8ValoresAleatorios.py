grupoNotas = []
nota = 0
tamanho = 0

while nota != -1:
    nota= int(input("Didite uma nota ou -1 para sair do programa: "))
    if nota != -1:
        grupoNotas.append(nota)
        tamanho += 1

tamanhoArray = len(grupoNotas)
somaArray = sum(grupoNotas)
arrayRevert = grupoNotas[::-1]
media = somaArray / tamanho
acimaMedia = sum(1 for nota in grupoNotas if nota > media)
abaixoDe7 = sum(1 for nota in grupoNotas if nota < 7)
print("Quantidades de valores lidos: ", tamanhoArray)


print("Conjunto de valores informados: ", end="")
for grupo in grupoNotas:
    print(grupo, end=" ")

print("\nConjunto de valores na ordem inversa: ")
for gruporv in arrayRevert:
    print(gruporv)

print("Soma dos valores: ", somaArray)
print("Média dos valores: ", media)
print(f"Valores a cima da média: {acimaMedia}")

print(f"Valores abaixo de 7: {abaixoDe7}")
print("\nFim do programa")




