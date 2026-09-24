class Bank:
    def __init__(self, balance: list[int]):
        self.bound = len(balance)
        self.bal = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        ok = False
        account1 -= 1
        account2 -= 1

        if (
            (0 <= account1 < self.bound)
            and (0 <= account2 < self.bound)
            and self.bal[account1] >= money
        ):
            self.bal[account1] -= money
            self.bal[account2] += money
            ok = True

        return ok

    def deposit(self, account: int, money: int) -> bool:
        ok = False

        account -= 1
        if 0 <= account < self.bound:
            self.bal[account] += money
            ok = True

        return ok

    def withdraw(self, account: int, money: int) -> bool:
        account -= 1
        ok = False
        if (0 <= account < self.bound) and self.bal[account] >= money:
            self.bal[account] -= money
            ok = True
        return ok
