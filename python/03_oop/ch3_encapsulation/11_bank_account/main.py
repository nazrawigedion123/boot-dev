class BankAccount:
    def __init__(self, account_number: str, initial_balance: float) -> None:
        self.account_number=account_number
        self.balance=initial_balance

    def get_account_number(self) -> str:
        return self.account_number

    def get_balance(self) -> float:
        return self.balance

    def deposit(self, amount: float) -> None:
        if amount<=0:
            raise ValueError("cannot deposit zero or negative funds")
        self.balance+=amount

    def withdraw(self, amount: float) -> None:
        if amount<=0:
            raise ValueError("cannot withdraw zero or negative funds")
        if self.balance<amount:
            raise ValueError("insufficient funds")
        self.balance-=amount

