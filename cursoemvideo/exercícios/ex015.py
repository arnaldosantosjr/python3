dias = int(input('Por quantos dias o carro foi alugado?\n'))
km = float(input('Quantos km rodados?\n'))

total = (dias * 60) + (km * 0.15)

print(f'O total a pagar é de R$ {total:.2f}.')
