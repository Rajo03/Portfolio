plik = open('mecz.txt', 'r')

wiersze = plik.readline().strip()

#print(len(wiersze))
il = 0
for i in range(1, len(wiersze)):
    if wiersze[i] != wiersze[i-1]:
        il+= 1
#print(il)

lA = 0
lB = 0

for i in range(len(wiersze)):
    if wiersze[i] == 'A':
        lA += 1
    else:
        lB += 1
        if (lA >= 1000 or lB >= 1000) and abs(lB-lA) >= 3:
            break
#print(f' Drużyna A: {lA}:{lB} Druzyna B: ')

licznik_passy_A = 0
licznik_passy_B = 0
tablica_passy_A = []
tablica_passy_B = []

for i in wiersze:
    if i == 'A':
        if licznik_passy_B >= 10:
            tablica_passy_B.append(licznik_passy_B)
        licznik_passy_B = 0
        licznik_passy_A += 1
    else:
        if licznik_passy_A >= 10:
            tablica_passy_A.append(licznik_passy_A)
        licznik_passy_A = 0
        licznik_passy_B += 1

print("licznik pass druzyny A:",len(tablica_passy_A)," licznik pass druzyny B:",len(tablica_passy_B),"suma",len(tablica_passy_A) + len(tablica_passy_B))

print("max A", max(tablica_passy_A),"max A",max(tablica_passy_B) )