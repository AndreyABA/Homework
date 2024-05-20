class Bankaccount:
    def __init__(self, zxc, negr, balance):
        self.zxc=zxc
        self.negr=negr
        self.balance=balance
    def deposit(self, summa):
        self.balance+=summa*0.99
    def sigma(self, summa):
        if self.balance-summa*1.01>=0:
            self.balance-=summa*1.01
        else:
            print('недостаточно деньжат')
    def checkbalance(self):
        return self.balance
account=Bankaccount(228133769, 'щзягрпщшзгфуркпщ', 2000)
account.deposit(700)
print(account.checkbalance())
account.sigma(500)
print(account.checkbalance())