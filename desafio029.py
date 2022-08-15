from random import randint
from time import sleep

print('Seu carro passou no radar 🚗...')
sleep(2)

vel = randint(10, 180)
if vel > 80:
    print(f'Você estava a {vel} Km/h e foi multado, o valor da multa é R${(vel-80)*7}')
else:
    print(f'Sua velocidade é {vel}Km/h. Continue dirijindo com segurança!')
