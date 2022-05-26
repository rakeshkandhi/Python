def Prime_number(n):
    if(n==1):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True
if (__name__=="__main__"):
    n=int(input("Enter the number:"))
    num=Prime_number(n)
    if(num):
        print(n," is a prime")
    else:
        print(n," is not prime")
