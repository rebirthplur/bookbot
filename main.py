import sys

def main(path):
    book_path = path
    text = get_book_text(book_path)
    counttext = count(text)
    char_count = get_char_count(text)
    sort_char = sort_char_count(char_count)
    pretty_count = char_count_output(sort_char)
    #print(f"Found {counttext} total words")
    #print(char_count)
    #print(sort_char)
    print(f"""========BOOKBOT=========
Analyzing book found at {book_path}...
-----------Word Count -------------
Found {counttext} total words
---------Character Count-----------
{pretty_count}
           """ )



def get_book_text(path):
    with open(path) as file:
        return file.read()

from stats import count
from stats import get_char_count
from stats import sort_char_count
from stats import char_count_output


if len(sys.argv) > 1:
    main(sys.argv[1])
else: 
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)









