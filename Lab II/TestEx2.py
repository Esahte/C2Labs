from Ex2 import Account


def main():
    account = Account(1122, 20000, 4.5)
    account.withdraws(2500)
    account.deposit(3000)

    print(account.getBalance(), account.getMonthlyInterestRate() *
          account.getBalance(), account.getDateCreated())


main()
