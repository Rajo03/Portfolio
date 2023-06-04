plik = open('sygnaly.txt')

wiersze = plik.readlines()

# for i in range(1000):
#     linia = wiersze[i]
#     if (i+1) % 40 == 0:
#         print(linia[9], end="")
# print()
# max = 0
# slowo = ""
# for i in range(1000):
#      linia = wiersze
#      sortowanie = set(wiersze)
# print(sortowanie)



for i in range(1000):
     linia = input()
     maks = 0
     mini = 255
     for j in list(linia):
          if ord(j) > maks:
               maks = ord(j)
          if ord(j) < mini:
               mini = ord(j)
          delta = maks - mini
     if delta <= 10:
          print(linia)
#print(maks, mini, delta)
