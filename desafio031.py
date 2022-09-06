distancia = float(input('Digite a distância da viagem (em Km): '))

if distancia <= 200:
    valor = distancia * 0.5
    print(f'A distância menor/igual a que 200Km. O valor é de {valor:.2f} reais.')
else:
    valor = distancia * 0.45
    print(f'A distância maior do que 200Km. O valor é de {valor:.2f} reais.')
