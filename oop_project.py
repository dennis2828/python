from bank_accounts import *

Dennis = BankAccount(1000, "Dennis")
Dave = BankAccount(2000, "Dave")

Dennis.getBalance()
Dave.getBalance()

Dennis.deposit(100000)

Dave.withdraw(10000)
Dave.withdraw(10)

Dave.transfer(10000, Dennis)
Dave.transfer(1000, Dennis)

Jim = InterestRewardAcct(1000,"Jim")

Jim.getBalance()

Jim.deposit(100)
Jim.transfer(100,Dennis)

Blaze = SavingsAcct(1000, "Blaze")

Blaze.getBalance()

Blaze.deposit(100)

Blaze.transfer(10000, Dennis)

