salarioHora = float(input("Qual o valor da sua hora de trabalho? "))

totalHoraMes = float(input("Quantas hora você trabalha por mês? "))
ValorHorasTrabalhadas = (salarioHora * totalHoraMes)

impostoRenda = ValorHorasTrabalhadas * (11/100)
inss = ValorHorasTrabalhadas * (8/100)
sindicato = ValorHorasTrabalhadas * (5/100)

totalDesconto = (impostoRenda + inss + sindicato)
liquido = ValorHorasTrabalhadas - totalDesconto

print("Resultado holerite")
print("")

print(" -- Salario bruto: R$:", ValorHorasTrabalhadas)
print(" -- Valor pago ao INSS: R$:", inss)
print(" -- Valor pago ao sindicato: R$:", sindicato)
print(" -- Valor pago ao IR: R$:", impostoRenda)
print(" -- Total de descontos: R$:", totalDesconto)
print(" -- Salario líquido à receber: R$:", liquido)





