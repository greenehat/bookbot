from stats import word_count
from stats import char_count
from stats import dict_listed
from stats import sort_on
import sys



def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    
    
    path_to_file = sys.argv[1]
    file_contents = get_book_text(path_to_file)
    num_words = word_count(file_contents)
    character_count = char_count(file_contents)
    list_of_dictionaries = dict_listed(character_count)
    list_of_dictionaries.sort(reverse=True, key=sort_on)


    print("============ BOOKBOT =============")
    print(f"Analizing book found at {path_to_file}...")
    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count ---------")
    for item in list_of_dictionaries:
        for key in item:
            print(f"{key}: {item[key]}")
    print("============= END =============")
    
        

main()