from banco import Banco
from conta import Conta


class CriarBanco:
    if __name__ == '__main__':
        banco = Banco()
        conta1 = Conta("28.100-3")
        conta2 = Conta("03.281-0")

        banco.cadastrar(conta1)
        banco.cadastrar(conta2)

        banco.creditar(conta1.get_numero(), 28.10)
        banco.creditar(conta2.get_numero(), 10.28)

        banco.transferir(conta1.get_numero, conta2.get_numero, 281)

        print(banco.saldo(conta1.get_numero()))

    