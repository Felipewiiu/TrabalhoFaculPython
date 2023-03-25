prestacao = 1
relatorio = []
atrasoDia = 0


def ValorPagamemto (atrasoDia, prestacao):
    if atrasoDia == 0:
         return prestacao
    else:
         return (prestacao + (prestacao * 0.03) ) + (prestacao * 0.01) * atrasoDia


while prestacao != 0:
        prestacao = float(input("Digite o valor da prestação: "))
        if prestacao == 0:
            print("\n====== Relatório do dia =====\n")
            quantidadePrestacao = len(relatorio)
            ValorTotalPrestacao= sum(relatorio)
            print(f"Quantidade de prestações pagas no dia: {quantidadePrestacao}")
            print(f"Valor total das prestações pagas no dia R$: {ValorTotalPrestacao} reais")
            print("\n==============================")
            exit()
        atrasoDia = int(input("digie quantos dias em atraso: "))
        relatorio.append(ValorPagamemto(atrasoDia, prestacao))
        print(f"Valor a ser pago é: {ValorPagamemto(atrasoDia, prestacao)} reais")





