#Transformação

#é pssivel muar uma strig através dos métodos 

frase = 'O essencial é invisível aos olhos'

#O replace não trasforma diretamente na string, mas de uma forma secundária
print(frase.replace('essecial','importante'))

#para trasformar diretamente a strig fazemos assim:
frase = frase.replace('essecial','importante')
print(frase)

#mantem as maísculas e transforma as maiúsculs em minúsculas
print(frase.upper())

#fas o contrário do upper
print(frase.lower())
#faz com que tudo fique minúsculo e deixa a primeira letra em maíusculo
print(frase.capitalize())

#Faz com que a primeira letra de cada palavra fique em maúsculo e o resto em minúsculo
print(frase.title())

#remove todos os espaços inúteis
print(frase.strip())

#O r a frente é de 'right' e issi indica que removerá todos os espaços inútie à direita
print(frase.rstrip())

#O l a frente é de 'left' e isso indica que removerá todos os espaços iníteis à esquerda
print(frase.lstrip())

#Verificando se determiada palavra está em uma frase
print('Important' in frase)
