def count_words(text):
    words = text.split()
    return len(words)

def count_chars(string):
    lower_string = string.lower()
    char_dict = {}
    for char in lower_string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    char_list = []
    for name, num in count_chars(file_contents).items():
        if name.isalpha():
            list_dict = {}
            list_dict["name"] = name
            list_dict["num"] = num
            char_list.append(list_dict)
    
    char_list.sort(reverse=True, key=sort_on)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file_contents)} words found in the document\n")
    for char_dict in char_list:
        print(f"The {char_dict["name"]} character was found {char_dict["num"]} times")
    print("--- End report ---")
    
   
main()