'''
vytvořte třídu MobilePhone
vymyslete k této třídě smysluplné atributy a metody
- 3-5 atributy (jaké vlastnosti a parametry by mohl mít mobilní telefon?)
- 2 metody (jaké chování (metody) by telefon mohl mít?)
vytvořte 2 instance
'''

class MobilePhone:
    def __init__(self,nazev,vodeodolnost,vyzvaneni,):
        self.nazev = nazev
        self.vodeodolnost = vodeodolnost
        self.vyzvaneni = vyzvaneni

    def vlastnosti(self): # metoda
        print(f"Mobilní telefon značky {self.nazev} s odolností proti vodě a kritím: {self.vodeodolnost}. Oblíbené vyzvánění je {self.vyzvaneni} ")     

Nokia = MobilePhone ('Nokia', 'IP65', 'ringtone') # Vytvoření dvou instancí
Samsung = MobilePhone ('Samsung', 'IP30', 'ding dang dong')

Nokia.vlastnosti() # metoda se musí zavolat
Samsung.vlastnosti()