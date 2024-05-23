#Estruturas de Repetição
#comando for
#É usado quando sabemos o número de vezes que aquilo irá se repetir

texto = input('Informe o texo: ')
VOGAL = 'AEIOU'

for letra in texto:
    #Assim contabiliza tanto maiúsculs quanto minúsculas
    if letra.upper() in VOGAL:
        print(letra, end="")
else:
    print() #adicionar uma quebra de linha
    print('Executa o final do laço')

