#.if./.elif....../.else
#.se./.se .não.se./.se.não

entrada = input('Você qier "entrar" ou "sair"?\n')

if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'sair':
    print('Você saiu do sitema')
else:
    print('Você não digitou nem "entrar" e nem "sair".')

print('FORA DOS BLOCOS')