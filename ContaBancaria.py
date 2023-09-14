class ContaBancaria:

    CONTA_CORRENTE = "CC";
    CONTA_POUPANCA = "CP";

    def __init__(self, numero, titular, saldo, tipoConta, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.tipoConta = tipoConta
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, tipoConta, valor):
        if tipoConta == self.tipoConta:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f"Valor de {valor} sacado com sucesso da {self.tipoConta}.")
            
            if self.saldo < valor:
                print("Saldo insuficiente.")

        if tipoConta != self.tipoConta:
            print(f"Vocé não pode sacar da {self.tipoConta} usando a conta {tipoConta}.")

    def extrato(self):
        print(f"Conta: {self.numero}\nSaldo: R${self.saldo:.2f}")


def criarConta(numero, titular, saldo, limite):
    conta = ContaBancaria(numero, titular, saldo, limite)
    return conta