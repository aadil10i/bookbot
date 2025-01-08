def main():
    book_path = "books/frankenstein.txt"
    text = open_book(book_path)
    num_words = get_num_words(text)

    print(f"{num_words}: words found in the document \n")

    occurence_list = count_occurances(text)
    for key, value in occurence_list:
        print(f"the {key} character was found {value} times \n")
    print("--- End report ---")

def open_book(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    total_count = 0
    words = text.split()

    for i in range (0, len(words)):
        total_count += 1
        
    return total_count

def count_occurances(text):
    char_count_dic = {}
    for char in text:
        lowered_case = char.lower()
        # remove non alphabetical characters
        if "a" <= lowered_case <= "z":
            for letter in lowered_case:
                if letter in char_count_dic:
                    char_count_dic[letter] += 1
                else:
                    char_count_dic[letter] = 1
            
            char_count_list = list(char_count_dic.items())
            char_count_list.sort(key=lambda item: item[1], reverse=True)

    return char_count_list

main()

