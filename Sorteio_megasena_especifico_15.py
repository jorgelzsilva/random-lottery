from random import randint
from babel.numbers import format_decimal
from datetime import datetime

# Programa que simula em quantos sorteios da mega sena uma sequência informada seria escolhida.

print('=' * 50)
print(f'{"QUANTO TEMPO LEVARIA PARA SER SORTEADO?":^50}')
print('-' * 50)

sequencia = []
cont = cont_4 = cont_5 = 0
primeira_quadra = 0
primeira_quina= 0
seq_quadra = []
seq_quina = []

while True:
    quantidade = int(input('Quantos números deseja escolher entre 6 e 15? '))
    if 6 <= quantidade <= 15:
        break
    else:
        print('\nA quantidade de números a serem escolhidos deve ser de 6 até 15')
print()
for c in range(1, quantidade + 1):
    while True:
        usuario = int(input(f'Escolha o {c}º número: '))
        if usuario in sequencia:
            print(f'\nO número {usuario} já foi informado, escolha outro\n')
        elif usuario < 1 or usuario > 60:
            print(f'\nO número {usuario} não pode ser escolhido, pois deve estar entre 1 e 60')
            print('Tente novamente.\n')
        else:
            sequencia.append(usuario)
            break
    sequencia.sort()

print('-' * 50) 

print(f'Você escolheu a sequência: ', end=' ')

for numero in sequencia:
    print(f'{numero}', end='  ')

print()
print('-' * 50) 

print(f'\nVerificando o número de sorteios até 6 de seus números serem sorteados')
print('\nIsso pode levar um tempo. Por favor aguarde.\n')

semanal = 2
ano = 52 * semanal

comeco = datetime.now()

while True:
    sorteio = [90, 90, 90, 90, 90, 90]
    cont_seq = 0
    for c in range(1,7):
        while True:
            escolha = randint(1,60)
            if escolha not in sorteio:
                break
        sorteio.append(escolha)
        sorteio.sort()
    for c in range(1,7):
        sorteio.pop()
    cont += 1
    for c in range(0, len(sorteio)):
        if sorteio[c] in sequencia:
            cont_seq += 1
    if cont_seq == 4:
        cont_4 += 1
        if cont_4 == 1:
            primeira_quadra = cont
            seq_quadra = sorteio
    elif cont_seq == 5:
        cont_5 += 1
        if cont_5 == 1:
            primeira_quina = cont
            seq_quina = sorteio
    if cont_seq == 6:
        break

media = cont / ano

print('-' * 50) 

print(f'Levaram {format_decimal(cont, locale="pt_BR")} sorteios até "{sorteio[0]} - {sorteio[1]} - {sorteio[2]} - {sorteio[3]} - {sorteio[4]} - {sorteio[5]}" ')

print(f'Isso equivale a aproximadamente {format_decimal(media, locale="pt_BR")} anos')

if cont_4 >= 1:
    print(f'\nNesse tempo quadras foram sorteadas {format_decimal(cont_4, locale="pt_BR")} vezes, acontecendo pela primeira vez no sorteio {format_decimal(primeira_quadra, locale="pt_br")}: {seq_quadra[0]} - {seq_quadra[1]} - {seq_quadra[2]} - {seq_quadra[3]} - {seq_quadra[4]} - {seq_quadra[5]}')
    
    print(f'Um sorteio de uma quadra ocorreu em média a cada {format_decimal((cont / cont_4), locale="pt_BR")} sorteios')

if cont_5 >= 1:
    print(f'\nNesse tempo quinas foram sorteadas {format_decimal(cont_5, locale="pt_BR")} vezes, acontecendo pela primeira vez no sorteio {format_decimal(primeira_quina, locale="pt_BR")}: : {seq_quina[0]} - {seq_quina[1]} - {seq_quina[2]} - {seq_quina[3]} - {seq_quina[4]} - {seq_quina[5]}')
    
    print(f'Um sorteio de uma quina ocorreu em média a cada {format_decimal((cont / cont_5), locale="pt_BR")} sorteios')

fim = datetime.now()

print(f'\nDuração: {fim - comeco}')

print('-' * 50) 