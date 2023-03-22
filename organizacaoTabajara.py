salarioAtual = int(input("Digite o seu salário atual "))

aumento20 = 20/100
aumento15 = 15/100
aumento10 = 10/100
aumento5 = 5/100

if salarioAtual <= 280:
    reajuste20 = salarioAtual + (salarioAtual*aumento20)
    print('-- Salário antes do reajuste', salarioAtual)
    print('-- Percentual de reajuste: ', round((aumento20 * 100)),"%")
    print('-- Valor do aumento R$:', (salarioAtual * aumento20) )
    print('-- Salário após o reajuste R$:', reajuste20)

elif salarioAtual > 280 and salarioAtual < 700:
    reajuste15 = salarioAtual + (salarioAtual * aumento15)
    print('-- Salário antes do reajuste', salarioAtual)
    print('-- Percentual de reajuste: ', round((aumento15 * 100)), "%")
    print('-- Valor do aumento R$:', (salarioAtual * aumento15))
    print('-- Salário após o reajuste R$:', reajuste15)
elif salarioAtual >= 700 and salarioAtual < 1500:
    reajuste10 = salarioAtual + (salarioAtual * aumento10)
    print('-- Salário antes do reajuste', salarioAtual)
    print('-- Percentual de reajuste: ', round((aumento10 * 100)), "%")
    print('-- Valor do aumento R$:', (salarioAtual * aumento10))
    print('-- Salário após o reajuste R$:', reajuste10)
else:
    reajuste5 = salarioAtual + (salarioAtual * aumento5)
    print('-- Salário antes do reajuste', salarioAtual)
    print('-- Percentual de reajuste: ', round((aumento5 * 100)), "%")
    print('-- Valor do aumento R$:', (salarioAtual * aumento5))
    print('-- Salário após o reajuste R$:', reajuste5)



