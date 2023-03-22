media = float(0)

for x in range(4):
    notas = int(input("Digite suas notas do bimestre: "))
    media += notas
    print('Média parcial', media/4)
    print("")

print('Sua média final é: ', media / 4, 'Parabéns!')




