import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <path_to_book>")
        return

    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = count_words(text)
    char_occurancies_dictionary = get_character_occurancies_dictionary(text)
    
    print_report(book_path, num_words, char_occurancies_dictionary)

def count_words(text):
    return len(text.split())

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_character_occurancies_dictionary(text):
    occurancies_dictionary = {}
    for char in text.lower():
        occurancies_dictionary[char] = occurancies_dictionary.get(char, 0) + 1
    
    return occurancies_dictionary

def print_report(book_path, num_words, char_occurancies_dictionary):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for char, occurancies in sorted(char_occurancies_dictionary.items(), key=lambda item: item[1], reverse=True):
        if char.isalpha():
            print(f"The '{char}' character was found {occurancies} times\n")
    print(f"--- End report ---")

main()