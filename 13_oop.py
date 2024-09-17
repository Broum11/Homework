'''
3. vytvořte soubor 13_oop.py
a v něm třídu Planeta, která bude obsahovat:
atributy:
- poradi 
- nazev
a metodu info
která řekne "Toto je [název planety] a je [pořadí] od Slunce"
vytvořte 2 instance
- Země
- a nějakou další planetu
'''
class Planeta:
    def __init__(self,nazev,poradi):
        self.nazev = nazev
        self.poradi = poradi

    def info(self): # metoda
        print(f"Toto je {self.nazev} a je {self.poradi} od Slunce")     

Zeme = Planeta ('Země', 3) # Vytvoření dvou instancí
Merkur = Planeta ('Merkur', 1)

Zeme.info() # metoda se musí zavolat
Merkur.info()