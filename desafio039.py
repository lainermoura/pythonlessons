import datetime

data = datetime.date.today()
anoAtual = int(data.strftime("%Y"))

anoNascimento = int(input('Digite o ano que você nasceu: '))
idade = anoAtual-anoNascimento

print(f'Você tem {idade} anos!')
if idade == 18:
    print('Seu momento de se alistar chegou!')
elif idade <= 17:
    print(f'Você ainda não tem idade para se alistar! Faltam {18-idade} anos. ')
else:
    print('Você já passou dos 18 anos e não pode se alistar.')
