nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))

media = (nota1+nota2)/2

if media < 5:
    print(f'Sua média foi {media} e você está reprovado.')
elif media >= 5 and media <= 6.9:
    print(f'Sua média foi {media} e você está de recuperação.')
else:
    print(f'Sua média foi {media} e você está aprovado! Parabéns!')
