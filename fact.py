def factorial(n):
    if n == 0 or n == 1:
        print(1)
    else:
        for i in range(2,n):
            n *= i

        print(n)


n = int(input('Enter a number: '))
factorial(n)
