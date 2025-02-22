def word_count(file_contents):
    count = len(file_contents.split())
    return count

def char_count(file_contents):
    chars_counted = {}
    char_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",
    "q","r","s","t","u","v","w","x","y","z"," ",",","'",".","?",'"',"(",")"]
    for char in char_list:
        lowercase = file_contents.lower()
        count = lowercase.count(char)
        chars_counted[char] = count
    return chars_counted