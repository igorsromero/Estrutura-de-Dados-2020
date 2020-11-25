def adicionarpilha(pilha, valor):
    return pilha.append(valor)


def removerpilha(pilha, qtd):
    for i in range(qtd):
        pilha.pop()
    return True


NPR = []

print('Pressione ENTER após inserir um número ou a operação.')
try:
    while True:
        var = input()
        adicionarpilha(NPR, var)
        pos = len(NPR)-1
        if var == '+':
            var = float(NPR[pos-2]) + float(NPR[pos-1])
            removerpilha(NPR, 3)
            adicionarpilha(NPR, var)
        elif var == '*':
            var = float(NPR[pos-2]) * float(NPR[pos-1])
            removerpilha(NPR, 3)
            adicionarpilha(NPR, var)
        elif var == '/':
            try:
                var = float(NPR[pos-2]) / float(NPR[pos-1])
                removerpilha(NPR, 3)
                adicionarpilha(NPR, var)
            except ZeroDivisionError:
                print("Impossível dividir por 0.")
                removerpilha(NPR, 1)
        elif var == '-':
            var = float(NPR[pos-2]) - float(NPR[pos-1])
            removerpilha(NPR, 3)
            adicionarpilha(NPR, var)
        print(var)
except ValueError:
    print("Não foi possível realizar a operação.")
