
def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print('valor sacado!')
        print('Retire o seu dinheiro!')
    print('Obrigado por ser nosso cliente!')

def depositar (valor):
    saldo = 500
    saldo += valor

sacar(100)