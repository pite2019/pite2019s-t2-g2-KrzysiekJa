#
#Banking simulator. Write a code in python that simulates the banking system. 
#The program should:
# - be able to create new banks
# - store client information in banks
# - allow for cash input and withdrawal
# - allow for money transfer from client to client
#If you can think of any other features, you can add them.
#This code shoud be runnable with 'python kol1.py'.
#You don't need to use user input, just show me in the script that the structure of your code works.
#If you have spare time you can implement: Command Line Interface, some kind of data storage, or even multiprocessing.
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.

class bank:
    def __init__(self, name, money, information_storage):
        self.name  = ""
        self.money = 10000000
        self.information_storage = []
        
    def moneyInput(self, change):
        self.money += change
    
    def moneyWithdrawal(self, change):
        self.money -= change
    
    def clientInformation(self, information_stream):
        self.information_storage.append(information_stream)

class client:
    def __init__(self, name1, name2, money):
        self.name1  = ""
        self.name2  = ""
        self.money  = 1000
        
    def moneyInput(self, change):
        self.money += change
    
    def moneyWithdrawal(self, change):
        self.money -= change

clent_list = [client(i,i,2900) for i in range(10)]


bank1 = bank("JP Morgan", 200000000, clent_list[:5])
bank2 = bank("PKO", 100000000, clent_list[5:])

print(bank1, bank2)