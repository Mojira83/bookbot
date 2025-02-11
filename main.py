def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):   
    char_count = {}
    for character in text:
        lower_char = character.lower()
        if lower_char.isalpha():
            if lower_char in char_count:
                char_count[lower_char] += 1
            else:
                char_count[lower_char] = 1

    list_report = []
    for char, count in char_count.items():
        list_report.append({'name': char, "num": count})

    list_report.sort(reverse=True, key=sort_on)
    return list_report

def sort_on(list_report):
    return list_report["num"]    

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{count_words(file_contents)} words found in the document")
        
        char_list = count_characters(file_contents)
        
        for char in char_list:
            print(f"The '{char['name']}' character was found {char['num']} times")
        print("--- End report ---")

main()