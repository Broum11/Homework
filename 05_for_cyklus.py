'''
vytvořte soubor 05_for_cyklus.py

v listu lze zapsat data i takto pod sebe:

kde budou data = [
    8848, # Mount Everest
    8611, # K2
    4808, # Mont Blanc
    5895, # Kilimanjaro
    3776, # Mount Fuji
    5642, # Elbrus
    1603, # Sněžka
    1492, # Praděd
    1323, # Lysá hora
]
logika bude následující:
for cyklem projděte všechny nadmořské výšky a pokud:
je hora nižší jak 3000 m - napište X je nizká výška
je hora 3000 m a více, ale zároveň méně jak 6000 m - napište X je střední výška
jinak napište X je vysoká výška
.. kde X je výška '''    

data = [
    8848, 
    8611, 
    4808, 
    5895, 
    3776, 
    5642, 
    1603, 
    1492, 
    1323,
]

for nad_vyska in data :      
        if 3000 > nad_vyska :
            print(f'Nízká výška hor ze seznamu: {nad_vyska} m')
        if  3000 < nad_vyska < 6000:
            print(f'Střední výška hor ze seznamu: {nad_vyska} m') 
        elif nad_vyska > 6000:
            print(f'Vysoká výška hor ze seznamu: {nad_vyska} m')    

'''
for int in range(0, len(seznam_hor), 2):
    """cyklus projde prvky i od nultého do posledního (funkce len řekne počet prvků), po kroku 2 prvků  - for i in range(start, stop, step): 
     a řekne která hora je nízká, střední, vysoká """
    nadmorska_vyska = seznam_hor[int]
    nazev_hory = seznam_hor[int + 1]

    if nadmorska_vyska < 3000:
        print(f"Hora {nazev_hory} je nízká, měří: {nadmorska_vyska}m")
    elif 3000 <= nadmorska_vyska < 6000:
        print(f"Hora {nazev_hory} je střední výšky, měří: {nadmorska_vyska}m")
    else:
        print(f"Hora {nazev_hory} je vysoké výšky, měří: {nadmorska_vyska}m")             
        ''' 