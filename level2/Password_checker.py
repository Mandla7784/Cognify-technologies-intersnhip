import string


capitalalphabets= string.ascii_uppercase
smallalphabets= string.ascii_letters
specialchar=string.punctuation
digits=string.digits



print(string.punctuation)
def password_checker(password:str)  -> str:
 
    special = False
    uppercase = False
    lowercase =False
    number = False



    if len(password) < 8:
        return "Invalid"

    for char in password:

        if char in capitalalphabets:uppercase = True
        elif char in smallalphabets:lowercase =True

        elif char in specialchar:special  = True
        elif char in digits: number = True

    return     special , uppercase , lowercase , number

      

    
def main(): 
    print(password_checker("w@@@MANDLA45"))

if __name__=="__main__":
    main()