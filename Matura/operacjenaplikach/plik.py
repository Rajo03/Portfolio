plik = open("test.txt", "a")
if plik.writable():
    plik.write(input("Wprowadz tekst: ")+ "\n")

plik.close()

plik = open("test.txt", "r")

if plik.readable():
    
    for l in plik:
        print(l)