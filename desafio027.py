nome = str(input('Digite seu nome completo: ')).strip().upper().split()

print(f"""
Muito prazer em te conhecer!
Seu primeiro nome é {nome[0]}.
Seu último nome é {nome[len(nome)-1]}.
""")
