#O progrma irá ler um ângulo qualquer e mostrará na tela o valor do seno, coseno e tangente desse ângulo.

import math
ang= float(input('Digite o valor do ângulo.\n'))

ang_rad = math.radians(ang)

sen = math.sin(ang_rad)
cos = math.cos(ang_rad)
tg = math.tan(ang_rad)

print(f'O valor do seno de {ang} é {sen:.3f}')
print(f'O valor do coseno de {ang} é {cos:.3f}')
print(f'O valor da tangente de {ang} é {tg:.3f}')