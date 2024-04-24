# and, or, not
print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)
print('=' *30)
saldo = 1000
saque = 200
limite = 100
conta_especial = True
saldo_suficiente = True


exp = saldo>= saque and saque <= limite or conta_especial and saldo >= saque

print(exp)

exp_2= (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

print(exp_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite

conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp3 =conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp3)