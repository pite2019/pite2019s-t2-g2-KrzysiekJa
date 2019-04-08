import weakref


class client:
    def __init__(self, name1, name2, money):
        self.name1 = name1
        self.name2 = name2
        self.money = 2000

    def moneyInput(self, change):
        self.money += change
                
    def moneyWithdrawal(self, change):
        if self.money - change < 0:
            print("Sorry. Client have not enough money.")
            return None
        self.money -= change
        
class bank:
    def __init__(self, bankName = 'Somewhere in Switzerland', bankMoney = 10000000):
        self.bankName  = bankName
        self.bankMoney = bankMoney
        self.client_list         = []
        self.information_storage = []
    
    def moneyInput(self, change):
        self.bankMoney += change
        self.information_storage.append(("Bank have input", change))
    
    def moneyWithdrawal(self, change):
        self.bankMoney -= change
        self.information_storage.append(("Bank have withdrawal", change))
    
    def addClient(self, name1, name2, amount):
        self.client_list.append(client(name1, name2, amount))
        self.information_storage.append((name1, name2, amount))
        self.moneyInput(amount)
    
    def moneyChangeClients(self, indexNumber1, indexNumber2, exchange):
        client1 = self.client_list[indexNumber1]
        client2 = self.client_list[indexNumber2]
        client1.moneyWithdrawal(exchange)
        client2.moneyInput(exchange)
        self.information_storage.append((client1.name1, client1.name2, client2.name1, client2.name2, "exchanged", exchange))
    
    def addInformation(self, information_stream):
        self.information_storage.append(information_stream)
    
    def delClient(self, name1, name2):
        for client in self.client_list:
            if (client.name1 == name1 and client.name2 == name2):
                index = self.client_list.index(client)
        del self.client_list[index]
        self.addInformation((name1, name2, 'is out.'))



def main():
    
    bank1 = bank("JP Morgan", 2000000000)
    bank2 = bank("PKO", 1000000000)
    
    bank1.addClient('Licciardi', 'Vincenzo', 30000000)
    
    bank1.addInformation('Ministry of Finance: You will be called by parlamentary commission.')
    
    new_clients_list = ['David', 'Rockeffeler', 180000000, 'Wlad', 'Dracula', 15000000, 'Geogre', 'Soros', 2500000, 'Wladimir', 'Putin', 10000000000]
    
    for i in range (0, len(new_clients_list) - 2, 3):
        bank1.addClient(new_clients_list[i], new_clients_list[i+1], new_clients_list[i+2])
        print('Added to ', bank1.bankName, ': ',new_clients_list[i], new_clients_list[i+1])
    
    new_clients_list = ['Jan', 'Kulczyk', 22000000, 'Urszula', 'Moździerz', 15000, 'Modry', 'Robert', 500, 'Wladimir', 'Putin', 10000000000]
    
    for i in range (0, len(new_clients_list) - 2, 3):
        bank2.addClient(new_clients_list[i], new_clients_list[i+1], new_clients_list[i+2])
        print('Added to ', bank2.bankName, ': ',new_clients_list[i], new_clients_list[i+1])
    
    print("\n", bank1.bankName, ":\n", bank1.bankMoney, "\n", bank2.bankName, ":\n", bank2.bankMoney, "\n")
    print(bank1.bankName, ":\n", bank1.information_storage, "\n", bank2.bankName, ":\n", bank2.information_storage) 
    
    bank2.delClient('Wladimir', 'Putin')
    print("\n", bank1.bankName, ":\n", bank1.bankMoney, "\n", bank2.bankName, ":\n", bank2.bankMoney, "\n")
    
    bank2.moneyChangeClients(1, 2, 500) 
    bank2.addClient('Filipiak', 'Janusz', 45000000)
    
    print("\n", bank1.bankName, ":\n", bank1.bankMoney, "\n", bank2.bankName, ":\n", bank2.bankMoney, "\n")
    bank1.addInformation('Ministry of Finance: Prima Aprilis.')
    print("\n",bank1.bankName, ":\n", bank1.information_storage, "\n", bank2.bankName, ":\n", bank2.information_storage)



if __name__=='__main__':
    main()
