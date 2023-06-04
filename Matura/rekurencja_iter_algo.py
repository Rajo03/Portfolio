

def rekurs_ciag (n):
    if (n == 1 or n == 0):
        print (1)
    if (n%2 | n>1):
        print ((n//4)+1)
    if (n%2 !=0 | n>1):
        print ((3*n+1)+1) 
    
#rekurs_ciag(17)
    

def iter_ciag (n):
   while n> 0:
        if (n == 1 or n == 0):
            print (1)
        if (n%2 | n>1):
            print ((n//4)+1)
        if (n%2 !=0 | n>1):
            print ((3*n+1)+1) 

iter_ciag(3)
