def fibo(num):
    a=0
    b=1
    print("The Fibonacci series are :")
    for i in range(0,num):
        c=a+b
        a=b
        b=c
        print(c," ",end=" ")
if __name__=="__main__":
    num=int(input("Enter the number of series to be printed:"))
    fibo(num)
    
