plik = open('C:\\Programowanie\\Matura\\matura2022\\liczby.txt', 'r')

wiersze = plik.readlines()





ile = 0 
pierwsza = -1
for wiersz in wiersze:
    wiersz = wiersz.strip()
    if wiersz[0] == wiersz[len(wiersz) - 1]:
        ile += 1 
        if pierwsza == -1:
            pierwsza = wiersz


print (ile, pierwsza)

#420 = 2 * 2 * 3 * 5 * 7
# 210 > 105 > 35 > 7 > 1

def rozklad_na_czynniki(liczba):
    czynniki = []
    i = 2
    while liczba > 1 and i * i <=liczba:
        while liczba % i == 0:
            czynniki.append(i)
            liczba = liczba / i 
        i = i + 1

    if liczba > 1:
        czynniki.append(liczba)
    return czynniki


max_czynikow = -1
max_czynikow_liczba = -1
max_roznych_czynnikow = -1
max_roznych_czynnikow_liczba = -1

for wiersz in wiersze:
    liczba = int(wiersz)
    rozklad = rozklad_na_czynniki(liczba)

    if len(rozklad) > max_czynikow:
        max_czynikow = len(rozklad)
        max_czynikow_liczba = liczba
    
    rozne = set(rozklad)
    if len(rozne) > max_roznych_czynnikow:
        max_roznych_czynnikow = len(rozne)
        max_roznych_czynnikow_liczba = liczba

print(max_czynikow_liczba, max_czynikow, max_roznych_czynnikow_liczba, max_roznych_czynnikow)

def ile_dobrych_trojek(wiersze):
    trojki = []

    for i in range(0, len(wiersze)):
        liczba_1 = int(wiersze[i])
        for j in range(0, len(wiersze)):
            if i == j:
                continue

            liczba_2 = int(wiersze[j])
            if liczba_2 % liczba_1 == 0:
                for k in range(0, len(wiersze)):
                    if i == k or j == k:
                        continue

                    liczba_3 = int(wiersze[k])
                    if liczba_3 % liczba_2 == 0:
                        trojki.append([liczba_1, liczba_2, liczba_3])

                    



    return trojki



def ile_dobrych_piatek(wiersze):
    piatki = []

    for i in range(0, len(wiersze)):
        liczba_1 = int(wiersze[i])
        for j in range(0, len(wiersze)):
            if i == j:
                continue

            liczba_2 = int(wiersze[j])
            if liczba_2 % liczba_1 == 0:
                for k in range(0, len(wiersze)):
                    if i == k or j == k:
                        continue

                    liczba_3 = int(wiersze[k])
                    if liczba_3 % liczba_2 == 0:
                        for m in range(0, len(wiersze)):
                            if i == k or j == k or k == m:
                                continue

                            liczba_4 = int(wiersze[m])
                            if liczba_4 % liczba_3 == 0:
                                for n in range(0, len(wiersze)):
                                    if i == m or j == m or k == m or m == n:
                                        continue




                                    liczba_5 = int(wiersze[n])
                                    if liczba_5 % liczba_4 == 0:
                                        piatki.append([liczba_1, liczba_2, liczba_3, liczba_4, liczba_5])
                                



    return piatki



dobre_trojki = ile_dobrych_trojek(wiersze)
dobre_piatki = ile_dobrych_piatek(wiersze)
print(len(dobre_trojki))
print(len(dobre_piatki))


for trojka in dobre_trojki:
    print(trojka)




