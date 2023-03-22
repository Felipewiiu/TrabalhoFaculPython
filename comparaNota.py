primeiraNota = float(input("Digite a primeira nota: "))

segundaNota = float(input("Digite a segunda nota: "))

media = (primeiraNota + segundaNota) / 2

if media >= 7 and media < 10:
    print("Sua média é:", media, "Você está aprovado!")
elif media < 7:
    print("Sua média é:", media, "Você está reprovado!")
elif media == 10:
    print("Sua média é:", media, "Parabéns você foi Aprovado com Distinção!")