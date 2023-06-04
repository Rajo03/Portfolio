plik = open('przyklad.txt')

wiersze = plik.readlines()

# print(wiersze)
maks = -1
mini = 256

for i in wiersze:
    wejscie = str(wiersze.split())
    print(i)
print(max(i))

# for i in range(200):
#     wejscie = list()

