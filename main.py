import os
import time

def number_of_words(words) -> int:
    return len(words.split())

# def char_calc(words) -> dict:
#     char_d = {chr(x): 0 for x in range(ord('a'), ord('z')+1)}
#     bad_chars = [';', '$', '!', "'", ',', ')', '(', '.','-', ':', '[', ']', '#', '*', '?', '"', '_', '/', '%', '@']
#     words = words.split()
#     for word in words: 
#         word = word.lower()
#         for char in word:
#             if char not in bad_chars:
#                 if str.isdigit(char) == False:
#                     char_d[char] += 1
#     return char_d

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents
  
def char_calculater(words) -> dict:
    chars = {}
    for c in words:
        lowered = c.lower()
        if lowered in chars:
            # Enter this path for every iteration besides the first one. 
            chars[lowered] += 1
        else:
            # Enter this clause for the first iteration
            chars[lowered] = 1
    return chars

def sort_dict(character_dict) -> None:
    sorted_list =[]
    for key in character_dict:
        if key.isalpha()== True:
            temp = {key: character_dict[key]}
            sorted_list.append(temp)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(dict):
    for key in dict:
        return dict[key]
           
def main():
    start_time = time.time()
    file_path = os.getcwd()
    file_path = file_path + "/books/frankenstein.txt"
    
    file_contents = get_book_text(file_path)
    word_count = number_of_words(file_contents)
    
    char_count_dict = char_calculater(file_contents)
    dict_list = sort_dict(char_count_dict)

    end_time = round(time.time() - start_time, 2)
    
    print(f"--- Begin report of {file_path[57:]} ---\n")
    print(f"{word_count} words found in the document.\n")
    for item in dict_list:
        for key in item:
            print(f"The '{key}' character was found {item[key]} times")
    print(f"\nScript run time: {end_time} seconds.")
    print("\n--- End Report ---")
    
if __name__ == "__main__":
    main()