def word_count(file_contents):
    count = len(file_contents.split())
    return count

def char_count(file_contents):
    chars_counted = {}
    char_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",
    "q","r","s","t","u","v","w","x","y","z"," ",",","'",".","?",'"',"(",")","æ","â","ê","ë","ô"]
    for char in char_list:
        lowercase = file_contents.lower()
        count = lowercase.count(char)
        chars_counted[char] = count
    return chars_counted



def dict_listed(chars_counted):
    dict_list = []
    for chars in chars_counted:
        if chars.isalpha() == True:
            value = chars_counted[chars]
            single_dict = {}
            single_dict[chars] = value
            dict_list.append(single_dict)    
        else:
            continue
    return dict_list

def sort_on(dict):
    for char in dict:
        return dict[char]

