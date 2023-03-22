numero = int(input('Digite o valor da tabuada: '))
multiplicador = 0

for tabuada in range(10):
    multiplicador+= 1
    result = multiplicador * numero
    print(numero, 'x', multiplicador, "=", result)