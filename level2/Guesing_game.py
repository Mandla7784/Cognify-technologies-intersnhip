from random import randint

class Generator:

    @staticmethod 
    def get_random_numb():
        return randint(0 , 101)
    
def main():

    while True:
        number =  Generator.get_random_numb()
        print(number)

        user_input = int(input("Enter a number: "))

        if user_input < number:
            print("Too low")
        elif user_input > number:
            print("High")

        else:
            print(f"Wooray you got the number {number}")
            return
    


 
 
if __name__=="__main__":
    main()