def fib_iterative(n):
    a=0
    b=1
    for i in range(n):
        print(a)
        a,b = b,a+b

n=int(input("ennter the no. of terms:"))
fib_iterative(n)

def fib_recursive(n, a=0, b=1):
    if n == 0:
        return
    print(a)
    fib_recursive(n - 1, b, a + b)


n = int(input("Enter the number of terms: "))
fib_recursive(n)
