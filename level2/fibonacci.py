def fibonacci(number:int):
    sequence = []
    for i in range(number):
        if i == 0:
            sequence.append(0)
        elif i == 1:
            sequence.append(1)
        else:
            sequence.append(sequence[-1]  + sequence[-2])
    return sequence

      

    
def main(): 
    print(fibonacci(4))

if __name__=="__main__":
    main()