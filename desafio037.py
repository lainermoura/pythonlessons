number = int(input('Digite um número: '))
interaction = int(input("""Você deseja converter esse número para:
1) binário
2) octal
3) hexadecimal
"""))

if interaction == 1:
      print(bin(number))
elif interaction == 2:
      print(oct(number))
elif interaction == 3:
      print(hex(number))
else:
      print('Insira uma opção válida!')
