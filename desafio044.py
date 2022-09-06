productValue = float(input('Digite o preço do produto: '))
print('''Qual será a forma de pagamento?
1) Dinheiro ou cheque (10% de desconto)
2) À vista no cartão (5% de desconto)
3) Em até 2x no cartão(sem desconto)
4) 3x ou mais no cartão (20% de juros)''')

option1 = productValue * 0.9
option2 = productValue * 0.95
option3 = productValue
option4 = productValue * 1.2

optionChoosed = int(input('Escolha uma opcão: '))
if optionChoosed == 1:
    print(f'O produto custa {productValue:.2f}, com 10% de desconto o pagamento será de {option1:.2f}')
elif optionChoosed == 2:
    print(f'O produto custa {productValue:.2f}, com 5% de desconto o pagamento será de {option2:.2f}')
elif optionChoosed == 3:
    print(f'O produto custa {productValue:.2f}, e em até 2x no cartão não terá desconto.')
elif optionChoosed == 4:
    print(f'O produto custa {productValue:.2f}, em mais de 3x no cartão terá acrecimo de 20%, custará {option4:.2f}')
else:
    print('Você não escolheu uma opção válida!')
