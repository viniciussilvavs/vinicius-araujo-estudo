# Simulando um xaixa eletrônico

#O usuário tem um saldo inicial de 500 e pode sacar dinheiro 
#até zerar o saldo ou encerrar.

saldo = 500

while saldo > 0:
    saque = float(input("Informe o valor do saque (ou dogite 0 para sair): "))

    if saque == 0:
        break

    if saque > saldo:
        print("Saldo insulficiente! Saque não efetuado.")
    else:
        saldo -= saque
        print(f"Saque efetuado! Novo saldo disponível R$ {saldo:.2f}")

print("Operação finalizada!")