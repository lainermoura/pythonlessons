r1 = int(input('Primeira reta: '))
r2 = int(input('Segunda reta: '))
r3 = int(input('Terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível formar um triângulo!')
    if r1 == r2 == r3:
        print('O triângulo é equilátero.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O triângulo é isósceles.')
    else:
        print('O triângulo é escaleno.')
else:
    print('Não é possível formar um triângulo.')