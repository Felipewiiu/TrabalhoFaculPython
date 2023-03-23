numero = int(input('Digite o valor da tabuada: '))
print('')

if numero  >= 1 and numero <= 10:
    multiplicador = 0

    for tabuada in range(10):
        multiplicador += 1
        result = multiplicador * numero
        print(numero, 'x', multiplicador, "=", result)
else:
    print("Digite um número entre 1 e 10")