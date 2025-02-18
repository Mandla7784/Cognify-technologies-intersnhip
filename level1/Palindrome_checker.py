
def isPalindrome(string:str) -> bool:

    string_copy = string[::-1]

    if string_copy == string:
        return True

    return False



def main():
    print(isPalindrome("madam"))




 
if __name__=="__main__":
    main()