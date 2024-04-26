#Operadores lógicos
#and .(e).or.(ou).not(não)
#and.-.Todas.as.condições.precisam.ser
#verdadeira.
#Se.qualqur valor for considerado falso,
#a expressão inteira for considerada naquele valor
#São considerados falsy (que você já viu)
#0 0 0 '' False
#Também exite o tipo None que é
#usado para representar um não valor

'''entrada = input('[E]ntrar [S]air:\n')
senha_difgitada = input('Senha: ')


senha_permitida = '123'
#if True:
#    ...
if entrada == 'E' and senha_difgitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')'''

# avaliação de curto circuito
print(True and True and True and False and True)
print(True and True)
