''' 1. Faça um programa que dado três números A, B e C os
apresente na ordem crescente.
Exemplo: Se os números forem A = 10, B = 4 e C = 8 a saída
do programa deve ser:
Ordem crescente => 4 – 8 – 10
Name: Gustavo. M. Khairalla
RM: 87101
'''

a = int(input('Primero valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
maior = menor = 0

if a == b or b == c or c == a:
    print('\033[31mTemos valores que são iguais!!\033[m')
    if a != b or b != c or c != a:
        print('\033[31mVocê colocou 2 valores IGUAIS e 1 DIRERENTE.\033[m')

if a > maior:
    maior = a
    if b > a and b > c:
        maior = b
    elif c > b and c > a:
        maior = c

if a > menor:
    menor = a
    if b < a and b < c:
        menor = b
    elif c < b and c < a:
        menor = c

if a != maior and a != menor:
    valor = a
elif b != maior and b != menor:
    valor = b
else:
    valor = c

print(f'\033[41mOrdem crescente! {menor}, {valor}, {maior}')
print(f'\033[41mOrdem decrecente! {maior}, {valor}, {menor}')
