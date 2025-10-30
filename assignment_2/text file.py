def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            print(f"Total number of words: {len(words)}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")


count_words_in_file("example.txt")
