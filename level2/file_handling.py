def file_handler(file_name):

    try:
        with open(file_name , "r") as file:
            content = file.readline
            return content

    except FileExistsError:
        print("Opps")




def main():
    content = file_handler("")
    print(content)

if __name__=="__main__":
    main()