primeiro_valor = input('Digite um valor:\n')
segundo_valor = input('Digite outro valor:\n')

if primeiro_valor > segundo_valor:
    print(f'primeiorvalor = {primeiro_valor}\n'
    f'é maior que segundo_valor.')
elif segundo_valor > primeiro_valor:
    print(f'segundo valor = {segundo_valor} é maior que primeiro valor')
else:
    print(f'{primeiro_valor} = {segundo_valor}, os valores são iguais')