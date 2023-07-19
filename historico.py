import datetime


class Historico:

    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        if not len(self.transacoes):
            print("Não foram realizadas movimentações.")
        else:
            # print(f"data abertura: {self.data_abertura}")
            print("transações: ")
            for t in self.transacoes:
                print("-", t)