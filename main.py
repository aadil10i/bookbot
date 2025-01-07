def main():
    book_path = "books/frankenstein.txt"
    text = open_book(book_path)
    num_words = get_num_words(text)

    print(num_words)
    print(count_occurances(text))

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

        for letter in lowered_case:
            if letter in char_count_dic:
                char_count_dic[letter] += 1
            else:
                char_count_dic[letter] = 1

    return char_count_dic

main()

