def addition(firstNum, secondNum):
    return firstNum + secondNum

def name(firstName, age):
    return "you are " + firstName + " you are " + str(age)

def fizzBuzz():
    for x in range(50):
        if((x % 3) == 0) and ((x % 5) == 0):
            print("FizzBuzz")
        elif ((x % 3) == 0):
            print("Fizz")
        elif ((x % 5) == 0):
            print("Buzz")
        else:
            print(x)

fizzBuzz() 
            
