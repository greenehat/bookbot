from stats import word_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents






def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = get_book_text(path_to_file)
    num_words = word_count(file_contents)
    print(f"{num_words} words found in the document")
    #print(file_contents)
    

main()