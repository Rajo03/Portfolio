from math import gcd, factorial

plik = open('przyklad.txt', 'r')

wiersze3 = plik.readlines()
wiersze2 = wiersze3.strip()
wiersze = int(wiersze2)

# potega = 1
# i=0
# t=[]
# while (True):
#     potega = pow(3,i)
#     t.append(potega)
#     if potega>10000:
#         break;
#     i += 1
# zlicz = 0
#
# for a in wiersze:
#     a=int(a.strip())
#     print(a)
#     if a in t:
#       zlicz+=1
#       print(a)
#
#  print(zlicz)

# def sil(n):
#     s = 1
#     for i in range(2, n+1):
#         s *= 1
#     return s
#
# for liczba in wiersze:
#     liczba = liczba.strip()
#     liczbav2 = int(liczba)
#     suma = 0
#     for i in liczba:
#         suma += sil(int(i))
#     if liczbav2 == suma:
#         print(liczbav2)

