def adicionarpilha(pilha, valor):
    pilha.append(valor)


def removerpilha(pilha, qtd):
    for i in range(qtd):
        pilha.pop()


NPR = []
try:
    while True:
        var = input()
        adicionarpilha(NPR, var)
        pos = len(NPR)-1
        if var == '+':
            var = float(NPR[pos-1]) + float(NPR[pos-2])
            removerpilha(NPR, 3)
            adicionarpilha(NPR, var)
        elif var == '*':
            var = float(NPR[pos-1]) * float(NPR[pos-2])
            removerpilha(NPR, 3)
            adicionarpilha(NPR, var)
        elif var == '/':
            try:
                var = float(NPR[pos-1]) / float(NPR[pos-2])
                removerpilha(NPR, 3)
                adicionarpilha(NPR, var)
            except ZeroDivisionError:
                print("Impossível dividir por 0.")
                removerpilha(NPR, 1)
        elif var == '-':
            var = float(NPR[pos-1]) - float(NPR[pos-2])
            removerpilha(NPR, 3)
            adicionarpilha(NPR, var)
        print(var)
except ValueError:
    print("Não foi possível realizar a operação.")
