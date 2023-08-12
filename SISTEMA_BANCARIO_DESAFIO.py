class Banco:
    def __init__(self):
        self.saldo = 0
        self.saques_realizados = 0
        self.extrato = []

    def depositar(self, valor):
        """
        Realiza um depósito na conta bancária.

        Args:
            valor (float): O valor a ser depositado.

        Returns:
            bool: True se o depósito for bem-sucedido, False caso contrário.
        """
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            return True
        else:
            return False

    def sacar(self, valor):
        """
        Realiza um saque na conta bancária.

        Args:
            valor (float): O valor a ser sacado.

        Returns:
            bool: True se o saque for bem-sucedido, False caso contrário.
        """
        if self.saques_realizados < 3 and 0 < valor <= 500 and self.saldo >= valor:
            self.saldo -= valor
            self.extrato.append(f"Saque: -R$ {valor:.2f}")
            self.saques_realizados += 1
            return True
        else:
            return False

    def consultar_saldo(self):
        """
        Consulta o saldo atual da conta bancária.

        Returns:
            float: O saldo disponível na conta.
        """
        return self.saldo

    def consultar_extrato(self):
        """
        Consulta o extrato das movimentações na conta bancária.

        Returns:
            str: Uma string com o extrato das movimentações.
        """
        if self.extrato:
            return "\n".join(self.extrato)
        else:
            return "Não foram realizadas movimentações"


def main():
    banco = Banco()

    while True:
        print("\n=== Menu ===")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Consultar Saldo")
        print("4. Consultar Extrato")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            valor = float(input("Digite o valor do depósito: "))
            if banco.depositar(valor):
                print("Depósito realizado com sucesso!")
            else:
                print("Valor de depósito inválido.")

        elif escolha == "2":
            valor = float(input("Digite o valor do saque: "))
            if banco.sacar(valor):
                print("Saque realizado com sucesso!")
            else:
                print("Saque inválido.")

        elif escolha == "3":
            saldo = banco.consultar_saldo()
            print(f"Saldo disponível: R$ {saldo:.2f}")

        elif escolha == "4":
            extrato = banco.consultar_extrato()
            print("Extrato:")
            print(extrato)

        elif escolha == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Escolha novamente.")


if __name__ == "__main__":
    main()
