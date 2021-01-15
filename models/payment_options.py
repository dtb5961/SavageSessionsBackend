import enum

class PaymentOption(int,enum.Enum):
    Zelle = 1
    CashApp = 2
    Cash = 3
    Other = 4

    def __json__(self):
        return self.name

