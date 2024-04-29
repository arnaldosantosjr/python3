#Análise

frase ='O essencial é invisível aos olhos'
#comprimento da frase
#01
#len(frase)

print(len(frase))

#conta quantas vezes um deteminao caractére 
#aparece na frase
#02
#frase.count('o')

print(frase.count('o'))

#Aqui o pragrma contará quantas vezes o caractere
#aparecerá em um determinado intervalo
#03
#frase.count('o',0, 13)

print(frase.count('o',0,13))

#Aqui ele dirá em que posição começará o ('el')
#04
#frase.find('el')

print(frase.find('el'))
#Colocando uma strig inseitente ele retorna o valor -1
print(frase.find('Android'))

#obs: É possivel fazer analise com um operador (o renorno será  True ou False)



