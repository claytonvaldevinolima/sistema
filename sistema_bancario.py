menu = '''

[d] Deposito
[s] Saque
[e] Extrato
[q] Sair

=> '''

# vou testar o github

saldo = 0
limite = 500
extrato  = " "
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Deposito "))
        
        if valor > 0:
            saldo += valor
            extrato += f"deposito: R$ {valor:.2f}\n"
            
        else:
            print("Repita a operação, valor informado invalido.")     
            
    elif opcao == "s":
        valor = float(input("Saque "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saque >= LIMITE_SAQUE
    
        if excedeu_saldo:
            print("operação falho! você não tem saldo suficiente. ")
        
        elif excedeu_limite:
            print("Operação falhou! o valor do saque excede o limite.")
    
        elif excedeu_saque:
            print("Operação falhou! numero maximo de saque excedo. ")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saque += 1
    
        else:
            print("operação falhou!")
        
    elif opcao == "e":
        print("\n===================Extrato==================")
        print("Sem movimentações." if not extrato else extrato )
        print(f"\nsaldo: R$ {saldo:.2f}")
        print("============================================")
        
        
    elif opcao == "q":
        break
        
    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")
    