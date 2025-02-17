

def calculator(num1:int  , num2:int , operand) -> int:

    if num2 == 0:
        raise ZeroDivisionError
    else:

        if operand =="+":return num1 + num2

        elif operand == "-": return num1 - num2

        elif operand == "*": return num1  * num2

        return num1 / num2

def main():
   while True:
        num1 = int(input("Enter num1: "))
        num2 = int(input("Enter num2: "))

        if num1 == "q".lower():
            break
        else:

      
            operand = input(("Enter operation (): "))
            answer =     calculator(num1  , num2 , operand)
                
            print(answer)

    

if __name__=="__main__":
    main()