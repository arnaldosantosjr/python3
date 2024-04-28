import sys


saldo = 2000.0
opcao = int(input('Informe uma opção:\n [1]Sacar \n [2]Extrato \n'))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: R$ "))
    #...
elif opcao == 2:
    print("Exibindo o extrato ...")

else:
    sys.exit("Opção inválida")
    