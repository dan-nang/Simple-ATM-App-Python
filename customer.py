from atm_card import ATMCard

class Customer:
    def __init__(self, id, cusPin = 123, cusBalance = 10000):
        self.id = id
        self.Pin = cusPin
        self.Balance = cusBalance

    def cekId(self):
        return self.id

    def cekPin(self):
        return self.Pin

    def cekSaldo(self):
        return self.Balance

    def withdrawBalance(self, nominal):
        self.Balance -= nominal

    def depositBalance(self, nominal):
        self.Balance += nominal
