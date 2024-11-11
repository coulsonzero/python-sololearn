class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def __repr__(self):
        """
        print the result of obj
        example: print(obj)
        """
        return "Account Balance: {}".format(self._balance)

    def deposit(self, amount):
        self._balance += amount


if __name__ == '__main__':
    acc = BankAccount(0)
    acc.deposit(int(input()))
    print(acc)

# 123
# Account Balance: 123