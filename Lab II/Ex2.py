from datetime import date


class Account:
    def __init__(self, Id=0, balance=0.0, annualInterestRate=0.0):
        self.__id = Id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate
        self.__dateCreated = date.today()

    def getId(self):
        return self.__id

    def getBalance(self):
        return self.__balance

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def getDateCreated(self):
        return self.__dateCreated

    def getMonthlyInterestRate(self):
        return (self.__annualInterestRate / 100) / 12

    def withdraws(self, withdraw):
        self.__balance -= withdraw

    def deposit(self, deposit):
        self.__balance += deposit

