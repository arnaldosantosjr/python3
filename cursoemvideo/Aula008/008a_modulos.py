#importuando tudo da biblioteca math

import math

num = int(input('Digite um número inteiro: \n'))

raiz = math.sqrt(num)

print(f'A taiz de {num} é igual a {math.ceil(raiz)}') #math.ceil faz com que fique arendondado para cima

print(f'A taiz de {num} é igual a {math.floor(raiz)}') #math.floor faz com que fique arendondado para baixo

print(f'A taiz de {num} é igual a {raiz:.2f}') #formatação com dus casas decimais 