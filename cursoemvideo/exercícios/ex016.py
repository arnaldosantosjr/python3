#Este progrma vai ler um número ral qualquer pelo teclado e irá mostrar na tela a sua porção inteira.
import math
n = float(input('Digite um número real:\n'))

inteiro = math.floor (n)

print(f'A parte inteir a de {n} é {inteiro}') #forma 1
print(f'A parte inteir a de {n} é {math.floor(n)}') #Forma2
