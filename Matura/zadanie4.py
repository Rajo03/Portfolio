plik = open('przyklad.txt', 'r')
wiersze = plik.readlines()


def zakodujnapis(instrukcje):
    napis = ""
    
    for instrukcja in instrukcje:
        instrukcja = instrukcja.strip().split(' ')
        polecenie = instrukcja[0]
        wartosc = instrukcja[1]
        
        if polecenie == "DOPISZ":
            napis += wartosc
        elif polecenie == "ZMIEN":
            napis = list(napis)
            napis[len(napis) - 1] = wartosc
            napis = ''.join(napis)
        elif polecenie == "USUN":
            napis = list(napis)
            napis.pop(len(napis) - 1)
            napis = ''.join(napis)
        else:
            indeks_litery = napis.index(wartosc)
            
            ascii_litery = ord(wartosc) + 1
            if ascii_litery > 90:
                ascii_litery -= 26
                
                
            napis = list(napis)
            napis[indeks_litery] = chr(ascii_litery)
            napis = ' '.join(napis)
            
    return napis

print(zakodujnapis(wiersze))