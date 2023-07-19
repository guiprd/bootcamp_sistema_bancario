from historico import Historico


class Conta:
    def __init__(self, titular, saldo=0.0):
        self._saldo = saldo
        self.titular = titular
        self.historico = Historico()

    def saldo(self):
        return self._saldo

    def deposito(self):
        valor = float(input("Valor a depositar (ex: 529.98): "))
        if valor <= 0:
            print("Valor para depósito não permitido")
            return False

        self._saldo = self._saldo + valor
        self.historico.transacoes.append("depósito de {}".format(valor))
        print(f"O valor de {valor} reais foi depositado.")
        return True
