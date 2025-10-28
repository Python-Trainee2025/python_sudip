def check(x, y):
    x = x.replace(" ", "").lower()
    y = y.replace(" ", "").lower()
    if sorted(x) == sorted(y):
        print('The words are anagrams')
    else:
        print('The words are not anagrams')

x = input("Enter the first word: ")
y= input("Enter the second word: ")
check(x, y)


