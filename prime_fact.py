import math
def Primefact(n):
    len1=-1
    if(n==1):
        fact.append(1)
        expo.append(0)
    d=2
    while(n>1):
        k=0
        while(n%d==0):
            n=n/d
            k=k+1
        if(k>0):
            fact.append(d)
            expo.append(k)
        d=d+1
if __name__=="__main__":
    fact=[]
    expo=[]
    n=int(input("Enter the number:"))
    len1=-1
    print("The Prime factorization of ",n," is:")
    Primefact(n)
    for i in range(0,len(fact)):
        print(fact[i],end=" ")
        print(expo[i])
