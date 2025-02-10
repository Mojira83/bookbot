def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):   
    char_count = {}
    for character in text:
        lower_char = character.lower()
        if lower_char in char_count:
            char_count[lower_char] += 1
        else:
            char_count[lower_char] = 1
    return char_count
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(count_words(file_contents))
        print(count_characters(file_contents))

main()