import random

n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')

lista = [n1, n2, n3, n4]
sorteado = random.sample(lista, 4)
index = 0

while index < len(sorteado):
    print(f'{index+1}- {sorteado[index]}')
    index += 1
