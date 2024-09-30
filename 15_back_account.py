'''
vytvořte soubor 15_back_account.py
bude obsahovat třídu BankAccount (Bankovní účet)
atributy:
- owner (str) - jméno vlastníka účtu
- balance (int) - stav konta
oba atributy lze zadat v __init__, balance bude mít defaultně hodnotu 0 pokud není zadáno jinak
Metody:
- deposit (vklad)
- withdraw (výběr)
- print (vytiskne stav konta) - jméno a aktuální stav
Příklad použití:
muj_ucet = BankAccount('Jan Novák', 1000)
muj_ucet.deposit(10000)
muj_ucet.withdraw(500)
muj_ucet.print
'''
class BankAccount:
    def __init__(self, owner: str, balance: int = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, castka: int):
        if castka > 0:
            self.balance += castka
            print(f'Vloženo: {castka} Kč. Nový stav: {self.balance} Kč.')
        else:
            print('Vklad musí být kladný.')

    def withdraw(self, castka: int):
        if 0 < castka <= self.balance:
            self.balance -= castka
            print(f'Vybráno: {castka} Kč. Nový stav: {self.balance} Kč.')
        else:
            print('Nedostatečný zůstatek')

    def print(self):
        print(f'Vlastník účtu: {self.owner}, Aktuální stav: {self.balance} Kč.')

if __name__ == "__main__":
    muj_ucet = BankAccount('Fanda Vlk', 1000)
    muj_ucet.deposit(10000)
    muj_ucet.withdraw(500)
    muj_ucet.print()
