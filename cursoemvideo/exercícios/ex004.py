''''
Este programa pedirá par o usuário digitar algo.
Depois ele irá exibir o tipo primitivo doque foi digitado
Por último ele exibirá todas as informações possíveis sobre o que foi digitado
'''
x = input('Digite algo: \n')
print('Qual a classe do valor?',type(x))
print('É numérico? ',x.isnumeric())
print('É alfanumérico? ',x.isalnum())
print('É Alfabético?',x.isalpha())
print('Tem caractére imprimível? ',x.isprintable())
print('Está em maiúsculo?',x.isupper())
print('Está em minúsculo?',x.islower())
print('Tem espaço? ',x.isspace())
print('Está capitalizado? ', x.istitle()) #Minúsculo e maiúsculo





