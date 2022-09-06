salario = float(input("Digite o valor do Solário: "))
if salario <= 1250:
    print(f'O valor do aumento foi de 15% e passou a receber {(salario * 15)/100 + salario:.2f} reais')
else:
    print(f'O valor de aumento foi de 10% e agora recebe {(salario * 10)/100 + salario:.2f} reais')
