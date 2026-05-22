# ABC define uma classe abstrata que obriga
# as subclasses a implementarem certos métodos.
from abc import ABC, abstractmethod
# Importa recursos de data e hora do módulo datetime
from datetime import datetime
import textwrap 

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    def realizar_transacao(self,conta, transacao):
        transacao.registrar(conta)
    def adicionar_conta(self,conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self,numero, cliente):
        self._saldo = 0 
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
        
    #mapeado nova conta, recebe cliente, numero e retorna um instancia de conta 
    @classmethod
    def nova_conta(cls,cliente, numero):
        return cls(numero, cliente)

    # Criando propriedades para acesso controlado aos atributos
    @property
    def saldo(self):
        return self._saldo
        
    @property
    def numero(self):
        return self._numero
        
    @property
    def agencia(self):
        return self._agencia
        
    @property
    def cliente(self):
        return self._cliente
        
    @property
    def historico(self):
        return self._historico
    # Operação para sacar
    def sacar(self, valor):
        # Puxa o valor do saldo
        saldo = self.saldo
        # Verifica se o valor do saque excede o saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n Operação falhou! Você não tem saldo suficiente. ")
            return False
        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            # para confimar que a operacao deu certo
            return True
        else:
            print("\n Operação falhou! O valor informado é inválido. ")
            return False
    #operacao para deposita
    def depositar(self,valor):
        if valor > 0:
            self._saldo += valor
            print(f"\n Deposito realizado com sucesso! ")
        else:
            print(f"\n Operacao falhou! Ovalor informado é invalido. ")
            return False
        return True
# contaCorrente mesmo atributos de conta, mas com 2 atributos a mais
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques =limite_saques
    #sobreescrita do metodo sacar, porque precisa validar senao execedeu limite do saldo, limite de  saque permitido
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == "Saque"]
        )
        excedeu_limite =valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print(f"\n Operação falhou! O valor do Saque execede o limite. ")
        elif excedeu_saques:
            print(f"\n Operação falhou! Número máximo de saques excedido. ")
        else:
            return super().sacar(valor)
        return False
    #metodo str para representa a classe conta corrente
    def __str__(self):
        return f"""\
            Agencia:\t{self.agencia}
            c/c:\t{self.numero}
            Titular:\t{self.cliente.nome}
        """
    
class Historico:
    def __init__(self):
        #lista de transacoes
        self._transacoes = []
    #propriedade para pegar as transacoes
    @property
    def transacoes(self):
        return self._transacoes
    # Método para adicionar transações ao histórico
    def adicionar_transacao(self, transacao):
        # Recebe uma transação e adiciona na lista do histórico
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
            }
        )
#interface de transacao que e uma classe abstrata
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

#mapeando o saque
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self,valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

def menu():
    menu = """
    ++++++++++++++++MENU++++++++++++++
        [d]\tDepositar
        [s]\tSacar
        [e]\tExtrato
        [nc]\tNova conta
        [lc]\tListar contas
        [nu]\tNovo usuários
        [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print(f"\n Cliente não possui conta! ")
        return
    #não permite cliente escolher conta
    return cliente.contas[0]

def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente =filtrar_cliente(cpf, clientes)
    if not cliente:
        print(f"\n Cliente não encontrado! ")
        return
    try:
        valor = float(input("Informe o valor do depósito: "))
    except ValueError:
        print("\n Valor inválido!")
        return
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)
    

def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print(f"\n Cliente não encontrado! ")
        return
    
    valor= float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print(f"\n Cliente não encontrado! ")
        return
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    print(f"\n ==========Extrato===========")
    transacoes= conta.historico.transacoes
    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações. "
    else:
        for transacao in transacoes:
            extrato += (
                f"\n{transacao['tipo']}: "
                f"\n\tR$ {transacao['valor']:.2f}"
            )
    
    print(extrato)
    print(f"\nSaldo: \n\tR$ {conta.saldo:.2f}")
    print('='*20)

def criar_conta(numero_conta, cliente, contas):
    cpf = input("Informe  o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, cliente)
    if not cliente:
        print(f"\n Cliente não encontrado, fluxo de criação de conta encerrado!")
        return
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.adicionar_conta(conta)
    print(f"\n === Conta criada com sucesso! ===")

def listar_contas(contas):
    for conta in contas:
        print("="*100)
        print(textwrap.dedent(str(conta)))

def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente numeros): ")
    cliente = filtrar_cliente(cpf, clientes)
    if cliente:
        print(f"\n Já existe cliente com esse CPF! ")
        return
    nome = input(f"Informe o nome comleto: ")
    data_nascimento = input("Informe a data de nascimento(dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)
    print("\n == Cliente criado com sucesso! ==")

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print(f"\n Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()