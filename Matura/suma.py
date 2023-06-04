
plik = open('C:\\PROGRAMOWANIE\Matura\\identyfikator.txt', 'r')

wiersze = plik.readlines()
"""""
maxsuma = 0
maxnumery= []
for wiersz in wiersze :
    wiersz = wiersz.strip()
    suma_cyfr = 0
    for i in range(3 , len(wiersz)):
        suma_cyfr = suma_cyfr + int(wiersz[i])
    if suma_cyfr > maxsuma:
        maxsuma = suma_cyfr
        maxnumery.clear()
        maxnumery.append(wiersz)
    elif suma_cyfr == maxsuma:
        maxnumery.append(wiersz)
        
#for numer in maxnumery:
    #print(numer)
    
palindromy = []
for wiersz in wiersze:
    wiersz = wiersz.strip()
    seria = wiersz[0:3]
    numer = wiersz[3:9]
    
    czy_palindrom_seria = seria == seria[::-1]
    czy_palindrom_numer = numer == numer[::-1]
    
    
    if czy_palindrom_seria or czy_palindrom_numer:
        palindromy.append(wiersz)
        
for palindrom in palindromy:
    print(palindrom)
  """
    
    
    
niepoprawne_iden = []
for wiersz in wiersze:
    wiersz = wiersz.strip()
    znak_0 = (ord(wiersz[0]) -55) *7
    znak_1 = (ord(wiersz[1]) -55) *3
    znak_2 = (ord(wiersz[2]) -55) *1
    znak_4 = int(wiersz[4]) *7 
    znak_5 = int(wiersz[5]) *3 
    znak_6 = int(wiersz[6])*1 
    znak_7 = int(wiersz[7]) *7 
    znak_8 = int(wiersz[8])  *3 
    suma = znak_0 + znak_1+znak_2+znak_4+znak_5+znak_6+znak_7+znak_8 
    suma = suma % 10
    
    if suma != int(wiersz[3]):
        niepoprawne_iden.append(wiersz)
    
    
for ni in niepoprawne_iden:
    print(ni)