casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do salário do comprador: '))
anosPagamento = int(input('Digite em quantos anos o pagamento será realizado: '))

valorMensal = (casa / anosPagamento)/12
trintaPorcento = salario * 0.3

print(f'O valor mensal da parcela será de: {valorMensal:.2f}')

if(valorMensal >= trintaPorcento):
    print('Empréstimo não aprovado!')
else:
    print('Empréstimo aprovado!')





