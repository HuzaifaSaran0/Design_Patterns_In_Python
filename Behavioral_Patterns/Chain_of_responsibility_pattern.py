from abc import ABC, abstractmethod

class ATMHandler(ABC):
    def __init__(self, denomination, next_handler=None):
        self.denomination = denomination
        self.next_handler = next_handler

    @abstractmethod
    def handle(self, amount):
        pass


class ConcreteATMHandler(ATMHandler):
    def handle(self, amount):
        dividend, remainder = divmod(amount, self.denomination)

        if dividend > 0:
            print(f"Handler{self.denomination} processed {dividend} notes of {self.denomination}")

        if remainder > 0 and self.next_handler:
            self.next_handler.handle(remainder)
        elif remainder > 0 and not self.next_handler:
            print(f"Cannot dispense {remainder}, unsupported amount.")


# Smallest denomination last
h100 = ConcreteATMHandler(100)
h500 = ConcreteATMHandler(500, h100)
h1000 = ConcreteATMHandler(1000, h500)

print("ATM Machine:")
h1000.handle(2500)   # 2x1000 + 1x500
h1000.handle(2600)   # 2x1000 + 1x500 + 1x100
h1000.handle(2000)   # 2x1000
h1000.handle(1255)   # 1x1000 + 2x100 + "cannot dispense 55"
