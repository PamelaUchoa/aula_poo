from conta import Conta


class BancoLista:
    def __init__(self):
        self.contas = []

    def cadastrar(self, conta: Conta):
        self.contas[self.indice] = conta
        self.indice += 1

    def procurar_conta(self, numero):
        i = 0
        achou = False
        while achou is False and i < self.indice:
            if self.contas[i].get_numero() == numero:
                achou = True
            else:
                i += 1
        if achou is True:
            return self.contas[i]
        else:
            return None

    def creditar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.creditar(valor)
        else:
            print("Conta Inexistente!")

    def debitar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.debitar(valor)
        else:
            print("Conta Inexistente!")

    def saldo(self, numero):
        conta = self.procurar_conta(numero)
        if conta:
            conta.get_saldo()
        else:
            print("Conta Inexixstente!")

    def transferir(self, origem, destino, valor):
        contaorigem = self.procurar_conta(origem)
        contadestino = self.procurar_conta(destino)

        if contaorigem and contadestino:
            saldo = contaorigem.get_saldo()
            if saldo >= valor:
                contaorigem.debitar(valor)
                contadestino.creditar(valor)
            else:
                print("Saldo Insuficiente!")
        else:
            print("Conta Inexistente!")
