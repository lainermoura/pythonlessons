from random import randint
from time import sleep

#Computador
numero = randint(1,5)
print('-=-' * 18)
print('Vou pensar em um número entre 0 a 5. Tente advinhar! ')

#Jogador
palpite = int(input('Em que número eu pensei? '))
print("PROCESSANDO...")
sleep(1)

if palpite == numero:
    print('Parabéns, vc conseguiu me vencer!')
else:
    print(f'Ganhei! Eu pensei no número {numero}!')
