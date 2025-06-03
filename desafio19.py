n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

import random

lista = [n1,n2,n3,n4]
elemento_aleatorio = random.choice(lista)
print(f'O aluno escolhido foi {elemento_aleatorio}')