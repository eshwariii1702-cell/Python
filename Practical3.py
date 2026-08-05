# ---------------------------------
# Strategy Design Pattern
# ---------------------------------

# Base Strategy Class
class PaymentMethod:

    def make_payment(self, amount):
        pass


# UPI Payment Strategy
class UPIPayment(PaymentMethod):

    def make_payment(self, amount):
        print(f"Payment of ₹{amount} completed using UPI.")


# Debit Card Strategy
class DebitCardPayment(PaymentMethod):

    def make_payment(self, amount):
        print(f"Payment of ₹{amount} completed using Debit Card.")


# Context Class
class PaymentGateway:

    def __init__(self, payment_method):
        self.payment_method = payment_method

    def change_method(self, payment_method):
        self.payment_method = payment_method

    def process_payment(self, amount):
        self.payment_method.make_payment(amount)


# ---------------------------------
# Main Program
# ---------------------------------

upi = UPIPayment()

gateway = PaymentGateway(upi)

gateway.process_payment(1200)

debit = DebitCardPayment()

gateway.change_method(debit)

gateway.process_payment(750)
