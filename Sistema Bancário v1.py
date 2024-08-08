#Sistema Bancário v1
menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair


=> """


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor que irá depositar: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor_saque = float(input("Informe o valor que irá sacar (limite de até 500 reais): "))

        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Você não possui saldo suficiente.")
                      
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite disponível.")
        
        elif excedeu_saques:
            print("O limite de saques diários já foi atingido, por favor retorne amanhã.")

        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido")


    elif opcao == "e":
        print(" Extrato ".center(30, "-"))
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("".center(30 , "-"))

    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")

