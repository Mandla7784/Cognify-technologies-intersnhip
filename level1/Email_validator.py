import regex

# functionto check if email is valid ot not 
def validating_email(email:str) -> str:
    pattern = 

    if email.split("@")[1].split("gamil")[1] not in string.punctuation:
        return "Invalid  email"

    elif  "@" not in email:
        return "Invalid"

    elif email.split("@")[1] is not "gmail.":
        return "invalid email"

    else:
        return "Valid email"

print(validating_email("mandla@gmai.com"))


