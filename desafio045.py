import random
import emoji
print('VAMOS JOGAR JOKENPO')
print('Escolha uma opção:')
list = [1, 2, 3]
m = random.choice(list)
j = int(input(emoji.emojize('1 - :raised_fist:\n2 - :raised_hand:\n3 - :victory_hand:\n')))
if m == j:
    print('Empatamos vamos denovo?')
elif m == 1 and j == 2:
    print(emoji.emojize('Você ganhou! Parabéns! :raised_hand: vence :raised_fist: | Quer tentar a sorte novamente?'))
elif m == 1 and j == 3:
    print(emoji.emojize('Ganhei! :raise_fist: vence :victory_hand: | Deseja tentar novamente?'))
elif m == 2 and j == 3:
    print(emoji.emojize('Você ganhou! Parabéns! :victory_hand: vence :raised_hand:| Quer tentar a sorte novamente?'))
elif m == 2 and j == 1:
    print(emoji.emojize('Ganhei! :raised_hand: vence :victory_hand: | Deseja tentar novamente?'))
elif m == 3 and j == 1:
    print(emoji.emojize('Você ganhou! Parabéns! :raised_hand: vence :victory_hand: | Quer tentar a sorte novamente?'))
elif m == 3 and j == 2:
    print(emoji.emojize('Ganhei! :victory_hand: vence :raised_hand:| Deseja tentar novamente?'))

    CORRIGIR