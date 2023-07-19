from historico import Historico
import variaveis

class Conta:
    def __init__(self, titular, saldo=0.0):
        self.quantidade_saques = 0
        self._saldo = saldo
        self.titular = titular
        self.historico = Historico()

    def saldo(self):
        return self._saldo

    def deposito(self):
        valor = float(input("Valor a depositar (ex: 529.98): "))
        if valor <= 0:
            print("Valor para depósito não permitido")

        else:
            self._saldo = self._saldo + valor
            self.historico.transacoes.append("depósito de R$ %.2f" % valor)
            print(f"O valor de {valor} reais foi depositado.")

    def saque(self):
        if self.quantidade_saques < variaveis.QUANTIDADE_SAQUES:
            valor = float(input("Valor a sacar (ex: 529.98): "))
            if valor <= 0:
                print("Valor de saque não permitido")

            elif valor > 500:
                print("Valor de saque acima do permitido por transação.")

            elif valor > self._saldo:
                print("Saldo insuficiente")

            else:
                self._saldo -= valor
                self.historico.transacoes.append("saque de R$ %.2f" % valor)
                print(f"Saque realizado com sucesso.")

                self.quantidade_saques += 1

        else:
            print("Limite de saques do dia atingido.")