import json
import re


        
class Bank:
    def __init__(self, bank_name = 'Somewhere in Switzerland', bank_money = 10000000):
        self.bank_name  = bank_name
        self.bank_money = bank_money
        self.__clients_file = '%sfile.txt' %(self.bank_name)
        
        file = open(self.__clients_file, 'x')
        file.close()
        
    def creAccount(self, name, last_name, amount):
        self.bank_money += amount
        file   = open(self.__clients_file, 'a')
        client = {
          'name': name,
          'last_name': last_name,
          'money': amount,
          'credit': 0
        }
        json_str = json.dumps(client)
        file.write(json_str)
        file.close()
        
        return client
       
    def delAccount(self, name, last_name):
        with open(self.__clients_file, 'r') as file:
            lines = file.readlines()
        file = open(self.__clients_file, 'w')
        for indx in lines:
            if (re.search('^{"name": "%s", "last_name": "%s"' %(name, last_name),indx) != None):
                tmp = json.loads(indx)
                amount = tmp['money']
                self.bank_money -= amount
                continue
            file.write(indx)
        file.close()
        
        try:
            return tmp
        except:
            raise NameError('None exist.')
        
    def moneyDeposit(self, name, last_name, change):
        self.bank_money += change
        with open(self.__clients_file, 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for indx in lines:
                if (re.search('^{"name": "%s", "last_name": "%s"' % (name, last_name),indx) != None):
                    tmp  = json.loads(indx)
                    tmp['money'] += change
                    tmp2 = json.dumps(tmp)
                    file.write(tmp2)
                    continue
                file.write(indx)
            file.truncate()
        file.close()
        
        try:
            return tmp
        except:
            raise NameError('None exist.')
            
    def moneyWithdrawal(self, name, last_name, change):
        self.bank_money -= change
        error = 0
        with open(self.__clients_file, 'r') as file:
            lines = file.readlines()
        with open(self.__clients_file, 'w') as file:
            for indx in lines:
                if (re.search('^{"name": "%s", "last_name": "%s"' % (name, last_name),indx) != None):
                    tmp  = json.loads(indx)
                    tmp['money'] -= change
                    if tmp['money'] < 0:
                        tmp['money']   += change
                        self.bank_money += change
                        error = 1
                    tmp2 = json.dumps(tmp)
                    file.write(tmp2)
                    continue
                file.write(indx)
        file.close()
        
        if error == 1:
            return "Operation failed- not enough money."
        try:
            return tmp
        except:
            raise NameError('None exist.')
    
    def exchangeBetwClients(self, name, last_name, nameX, last_nameX, exchange):
        try:
            moneyWithdrawal(name, last_name, exchange)
        except (NameError, "Operation failed- not enough money."):
            return "Operation failed- problems with clients' money."
        else:
            moneyDeposit(nameX, last_nameX, exchange)
    
    def giveCredit(self, name, last_name, amount):
        if amount > 0.1 * self.bank_money:
            return "Unfortunately, not possible."
        with open(self.__clients_file, 'r') as file:
            lines = file.readlines()
        with open(self.__clients_file, 'w') as file:
            for indx in lines:
                if (re.search('^{"name": "%s", "last_name": "%s"' % (name, last_name),indx) != None):
                    tmp  = json.loads(indx)
                    tmp['credit'] = amount
                    tmp2 = json.dumps(tmp)
                    file.write(tmp2)
                    continue
                file.write(indx)
        file.close()
        
        try:
            return tmp
        except:
            raise NameError('None exist.')



def main():
    
    bank1 = Bank("JP Morgan", 20000000000)
    bank2 = Bank("PKO", 1000000000)
    bank3 = Bank("Transfer Bank", 1500000000)
    
    
    new_clients_list = ['Licciardi', 'Vincenzo', 30000000, 'David', 'Rockeffeler', 180000000, 'Wlad', 'Dracula', 15000000, 'Geogre', 'Soros', 2500000, 'Wladimir', 'Putin', 10000000000]
    
    for i in range (0, len(new_clients_list) - 2, 3):
        result = bank1.creAccount(new_clients_list[i], new_clients_list[i+1], new_clients_list[i+2])
        print('Added to ', bank1.bank_name, ': ', result)
    
    new_clients_list = ['Jan', 'Kulczyk', 22000000, 'Urszula', 'Moździerz', 15000, 'Robert', 'Robert', 500, 'Wladimir', 'Putin', 10000000000]
    
    for i in range (0, len(new_clients_list) - 2, 3):
        result = bank2.creAccount(new_clients_list[i], new_clients_list[i+1], new_clients_list[i+2])
        print('Added to ', bank2.bank_name, ': ', result)
    
    new_clients_list = ['Filipiak', 'Janusz', 45000000,]
    
    for i in range (0, len(new_clients_list) - 2, 3):
        result = bank2.creAccount(new_clients_list[i], new_clients_list[i+1], new_clients_list[i+2])
        print('Added to ', bank3.bank_name, ': ', result)
    
    
    print(bank2.bank_name, "gives credit:", bank2.giveCredit("Robert", "Robert", 1500))
    print(bank2.bank_name, "gives credit:", bank2.giveCredit("Wladimir", "Putin", 2000))
    
    


if __name__=='__main__':
    main()