import regex

# functionto check if email is valid ot not 
def validating_email(email:str) -> str:
    pattern ="^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$"

    if  regex.match(pattern , email):
        return "valid  email"
    else:
        return "Invalid "




def main():

    print(validating_email("mandlagmai.com"))


if __name__=="__main__":
    main()

