#O programa irá ler o comprimento do cateto oposto e do cateto adjacente de um triângulo retânco e o calculo irá mostrar a hipotenusa.
import math
co= int(input('Digite o tamano do cateto oposto.\n'))
ca= int(input('Digite o tamonho do cateo adjacente.\n'))

hp = math.hypot(co, ca)

print(f'Se o cateto oposto mede {co} e o adjacente {ca}, a hipotenusa só pode ser {math.hypot(hp)}')