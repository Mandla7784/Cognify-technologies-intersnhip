def file_handler(file_name):
    try:
        with open(file_name , "r") as file:
            content = file.read().lower()
            words = content.split()

        return words

   

    except FileExistsError:

        print(f"Error: {file_name} not found.")
        return []
   

def main():
    # counting occurrences of each word
    words  = file_handler("names.txt")
    word_count   = {}

    for word in words:
        word_count[word] = word_count.get(word , 0 ) + 1

    my_words =dict(sorted(word_count.items()))


    for word ,count in my_words.items():
        print(f"{word} : {count}")



if __name__=="__main__":
    main()