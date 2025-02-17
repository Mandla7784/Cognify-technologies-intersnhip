class TemperatureConverter:
    @staticmethod
    def convert(temperature ,unit_measurement):
        # converting F to C
        if unit_measurement == "F":
            temperature = (temperature * (9/5))  + 32
        else:
            # C to F
            temperature = (temperature - 32) / (9/5)
        return temperature

user_temp = int(input('Enter the temp:  '))
print()
user_units = input("Enter unit (F or C:  ").upper()



results =  TemperatureConverter.convert(user_temp , user_units)
print(f"Answer is {results}")

    
