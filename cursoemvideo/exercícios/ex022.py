nome= input('Informe o seu nome completo:')

print(f'Seu nome completo é {nome}.')

#Nome com todas as letras maiúsculas
print(nome.upper())
#Todas as letras minúsculas
print(nome.lower())
#quantidade de letrsa (não os caractéres)
numero_letras = len([letra for letra in nome if letra.isalpha()])
print(numero_letras)

#quantidade de letras no primeiro nome
numero_letras = len([letra for letra in nome if letra.isalpha()])