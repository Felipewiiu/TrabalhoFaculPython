altura = float(input("Digite sua altura em metros: "))

sexo = str(input("Digite seu sexo, masculino ou feminino: "))

if sexo == "masculino":
    imc = round((72.7 * altura) - 58, 3)
    print("seu IMC é: ", imc)
elif sexo == "feminino":
    imc = round((62.1 * altura) - 44.7, 3)
    print("seu IMC é: ", imc)
else:
    print("sexo incorreto, por favor tente novamente")