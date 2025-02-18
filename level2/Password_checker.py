from string import ascii_letters , punctuation ,ascii_uppercase ,digits


capitalalphabets= ascii_uppercase
smallalphabets= ascii_letters
specialchar=punctuation
digits= digits




def password_checker(password:str)  -> tuple[bool]:
 
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