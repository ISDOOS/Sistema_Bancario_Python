# Sistema Bancário em Python

# Inicialização do saldo da conta
saldo = 0.0

# Função para realizar depósito na conta
def depositar(valor):
    """
    Função para realizar um depósito na conta.
    
    Parâmetros:
    valor (float): Valor a ser depositado na conta.
    
    Retorno:
    bool: True se o depósito for bem-sucedido, False caso contrário.
    """
    global saldo
    if valor > 0:
        saldo += valor
        return True
    else:
        return False

# Função para realizar saque na conta
def sacar(valor):
    """
    Função para realizar um saque na conta.
    
    Parâmetros:
    valor (float): Valor a ser sacado da conta.
    
    Retorno:
    bool: True se o saque for bem-sucedido, False caso contrário.
    """
    global saldo
    if valor > 0 and saldo >= valor:
        saldo -= valor
        return True
    else:
        return False

# Função para exibir o extrato da conta
def extrato():
    """
    Função para exibir o extrato da conta.
    """
    global saldo
    if saldo == 0:
        print("Não foram realizadas movimentações")
    else:
        print(f"Extrato da Conta:")
        print(f"Saldo atual: R$ {saldo:.2f}")

# Função principal para interagir com o usuário
def main():
    """
    Função principal para interagir com o usuário e executar operações bancárias.
    """
    print("Bem-vindo(a) ao Sistema Bancário!")
    
    while True:
        print("\nOpções:")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Extrato")
        print("4 - Sair")
        
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            valor = float(input("Digite o valor a ser depositado: "))
            if depositar(valor):
                print("Depósito realizado com sucesso!")
            else:
                print("Valor de depósito inválido!")
        elif opcao == 2:
            valor = float(input("Digite o valor a ser sacado: "))
            if sacar(valor):
                print("Saque realizado com sucesso!")
            else:
                print("Saque não autorizado. Verifique o saldo.")
        elif opcao == 3:
            extrato()
        elif opcao == 4:
            print("Saindo do Sistema Bancário. Até logo!")
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
