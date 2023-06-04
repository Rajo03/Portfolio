plik = open('C:\\Programowanie\\Matura\\szachy.txt', 'r')

wiersze = plik.readlines()


plansze = []

for i in range(0, len(wiersze) , 9):
    plansza = []
    for j in range(0, 8): 
        plansza.append(wiersze[i+j].strip())
    plansze.append(plansza)

print(plansze)



ile_plansz_conajmniej_jedna_kolumna = 0

ile_max_pustych_kolumn = 0

for plansza in plansze:
    ile_pustych_na_danej_planszy = 0
    for kolumna in range(0, 8):
        czy_pusta_kolumna = True
        for wiersz in range(0, 8):
            if plansza[wiersz][kolumna] != '.':
                czy_pusta_kolumna = False
                break
        if czy_pusta_kolumna == True:
            ile_pustych_na_danej_planszy += 1
    if ile_pustych_na_danej_planszy > 0:
        ile_plansz_conajmniej_jedna_kolumna += 1
        if ile_pustych_na_danej_planszy > ile_max_pustych_kolumn:
           ile_max_pustych_kolumn = ile_pustych_na_danej_planszy

print(f'ile_plansz_conajmniej_jedna_kolumna: {ile_plansz_conajmniej_jedna_kolumna}')
print(f'ile_max_pustych_kolumn : {ile_max_pustych_kolumn}')





ile_plansz_w_rownowadze = 0 
ile_bierek_najmniej_w_rownowadze = 99999
pionki = ['k', 's', 'h', 'g', 'w', 'p']
for plansza in plansze:
    czy_plansza_w_rownowadze = True
    plansza = ''.join(plansza)
    for pionek in pionki:
        if plansza.count(pionek) != plansza.count(pionek.upper()):
            czy_plansza_w_rownowadze = False
            break
    if czy_plansza_w_rownowadze == True:
        ile_plansz_w_rownowadze += 1
        ile_pol = len(plansza)
        ile_pustych = plansza.count('.')
        ile_bierek = ile_pol - ile_pustych
        if ile_bierek < ile_bierek_najmniej_w_rownowadze:
            ile_bierek_najmniej_w_rownowadze = ile_bierek


print(f'ile_plansz_w_rownowadze: {ile_plansz_w_rownowadze}')
print(f'ile_bierek_najmniej_w_rownowadze: {ile_bierek_najmniej_w_rownowadze}')




def ile_szachów(król_symbol, wieza_symbol):
    ile_szachów = 0
    for plansza in plansze:
        czy_szachuje = False
        for wiersz in range(0, 8):
            for kolumna in range(0, 8):
                if plansza[wiersz][kolumna] == król_symbol:
                    wiersz_w_gore = wiersz - 1
                    wiersz_w_dol = wiersz + 1
                    kolumna_w_prawo = kolumna + 1
                    kolumna_w_lewo = kolumna - 1

                    while wiersz_w_gore >= 0:
                        if plansza[wiersz_w_gore][kolumna] == wieza_symbol:
                            czy_szachuje = True
                            break
                        if plansza[wiersz_w_gore][kolumna] != '.':
                            break
                        wiersz_w_gore -= 1 

                    while wiersz_w_dol <= 7:
                        if plansza[wiersz_w_dol][kolumna] == wieza_symbol:
                            czy_szachuje = True
                            break
                        if plansza[wiersz_w_dol][kolumna] != '.':
                            break
                        wiersz_w_dol += 1

                    while kolumna_w_prawo <= 7:
                        if plansza[wiersz][kolumna_w_prawo] == wieza_symbol:
                            czy_szachuje = True
                            break
                        if plansza[wiersz][kolumna_w_prawo] != '.':
                            break
                        kolumna_w_prawo += 1

                    while kolumna_w_lewo >= 0:
                        if plansza[wiersz][kolumna_w_lewo] == wieza_symbol:
                            czy_szachuje = True
                            break
                        if plansza[wiersz][kolumna_w_lewo] != '.':
                            break
                        kolumna_w_lewo -= 1

        if czy_szachuje:
            ile_szachów += 1

    return ile_szachów

print(f"ile białych {ile_szachów('K', 'w')}")
print(f"ile czarnych {ile_szachów('k', 'W')}")
