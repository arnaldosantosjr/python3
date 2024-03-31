nome = input('Qual o seu nome?\n')
print(f'Prazer em conhecê-lo, {nome :=^20}! ')#Arnaldo será exibido em 20 caracteres, centralizado entre sinais de =;
n = int(input(f'{nome}, digite um valor. \n'))
n2 = int(input('Digite outro número.\n'))
div = n/ n2
dint = n//n2

print(f'{nome}, a divisão entre {n} e {n2} é {div}.')
print(f'{nome},e a divisão com um limite de casas decimais é entre {n} e {n2} é {div:.3f}. ', end='>>>') #:.3f limita a três casas decimais. E o end='' impede a quebra de linhas padrão do print
print(f'A divisão inteira é {dint}')
