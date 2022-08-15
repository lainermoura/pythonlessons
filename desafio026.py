frase = str(input('Digite uma frase: ')).strip().upper()
print(f"""
A primeira letra A aparece {frase.count('A')} vezes na frase.
A letra A aparece pela primeira vez na {frase.find('A')+1}ª posição.
A letra A aparece pela última vez na {frase.rfind('A')+1}ª posição.

""")
