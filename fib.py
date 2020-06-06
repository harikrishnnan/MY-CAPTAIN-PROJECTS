
def fib(n1):
    if(n1==0):
        return 0
    elif(n1==1):
        return  1
    else:
        return fib(n1-1)+fib(n1-2)
    
    
n=int(input("enter n"))
for i in range(n):
    print(fib(i))