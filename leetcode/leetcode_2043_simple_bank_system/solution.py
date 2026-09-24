class Bank:
    def __init__(self, balance: list[int]):
        self.bound = len(balance)
        self.bal = balance

    def _validate_account(self, account):
        account -= 1
        assert 0 <= account <= self.bound
        return account

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        ok = True
        try:
            account1 = self._validate_account(account1)
            account2 = self._validate_account(account2)
            assert self.bal[account1] >= money
            self.bal[account1] -= money
            self.bal[account2] += money
        except AssertionError:
            ok = False
        return ok

    def deposit(self, account: int, money: int) -> bool:
        ok = True
        try:
            account = self._validate_account(account)
            self.bal[account] += money
        except AssertionError:
            ok = False
        return ok

    def withdraw(self, account: int, money: int) -> bool:
        ok = True
        try:
            account = self._validate_account(account)
            assert self.bal[account] >= money
            self.bal[account] -= money
        except AssertionError:
            ok = False
        return ok
