class Client:
    accountNumber = 1
    def __init__(self, name, balance= 0.0):
        self.name = name
        self.balance = balance
        self.acctNumber = Client.accountNumber
        Client.accountNumber +=1 #get a new number for each client
    def withdraw(self, amount): #self is needed in every method
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount;
            print(self.balance, "is left")

            
#Code to check - called a test harness
#joeBlow = Client('Joe Blow', 50)
#print(joeBlow.name, joeBlow.balance, joeBlow.acctNumber)
