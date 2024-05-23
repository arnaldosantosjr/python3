nome= str(input('Informe o seu nome completo:')).strip()#Strip() Serve para cortar as string para eliminar a contagem dos espaços

print('Analisando seu nome...')
print(f'Seu nome completo é:\n {nome}.')

#Nome com todas as letras maiúsculas
print(f'Seu nome em Músculo é: {nome.upper()}')

#Todas as letras minúsculas
print(f'Seu nome com todas as letras Minúsculas é: {nome.lower()}')

#quantidade de letras (não os caractéres)
print(f'O nimero de letras do seu nome é:{len(nome)-nome.count(' ')}')

#quantidade de letras no primeiro nome
'''print(f'Seu primeiro nome tem {nome.find(' ')} letras') #Essa é a primeira forma'''

#quantidade de letras no primeiro nome (Segunda forma)
separa = nome.split()#Faz a separação das palavras contidas na frase
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')