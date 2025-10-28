
value = input("Enter a word or phrase: ")
cleaned_value = value.replace(" ", "").lower()
x=cleaned_value[::-1]
if cleaned_value == x:
    print("the word is palindrome.")
else:
    print("the word is not a palindrome.")