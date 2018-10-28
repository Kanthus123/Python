#It helps building a chain of objects. Request enters from one end and keeps going from object to object till it finds the suitable handler.

#For example, you have three payment methods (A, B and C) setup in your account;
#each having a different amount in it. A has 100 USD, B has 300 USD and C having 1000 USD and the preference for payments is chosen as A then B then C.
#You try to purchase something that is worth 210 USD. Using Chain of Responsibility,
#first of all account A will be checked if it can make the purchase, if yes purchase will be made and the chain will be broken.
#If not, request will move forward to account B checking for amount if yes chain will be broken otherwise the request will keep forwarding till it finds the suitable handler.
#Here A, B and C are links of the chain and the whole phenomenon is Chain of Responsibility.

class Account:

    def __init__(self):
        self.successor = None
        self.balance = 0

    def set_next(self, account):
        self.successor = account

    def pay(self, amount_to_pay):
        if self.can_pay(amount_to_pay):
            print('Paid {} using {}'.format(amount_to_pay, self.__class__.__name__))
            self.successor.pay(amount_to_pay)
        else:
            raise Exception('None of the accounts have enough balance')

    def can_pay(self, amount):
        return self.balance >= amount

class Bank(Account):

    def __init__(self, balance):
        self.balance = balance

class PayPal(Account):

    def __init__(self, balance):
        self.balance = balance

class Bitcoin(Account):

    def __init_(self, balance):
        self.balance = balance

if __name__ == '__main__':

    # Let's prepare a chain like below
    #     bank->paypal->bitcoin
    # First priority bank
    # If bank can't pay then paypal
    # If paypal can't pay then bit coin

    bank = Bank(100)
    paypal = PayPal(200)
    bitcoin = Bitcoin(300)
    bank.set_nex(paypal)
    paypal.set_next(bitcoin)

    bank.pay(259)
      # Cannot pay using Bank, Proceeding...
      # Cannot pay using PayPal, Proceeding...
      # Paid 259 using Bitcoin
