import datetime

data = datetime.date.today()
anoAtual = int(data.strftime("%Y"))

anoNascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = anoAtual-anoNascimento

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 20:
    print('SENIOR')
else:
    print('MASTER')