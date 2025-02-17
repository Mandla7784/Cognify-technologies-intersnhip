import regex

# functionto check if email is valid ot not 
def validating_email(email:str) -> str:
    pattern ="^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$"

    if  regex.match(pattern , email):
        return "valid  email"
    else:
        return "Invalid "

    # elif  "@" not in email:
    #     return "Invalid"

    # elif email.split("@")[1] is not "gmail.":
    #     return "invalid email"

    # else:
    #     return "Valid email"

print(validating_email("mandlagmai.com"))


