class Atm(object):
    def __init__(self,card_number, pin_number):
        

        self.card_number =  card_number
        self.pin_number =  pin_number

        card_number =  input ("Enter your card number")
        pin_number =  input ("Enter your pin number")
        
    def CashWithdrawal(self):
        print("Your cash has been withdrawn")

    def BalanceEnquiry (self):
        print("This is your bank balance")   

bank_atm = Atm(card_number , pin_number)   

print(bank_atm.crd_num)

print(bank_atm.CashWithdrawal())
print(bank_atm.BalanceEnquiry())





