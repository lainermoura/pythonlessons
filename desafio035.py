a = float(input('Insira a primeira medida: '))
b = float(input('Insira a segunda medida: '))
c = float(input('Insira a terceira medida: '))
lista = [a, b, c]
if a + b + c - max(lista) > max(lista):
    print(f'{a:.0f}, {b:.0f} e {c:.0f} PODEM formar um triângulo.')
else:
    print(f'{a:.0f}, {b:.0f} e {c:.0f} NÃO PODEM  formar um triângulo.')
