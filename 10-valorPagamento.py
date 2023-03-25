prestacao = 1


def ValorPagamemto (atrasoDia, prestacao):
    if atrasoDia != 0:
        prestacao
    else:
         valor = (prestacao + (prestacao * 0.03) ) + (prestacao * 0.01) * atrasoDia
         print(f"Valor a ser pago: {valor}")

while prestacao != 0:
    if prestacao != 0:
        prestacao = int(input("Digite o número de prestação: "))
        atrasoDia = int(input("digie quantos dias em atraso: "))
        ValorPagamemto(prestacao, atrasoDia)



