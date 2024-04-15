import time

tempo = input('Digite o tempo em (segundos):\n')


if tempo.isdigit():
    tempo = int(tempo)
else:
    print('Entrada Inválida!')
    quit()

# uma outra opção para o whilepode ser:
# while tempo:
while tempo !=0:
    minutos, segundos = divmod(tempo, 60)
    timer = "{:02d}: {:02d}".format(minutos, segundos) # :02 iforma que vou considerar o zero a esquerda e mostre inteiro. Por isso é preciso usar o .format nolufar do f 
    print (timer, end = "\r")# o \r ao contrario do \n não salta uma linha, mas reescreve ela.
    time.sleep(1)
    tempo = tempo -1

print('Tempo esgotado.')
