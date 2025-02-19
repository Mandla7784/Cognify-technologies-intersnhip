def file_handler(file_name):
    try:
        with open(file_name , "r") as file:
            content = file.readlines()
            return content

    except FileExistsError:
        return 
   

def main():
    content = file_handler("names.txt")
 
    for word  in content:
        print(word)
    

    

if __name__=="__main__":
    main()