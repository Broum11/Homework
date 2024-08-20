
''' vytvořte 02_user.py kde
uživatel zadá své jmeno a věk pomocí input
uložte tyto informace do souboru
02_user.txt '''
''' 
'r'  je pro čtení souboru.
'w'  je pro zápis do souboru. Pokud soubor již existuje, bude vymazán. Pokud neexistuje, vytvoří se nový soubor.
'a'  slouží k připojení k souboru. To znamená přidání nového obsahu na konec existujícího souboru.
'r+' je jak pro čtení, tak pro zápis do souboru.'''


cesta = '02_users.txt' # cesta souboru se může psát rovnou do závorky,bez toho,abych dělal proměnou
jmeno = input("Zadejte své jméno: ")
vek = input("Zadejte svůj věk: ")

with open(cesta, mode='a') as file:
    file.write("Jmeno: " + jmeno +"\n" + "vek: " + vek )

