#importuando sqrt (raiz quadrada) da biblioteca math

from math import sqrt, floor, ceil

num = int(input('Digite um número inteiro: \n'))

raiz = sqrt(num)

print(f'A taiz de {num} é igual a {ceil(raiz)}') #ceil faz com que fique arendondado para cima

print(f'A taiz de {num} é igual a {floor(raiz)}') #floor faz com que fique arendondado para baixo

print(f'A taiz de {num} é igual a {raiz:.2f}') #formatação com dus casas decimais 