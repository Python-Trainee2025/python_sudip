def check_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        print('prime number')
    else:
        print('composite number')


a = int(input('Enter a number: '))
check_prime(a)

