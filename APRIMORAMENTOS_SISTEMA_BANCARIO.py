#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Cliente:
    def __init__(self, nome, cpf, idade, data_nascimento, logradouro, bairro, cidade, estado):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.data_nascimento = data_nascimento
        self.logradouro = logradouro
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado

class Conta:
    numero_conta = 1
    agencia = "0001"

    def __init__(self, cliente):
        self.numero = Conta.numero_conta
        self.agencia = Conta.agencia
        self.cliente = cliente
        self.saldo = 0
        self.extrato = []
        self.saques_realizados = 0

        Conta.numero_conta += 1

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            return True
        else:
            return False

    def sacar(self, valor, limite=500, limite_saques=3):
        if self.saques_realizados < limite_saques and 0 < valor <= limite and self.saldo >= valor:
            self.saldo -= valor
            self.extrato.append(f"Saque: -R$ {valor:.2f}")
            self.saques_realizados += 1
            return True
        else:
            return False

    def consultar_saldo(self):
        return self.saldo

    def consultar_extrato(self):
        if self.extrato:
            return "\n".join(self.extrato)
        else:
            return "Não foram realizadas movimentações"

def cadastrar_cliente():
    nome = input("Nome: ")
    cpf = input("CPF: ")
    idade = int(input("Idade: "))
    data_nascimento = input("Data de Nascimento: ")
    logradouro = input("Logradouro: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado (Sigla): ")

    cliente = Cliente(nome, cpf, idade, data_nascimento, logradouro, bairro, cidade, estado)
    return cliente

def cadastrar_conta(cliente):
    conta = Conta(cliente)
    return conta

def consultar_usuarios(clientes):
    for cliente in clientes:
        print("Nome:", cliente.nome)
        print("CPF:", cliente.cpf)
        print("Idade:", cliente.idade)
        print("Data de Nascimento:", cliente.data_nascimento)
        print("Logradouro:", cliente.logradouro)
        print("Bairro:", cliente.bairro)
        print("Cidade:", cliente.cidade)
        print("Estado:", cliente.estado)
        print()

def consultar_cliente_por_cpf(clientes, cpf_consulta):
    for cliente in clientes:
        if cliente.cpf == cpf_consulta:
            print("Nome:", cliente.nome)
            print("CPF:", cliente.cpf)
            print("Idade:", cliente.idade)
            print("Data de Nascimento:", cliente.data_nascimento)
            print("Logradouro:", cliente.logradouro)
            print("Bairro:", cliente.bairro)
            print("Cidade:", cliente.cidade)
            print("Estado:", cliente.estado)
            print()
            break
    else:
        print("Cliente não encontrado.")

def consultar_contas_cliente(contas, cpf_consulta):
    for conta in contas:
        if conta.cliente.cpf == cpf_consulta:
            print("Número da Conta:", conta.numero)
            print("Agência:", conta.agencia)
            print("Cliente:", conta.cliente.nome)
            print("Saldo:", conta.saldo)
            print()
    else:
        print("Nenhuma conta encontrada para o CPF informado.")

def consultar_saldo_e_extrato(contas, numero_conta):
    for conta in contas:
        if conta.numero == numero_conta:
            print("Saldo disponível:", conta.consultar_saldo())
            print("Extrato:")
            extrato = conta.consultar_extrato()
            if extrato:
                print(extrato)
            else:
                print("Não foram realizadas movimentações.")
            break
    else:
        print("Conta não encontrada.")

def main():
    clientes = []
    contas = []

    while True:
        print("\n=== Menu ===")
        print("1. Cadastrar Cliente")
        print("2. Cadastrar Conta")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Consultas")
        print("6. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cliente = cadastrar_cliente()
            clientes.append(cliente)
            print("Cliente cadastrado com sucesso!")

        elif escolha == "2":
            cpf = input("Digite o CPF do cliente: ")
            cliente_encontrado = None
            for cliente in clientes:
                if cliente.cpf == cpf:
                    cliente_encontrado = cliente
                    break
            if cliente_encontrado:
                conta = cadastrar_conta(cliente_encontrado)
                contas.append(conta)
                print("Conta cadastrada com sucesso!")
            else:
                print("Cliente não encontrado.")

        elif escolha == "3":
            numero_conta = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor do depósito: "))
            for conta in contas:
                if conta.numero == numero_conta:
                    if conta.depositar(valor):
                        print("Depósito realizado com sucesso!")
                    else:
                        print("Valor de depósito inválido.")
                    break
            else:
                print("Conta não encontrada.")

        elif escolha == "4":
            numero_conta = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor do saque: "))
            for conta in contas:
                if conta.numero == numero_conta:
                    if conta.sacar(valor):
                        print("Saque realizado com sucesso!")
                    else:
                        print("Saque inválido.")
                    break
            else:
                print("Conta não encontrada.")

        elif escolha == "5":
            while True:
                print("\n=== Menu de Consultas ===")
                print("1. Consultar Usuários")
                print("2. Consultar Cliente por CPF")
                print("3. Consultar Contas do Cliente")
                print("4. Consultar Saldo e Extrato")
                print("5. Voltar")

                escolha_consultas = input("Escolha uma opção: ")

                if escolha_consultas == "1":
                    consultar_usuarios(clientes)
                elif escolha_consultas == "2":
                    cpf_consulta = input("Digite o CPF do cliente: ")
                    consultar_cliente_por_cpf(clientes, cpf_consulta)
                elif escolha_consultas == "3":
                    cpf_consulta = input("Digite o CPF do cliente: ")
                    consultar_contas_cliente(contas, cpf_consulta)
                elif escolha_consultas == "4":
                    numero_conta = int(input("Digite o número da conta: "))
                    consultar_saldo_e_extrato(contas, numero_conta)
                elif escolha_consultas == "5":
                    break
                else:
                    print("Opção inválida. Escolha novamente.")

        elif escolha == "6":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Escolha novamente.")


if __name__ == "__main__":
    main()

