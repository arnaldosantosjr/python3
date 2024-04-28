maior_idade = 18

idade = int(input("Informe sua idade: "))

if idade >= 18:
    print(f'Sua idade é {idade}, você já pode tirar a CNH.')

elif idade >= 12 and idade < maior_idade:
    print('Você já pode assistir as aulas teóricas.\n'
        f'Ainda faltam {maior_idade - idade} anos para você começar as aulas práticas')   
else:
    print(f'Sua idade é {idade}, por tanto, você ainda não pode tiara a CNH.')
    print(f'Ainda faltam {maior_idade - idade} anos para você poder tirar a CNH.')