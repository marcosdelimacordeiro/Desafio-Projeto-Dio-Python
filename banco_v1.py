menu = """"
[1] - Sacar
[2] - Depositar
[3] - Extrato
[4] - Sair
"""
menu_bancario = 1
limite_saque = 3
saldo = 1000
extrato_deposito =[]
saque_realizado=0
extrato_saque = []
continuar = 1

while menu_bancario != 2:
    
    print(menu)
    opcao = int(input("Digite um opcao: "))
    
    if opcao == 1:
        while saque_realizado < limite_saque and continuar == 1:
            saque = int(input("Qual valor do saque: "))
            if saldo > 0 and  saldo >= saque:
                print(f"Saque no valor de R$ {saque:.2f} reais realizado com sucesso!")
                saldo -= saque
                saque_realizado += 1
                extrato_saque.append(f"\n Foi realizado saque no valor R$ {saque:.2f} reais")
                if saque_realizado < limite_saque:
                    continuar = int(input("""
                                        =====================================
                                        Deseja continuar: 
                                        Digite a opcao desejada
                                        [1] - (sim) para continuar ou 
                                        [2] - (nao) para Sair. 
                                        =====================================
                                        """).lower())
            else:
                print("Saldo insulfiente para saque!")
                break
        else:
            print("limite atingido! Você ja atingiu 3 saques diarios! ")
    elif opcao == 2:
        continuar_deposito = 1
        while continuar_deposito != 2:
            deposito = int(input("Qual valor deseja depositar: "))
            if deposito > 0 and continuar_deposito == 1:  
                saldo += deposito
                print(f"Deposito no valor de R$ {deposito:.2f} reais realizado com sucesso! seu saldo agora e de R$ {saldo:.2f} reais.")
                extrato_deposito.append(f" deposito realizando valor de R$ {deposito:.2f}")
            else:
                print("verificar deposito novamente aconteceu um erro!")

            continuar_deposito = int(input("""
                                        =====================================
                                        Deseja continuar: 
                                        Digite a opcao desejada
                                        [1] - (sim) para continuar ou 
                                        [2] - (nao) para Sair. 
                                        =====================================
                                        """).lower())
            
    elif opcao == 3:
        menu_extrato = """
    [1] - Extrato Saldo
    [2] - Extrato Saque
    [3] - Extrado Deposito
    [4] - Sair
    """
        print(menu_extrato)
        opcao_extrato = int(input("Qual opcao voce deseja: "))
        if opcao_extrato == 1:
            extrato1 = f'''
            ========Extrato Bancario Cliente========
            Conta : 001
            saldo Atual : R$ {saldo: .2f} reais
            ========================================
            '''
            print(extrato1)
        elif opcao_extrato == 2:
            for saque in extrato_saque:
                extrato2 = f'''
                ======Extrato Bancario Cliente - Saques=======
                Conta : 001
                Saque: {extrato_saque: .2f}
                ==============================================
                '''
                print(saque)
        elif opcao_extrato == 3:
            for deposito in extrato_deposito:
                print(deposito)
        else:
            print("saindo")
    else:
        menu_saida = '''
        ============================================
            Saindo! Obrigado por usar nosso Banco.!!
        ============================================

        '''
        print(menu_saida)
        break

    menu_bancario = int(input("""
                              =========================================================
                                     Deseja continuar e voltar menu inicial:
                                     Digite a opcao desejada:
                                     [1] - sim para continuar
                                     [2] - Não para sair
                              =========================================================
                               """).lower())


