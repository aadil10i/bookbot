def main():
    book_path = "books/frankenstein.txt"
    text = open_book(book_path)
    num_words = get_num_words(text)
    print(num_words)

def get_num_words(text):
    total_count = 0
    words = text.split()

    for i in range (0, len(words)):
        total_count += 1
        
    return total_count

def open_book(path):
    with open(path) as f:
        return f.read()


main()

