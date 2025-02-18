def file_handler(file_name):

    try:
        with open(file_name , "r") as file:
            content = file.readlines()
            return content

    except FileExistsError:
        return 
   

def main():
    content = file_handler("names.txt")
    counts = 0 
    for word  in content:
        counts +=  content.count(word)
        print(counts)

    

if __name__=="__main__":
    main()