
def main(): # menu principal 
    return  """
        ==================================
        [1] - Cadastrar Usuario
        [2] - Cria Conta 
        [3] - Saque
        [4] - Deposito
        [5] - Extrato
        [6] - Sair
        ==================================
        """

def menu_extrato():
    return """
        ===============================
        [1] - Extrato Saldo
        [2] - Extrato Saque
        [3] - Extrado Deposito
        [4] - Sair
        ===============================
        """

#variaveis globais
saldo = 1000
numeros_saque = 0
contador = 0 
limite_saque = 500 
opcao = 0
lista_saque = [] 
lista_deposito = [] 
lista_usuarios = [] 
lista_contas_bancarias = []
numero_conta = 0

#===============================================
# funcao para cadastrar usuario
#===============================================
def cliente():
    cpf = ''.join(c for c in input("Digite seu CPF: ") if c.isdigit()) # iria verifica cada numero digitado , se estiver correto , faz uniao deles 
    for usuarios in lista_usuarios:
        if usuarios["cpf"] == cpf:
            print("ERRO! Usuario ja cadastrado")
            return
        
    clientes = {
        "nome": input("Digite seu Nome: "),
        "cpf": cpf,
        "endereco" : input("Digite seu endereço (Ex: Rua ABC,123 - Centro - Cidade/UF): "),
        "nascimento":input("Digite sua data de nascimento: ")
    }
    lista_usuarios.append(clientes)
    print("Usuario criado com sucesso!")
    return clientes

#===============================================
# funcao para cria conta bancaria
#===============================================
def criar_conta(cpf,usuarios,contas):
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)
    if not usuario:
        print("Usuário não encontrado. Cadastre-o primeiro.")
        return None

    # Gera número da conta automaticamente
    numero_conta = len(contas) + 1
    conta = {
        "cpf" : cpf,
        "Agencia" : "0001",
        "Conta" : numero_conta,
        "usuario" : usuario
    }
    contas.append(contas)
    print(f"Conta criada com sucesso! Agência: 0001 | Conta: {numero_conta}")
    return conta

#===============================================
# funcao para saque
#==============================================
def saque(*,saldo, numeros_saque, limite_saque, valor): 
    if valor <= saldo: #verifica que saldo e menor que saque
        if  valor <= limite_saque: # verifica que o valor e inferior a limite de saque definido
            print(f"Seu Saque no valor de R$ {valor: .2f} foi realizado com sucesso!")
            numeros_saque += 1
            saldo -= valor
            lista_saque.append(f"Saque {numeros_saque}: Realizado no valor de R$ {valor:.2f} ")
            return saldo, numeros_saque
        else:
            print("Valor de saque maior que limite permitido tente novamente")
    else:
        print("Não foi Possivel realizar o saque, seu Saldo é insuficiente!")
    return saldo, numeros_saque

#===============================================
#funcao para deposito
#===============================================
def deposito(depositar,saldo,contador,/):
    if depositar > 0:
        saldo += depositar
        contador += 1
        print(f"Novo valor de saldo R$ {saldo: .2f}")
        lista_deposito.append(f"Deposito {contador}: Foi Realizado um novo deposito no valor de R$ {depositar: .2f}")
    return depositar, saldo, contador

#===============================================
# funcao para extrato
#==============================================
def extrato(escolha, saldo,/,saque=lista_saque,deposito=lista_deposito):
    if escolha == 1:
        print( f"""
            =======================================
                Conta = 00000
                Saldo atual : {saldo: .2f}
            =======================================
            """
            ) 
    elif escolha == 2:
        if saque:
            for saque in lista_saque:
                print(f"\n {saque}")
        else:
            print("\nNenhum saque registrado.")
    elif escolha == 3:
        if deposito:
            for deposito in lista_deposito:
                print(f"\n {deposito}")
        else:
            print("\nNenhum deposito registrado.")
    else:
        return print("saindo ")

while opcao != 5:
    print(main())
    opcao = float(input(" qual opcao: "))
    if opcao == 1:
        cadastro = cliente()
        lista_de_cliente=input("Deseja verificar lista de cliente ")
        if lista_de_cliente == "sim":
            for clientes in lista_usuarios:
                print(clientes)
    elif opcao == 2:
        cpf = input("Digite o CPF do cliente: ")
        criar_conta(cpf, lista_usuarios, lista_contas_bancarias)
        if input("Deseja ver todas as contas? (sim/não): ").lower() == "sim":
            for conta in lista_contas_bancarias:
                print(conta)
    elif opcao == 3:
        while numeros_saque < 3:
            valor = float(input("Qual sera o valor de saque: "))
            saldo, numeros_saque= saque(saldo=saldo,numeros_saque=numeros_saque,limite_saque=limite_saque, valor=valor)
            escolha = input("""
                                        =====================================
                                        Deseja continuar: 
                                        Digite a opcao desejada
                                        [1] - Digite(sim) para continuar ou 
                                        [2] - Digite (nao) para Sair. 
                                        =====================================
                                        """).lower()
            if escolha != 'sim':
             break
        if numeros_saque >= 3: 
            print("Numero de saque diario atingido!")
    elif opcao == 4:
        continuar_deposito = "sim"
        while continuar_deposito != "nao":
            depositar = float(input("Qual valor deseja depositar: "))
            if depositar > 0 and continuar_deposito == "sim": 
                depositar, saldo,contador = deposito (depositar , saldo,contador)
            else:
                print("verificar deposito novamente aconteceu um erro!")
            continuar_deposito = str(input("""
                                        =====================================
                                        Deseja continuar: 
                                        Digite a opcao desejada
                                        [1] - (sim) para continuar ou 
                                        [2] - (nao) para Sair. 
                                        =====================================
                                        """).lower())
    elif opcao == 5:
        continuar_extrato = "sim"
        while continuar_extrato != "nao":
            print(menu_extrato())
            escolha = int(input("Digite numero da opcao desejada: "))
            extrato(escolha, saldo, saque= lista_saque, deposito=lista_deposito)
            continuar_extrato = str(input("""
                                        =====================================
                                        Deseja continuar: 
                                        Digite a opcao desejada
                                        [1] - (sim) para continuar ou 
                                        [2] - (nao) para Sair. 
                                        =====================================
                                        """).lower())
    else:
        print("""
                =======================================
                Obrigado por usar nosso banco!
                =======================================
              """)
        break