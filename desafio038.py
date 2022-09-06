n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

if n1 > n2:
    print(f'O primeiro valor é maior. | {n1} > {n2}')
elif n2 > n1:
    print(f'O segundo valor é maior. | {n2} > {n1}')
else:
    print('Os valores são iguais!')
