n = input('Digite um numero de 0 a 9999: ')
s = '000' + n

print(f"""
Milhar: {s[-4]}
Centena: {s[-3]}
Dezena: {s[-2]}
Unidade: {s[-1]}
""")
