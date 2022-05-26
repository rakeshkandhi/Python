def SOE(n):
    for i in range(0,n+1):
        Prime_number.append(True)
    for j in range(2,n+1,1):
        if(Prime_number[j]==True):
            for k in range(j*2,n+1,j):
                Prime_number[k]=False
if(__name__=="__main__"):
    Prime_number=[]
    n=int(input("Enter the number:"))
    SOE(n)
    print("Prime numbers are:")
    for i in range(0,n+1):
        if(Prime_number[i]):
            print(i,end=" ")
