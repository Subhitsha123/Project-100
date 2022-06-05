class Atm(object):
    def __init__(self,card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number

    def CashWithdrawal(self):
        print("Your cash has been withdrawn")

    def BalanceEnquiry (self):
        print("This is your bank balance")   

bank_atm = Atm('1357 0981 7358 3809', '375839')   

print(bank_atm.card_number)

print(bank_atm.CashWithdrawal())
print(bank_atm.BalanceEnquiry())





