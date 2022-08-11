nome = input('Qual é o seu nome completo? ')
maiusc = nome.upper()
minusc = nome.lower()
splitnome = nome.split()
joinnome = ''.join(splitnome)
primeironome = len(splitnome[0])
print(f"""
Seu nome é {nome}. 
Seu nome em letras maiúsculas: {maiusc},
Seu nome em letras maiúsculas: {maiusc},
seu tem {len(joinnome)} letras,
seu primeiro nome tem {primeironome} letras
""")

