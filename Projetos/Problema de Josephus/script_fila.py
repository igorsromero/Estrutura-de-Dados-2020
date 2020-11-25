def remove(lista, posicao):
    lista.pop(posicao)


numeroSoldados = int(input('Digite o número de soldados: '))
vetor = [x+1 for x in range(numeroSoldados)]
aux = []

while len(vetor) > 1:
    if (len(vetor) % 2) == 0:
        for par in range(len(vetor)):
            if (par % 2) != 0:
                aux.append(par)
    else:
        remove(vetor, 0)
        for impar in range(len(vetor)):
            if (impar % 2) == 0:
                aux.append(impar)
    tamanho = len(aux)
    for i in range(tamanho):
        remove(vetor, aux[tamanho-1])
        tamanho -= 1
    aux = []
print('Você deve sentar no lugar {} para garantir sua sobrevivência.'.format(vetor[0]))
