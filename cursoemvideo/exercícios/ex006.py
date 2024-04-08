n = int(input('digite um número inteiro.\n'))

dob = n * 2
tri = n * 3
raiz = n ** (1/2)

print(f'O dobro de {n} é {dob}, o triplo é {tri}, e a raíz quadrada é igual ou aproximadamente  {raiz:.2f}')

#Fazendo a raiz com a função pow(potência)
print(f'O dobro de {n} é {dob}, o triplo é {tri}, e a raíz quadrada é igual ou aproximadamente  {pow(n,(1/2))}')
