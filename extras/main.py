'''print('Quero meu primeiro emprego.')


nome = input('Digite su nome:\n')
idade = int(input ('Digite sua idade: \n'))
peso = float(input('Digite su peso.\n'))

print(nome)
print(idade)
print(peso)'''

'''soma = 1 + 1
multiplicacao = 1 * 1
divisao = 1 / 1
potencia = 1 ** 1
subtacao = 1 - 1

print(f'soma {soma}')
print(f'multiplicacao {multiplicacao}')
print(f'Divisão {divisao}')
print(f'potencia {potencia}')
print(f'subtracao {subtacao}')'''

'''idade = int(input('Infome sua idade:\n'))

if idade >= 18:
    print('Entrada permitida!')
else:
    print('Entrada não permitida!')'''

'''salario = float(input('Informe o salário:\n'))

if salario <= 3000:
    print('programador junior')
elif salario >3000 and salario <= 6000:
    print('Programdor pleno')
elif salario > 6000 and salario <= 15000:
    print('Programador senio')
else:
    print('Gegente de projetos')'''

#listas

#Repetições

notas = []
for x in range (5):
    cod_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [cod_aluno, nota]
    notas.append(resultado)
print('Quantidade de notas', len(notas))

for n in notas:
    cod_aluno = n[0]
    nota = n[1]
    print("O RM", cod_aluno, "tirou a nota:", nota)