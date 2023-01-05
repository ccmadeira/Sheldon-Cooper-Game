from random import randint
import emoji
from time import sleep

jogadas = (emoji.emojize('Pedra :punch:',language='alias'), emoji.emojize('Papel :hand:',language='alias'), emoji.emojize('Tesoura :v:',language='alias'), emoji.emojize('Lagarto :lizard:',language='alias'), emoji.emojize('Spock :vulcan_salute:',language='alias'))

computador = randint(0,4) 

print('''Suas opções:
[0]Pedra
[1]Papel
[2]Tesoura
[3]Lagarto
[4]Spock
''')

jogador = int(input('Qual a sua jogada?: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('LAGARTO')
sleep(1)
print('SPOCK')
sleep(1)

print('-='* 12)
print('O computador jogou {}'.format(jogadas[computador]))
print('Jogador jogou {}'.format(jogadas[jogador]))
print('-='* 12)

if computador == 0:
    if jogador == 0:
        print('Deu empate, jogue novamente')

    elif jogador == 1:
        print('Você VENCEU!')

    elif jogador == 2:
        print('Que pena, você PERDEU!')

    elif jogador == 3: 
        print('Que pena, você PERDEU!')

    elif jogador == 4:        
        print('Você VENCEU!')

    else:
        print('Jogada Inválida')    

elif computador == 1:
    if jogador == 0:
        print('Que pena, você PERDEU!')

    elif jogador == 1:
        print('Deu empate, jogue novamente')

    elif jogador == 2:
        print('Você VENCEU!')

    elif jogador == 3: 
        print('Você VENCEU!')

    elif jogador == 4:        
        print('Que pena, você PERDEU!')    

    else:
        print('Jogada Inválida') 

elif computador == 2:
    if jogador == 0:
        print('Você VENCEU!')

    elif jogador == 1:
        print('Que pena, você PERDEU')

    elif jogador == 2:
        print('Deu empate, jogue novamente')

    elif jogador == 3: 
        print('Que pena, você PERDEU!')

    elif jogador == 4:        
        print('Você VENCEU!')    

    else:
        print('Jogada Inválida') 

elif computador == 3:
    if jogador == 0:
        print('Você VENCEU!')

    elif jogador == 1:
        print('Que pena, você PERDEU!')

    elif jogador == 2:
        print('Você VENCEU!')

    elif jogador == 3: 
        print('Deu empate, jogue novamente')

    elif jogador == 4:        
        print('Que pena, você PERDEU!')

    else:
        print('Jogada Inválida')

elif computador == 4:
    if jogador == 0:
        print('Que pena, você PERDEU!')

    elif jogador == 1:
        print('Você VENCEU!')

    elif jogador == 2:
        print('Que pena, você PERDEU!')

    elif jogador == 3: 
        print('Você VENCEU!')

    elif jogador == 4:        
        print('Deu empate, jogue novamente')

    else:
        print('Jogada Inválida') 
        
print('\b')                       

