'''
Vytvořte soubor 04_funkce.py
ve kterém budou 2 funkce:
1) funkce pro výpočet obsahu kruhu
2) funkce pro výpočet obvodu kruhu
vstupní parametr bude poloměr  '''


polomer = int(input("Zadejte poloměr kruhu: "))

def obsah_kruhu (polomer):
    return (polomer**2) * 3.14

vypocet_obsahu_kruhu = (obsah_kruhu(polomer))
print('Výpočet obsahu kruhu je :')
print(vypocet_obsahu_kruhu)   


def obvod_kruhu(polomer):
    return(2 * polomer * 3.14)

vypocet_obvodu =(obvod_kruhu(polomer))
print('Výpočet obvodu kruhu je :')
print(vypocet_obvodu)




'''
řecké písmeno PI definujte jako 3.14 nebo importujte modul math, kde se nachází konstanta pi


import math

polomer = int(input("Zadejte poloměr kruhu: "))

def obsah_kruhu (polomer):
    return(round(polomer**2 * (math.pi),2))

vypocet_obsahu_kruhu = (obsah_kruhu(polomer))
print('Výpočet obsahu kruhu je :')
print(vypocet_obsahu_kruhu)   


def obvod_kruhu(polomer):
    return(round( 2 * polomer * (math.pi),2))

vypocet_obvodu =(obvod_kruhu(polomer))
print('Výpočet obvodu kruhu je :')
print(vypocet_obvodu) '''