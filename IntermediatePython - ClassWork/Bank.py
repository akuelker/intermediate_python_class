import BankClient #keep in same directory or you need a package

cust1 = BankClient.Client('Audrey', 100000)
print(cust1.name, cust1.balance, cust1.acctNumber)

cust2 = BankClient.Client('George')
print(cust2.name, cust2.balance, cust2.acctNumber)

cust1.withdraw(50)
cust2.withdraw(50)
