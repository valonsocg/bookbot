def get_num_words(book_text):
    words = len(book_text.split())
    return words

def char_count(book_text):
    char_counted = {}
    lower_case_text = book_text.lower()
    for i in lower_case_text:
        
        if i in char_counted:
            char_counted[i]+=1
        else:
            char_counted[i] = 1
    return char_counted

def sort_on(items):
    return items["num"]

def sort_dictionaries(char_dictionary):
    list_values = []
    for char in char_dictionary:
        count = char_dictionary[char]
        list_values.append({"char":char,"num":count})
    list_values.sort(reverse=True,key=sort_on)
    return list_values
    