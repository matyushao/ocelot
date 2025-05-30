"""
Разработка системы управления банковскими счетами
Цель:Создать систему управления банковскими счетами с использованием ООП для моделирования различных
типов счетов и операций с ними.
Шаги для выполнения:

1. Определение базового класса `BankAccount`:
    - Атрибуты: `owner` (владелец счета, строка), `__balance`(баланс счета, изначально 0, приватный).
    - Методы:
        - Конструктор `__init__(self, owner, balance=0)`
        - `deposit(self, amount)`: добавляет сумму к балансу, если сумма положительная, иначе выбрасывает `ValueError`
        - `withdraw(self, amount)`: снимает сумму с баланса, если на счету достаточно средств,
        иначе выбрасывает `ValueError`
        - `get_balance(self)`: возвращает текущий баланс.
2. Создание класса `SavingsAccount` (наследуется от `BankAccount`):
    - Дополнительный атрибут: `interest_rate` (процентная ставка 0.05).
    - Метод `apply_interest(self)`: начисляет проценты на остаток по счету.
3. Создание класса `CheckingAccount` (наследуется от `BankAccount`):
    - Переопределение метода `withdraw(self, amount)`: позволяет снимать средства без ограничений по балансу.

    После создания структуры необходимо:

    1. создать экземпляр класса `SavingsAccount`
    2. внести депозит 500
    3. списать с него 100
    4. применить начисление процентов
    5. написать тест с использованием pytest, что сумма > 0
"""
import pytest

class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма депозита должна быть положительной")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Средств на счету недостаточно, пополните счет")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)


class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self._BankAccount__balance -= amount


def test_saving_account():
    account = SavingsAccount("Matvey")
    account.deposit(500)
    account.withdraw(100)
    account.apply_interest()
    assert account.get_balance() > 0

