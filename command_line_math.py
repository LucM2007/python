number1 = input("what do you want to put in number 1? ")
a = int(number1)
number2 = input("what do you want to put in number 2? ")
b = int(number2)


while True:
    operator = input("Enter wich operator you wanne use: ").capitalize()

    match operator:
        case "Times":
            if(a==0 or b==0):
                print("You can't multiply by 0")
                if(a==0):
                    a = int(input("Enter a new number for number 1: "))
                else:
                    b = int(input("Enter a new number for number 2: "))
            print( a*b)  
            break
        case "Plus":
            print(a+b)
            break
        case "Minus":
            print(a-b)
            break
        case "Divide":
            if(a==0 or b==0):
                print("You can't multiply by 0")
                if(a==0):
                    a = int(input("Enter a new number for number 1: "))
                else:
                    b = int(input("Enter a new number for number 2: "))
            
            print(a/b)
            break
        case "Power":
            print(a**b)
            break
        case _:
            print("Invalid operator. Please try again. you can chose between Times, Plus, Minus, Divide and Power")