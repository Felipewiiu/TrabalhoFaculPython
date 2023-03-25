salarios = []
salario = 0

while salario != -1:
    salario = float(input("Insira o salário do vendedor ou digite -1 para finalizar: "))
    if salario != -1:
        salarios.append(salario)


contadores = [0] * 9 + [0]

for salario in salarios:
    posicao = min(int((salario - 200) // 100), 8)
    contadores[posicao] += 1


for i in range(len(contadores)):
    if i < 8:
        print(f"${i*100+200}-${i*100+299}: {contadores[i]}")
    else:
        print(f"$1000 ou mais: {contadores[i]}")

