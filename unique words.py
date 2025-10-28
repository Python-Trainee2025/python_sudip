import string
text = input("Enter a sentence or paragraph: ")
cleaned_text = text.translate(str.maketrans('', '', string.punctuation)).lower()
words = cleaned_text.split()
unique_words = set(words)
print(f"Number of unique words: {len(unique_words)}")