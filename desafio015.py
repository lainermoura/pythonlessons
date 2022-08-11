dias = int(input('Por quantos dias o carro foi alugado? '))
kmrodados = float(input('Quantos KM o carro rodou? '))
valorapagar = 60 * dias + 0.15 * kmrodados
print('O valor total a pagar é: {:.2f} reais.'.format(valorapagar))
