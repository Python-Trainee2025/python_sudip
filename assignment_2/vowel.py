def check_vowel(a):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in a:
        if i in vowels:
            print(f"{i} is a vowel")
            count += 1
    print(f"{count} vowels were found")


a = input("Enter a string: ").lower()
check_vowel(a)