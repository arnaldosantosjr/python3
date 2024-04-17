#O ususário irá inserir o nome de quatro alunos. O programa irá sortear um deles para apagar o quadro.

import random

a1 = input('Nome do primeiro aluno\n')
a2 = input('Nome do segundo aluno\n')
a3 = input('Nome do terceiro aluno\n')
a4 = input('Nome do quarto aluno\n')

nomes = (a1, a2, a3, a4)

sorteado = random.choice(nomes)
print(f'O nome sorteado é {sorteado}.')