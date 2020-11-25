numeroSoldados = int(input('Digite o número de soldados: '))

for potencia in range(numeroSoldados):
    if numeroSoldados == 1:
        numeroSoldados = 0
        break
    elif numeroSoldados < 2 ** (potencia+1):
        numeroSoldados -= (2 ** potencia)
        break

print('Você deve sentar no lugar {} para garantir sua sobrevivência.'.format(2*numeroSoldados+1))
