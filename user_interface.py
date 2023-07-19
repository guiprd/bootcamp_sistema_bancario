from time import sleep


import variaveis
MENU = '''

Funções disponíveis:
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => '''

def interactions(conta):

    while variaveis.interaction != "q":
        print(MENU)
        variaveis.interaction = str(input("O que deseja fazer? "))
        if variaveis.interaction == "d":
            # Função de depósito
            conta.deposito()
        elif variaveis.interaction == "s":
            #  Função de saque
            print("Saque realizado com sucesso")

        elif variaveis.interaction == "e":
            # Função de extrato
            print("Extrato:")

        elif variaveis.interaction == "q":
            sleep(1)
            print("Fechando o sistema...")
            sleep(1)

        else:
            print("Função não existe, tente novamente uma função disponível:")
