while True:
    play = input("Do you want to play? (yes/no): ").strip().lower()
    if play != 'yes':
        exit()
    how_manny_numbers = int(input("how many numbers do you want to use? "))
    question = []
    operators = ["power", "times", "divide", "plus", "minus"]
    if how_manny_numbers < 1:
        print("you need to enter a number greater than 0")
    else:
        for i in range(how_manny_numbers):
            number = input(f'what do you want to make number {i + 1}? ')
            if number.isdigit():
                question.append(int(number))
            else:
                print("you need to enter a number")
                break
            if i != how_manny_numbers - 1:
                operator = input("what operator do you want to use: ")
                question.append(operator)
        for j in range(len(operators)):
            while operators[j] in question:
                for k in range(len(question)):
                    if question[k] == operators[j]:
                        if operators[j] == "power":
                            result = question[k-1]**question[k+1]
                            print(f'{question[k-1]}^{question[k+1]} = {result}')
                        elif operators[j] == "times":
                            if question[k-1] == 0 or question[k+1] ==0:
                                if question[k-1] == 0:
                                    NewNumber = input("You can't multiply by 0, please enter a new number: ")
                                    if NewNumber.isdigit():
                                        question[k-1] = int(NewNumber)
                                if question[k+1] == 0:
                                    NewNumber = input("You can't multiply by 0, please enter a new number: ")
                                    if NewNumber.isdigit():
                                        question[k+1] = int(NewNumber)
                            result = question[k-1] * question[k+1]
                            print(f'{question[k-1]}*{question[k+1]} = {result}')
                        elif operators[j] == "divide":
                            if question[k-1] == 0 or question[k+1] == 0:
                                if question[k-1] == 0:
                                    NewNumber = input("You can't divide by 0, please enter a new number: ")
                                    if NewNumber.isdigit():
                                        question[k-1] = int(NewNumber)
                                if question[k+1] == 0:
                                    NewNumber = input("You can't divide by 0, please enter a new number: ")
                                    if NewNumber.isdigit():
                                        question[k+1] = int(NewNumber)
                            result = question[k-1] / question[k+1]
                            print(f'{question[k-1]}/{question[k+1]} = {result}')
                        elif operators[j] == "plus":
                            result = question[k-1] + question[k+1]
                            print(f'{question[k-1]}+{question[k+1]} = {result}')
                        elif operators[j] == "minus":
                            result = question[k-1] - question[k+1]
                            print(f'{question[k-1]}-{question[k+1]} = {result}')
                        else:
                            print("Something went wrong, please try again and use real operators (power, times, divide, plus, minus)")
                            break
                        question.pop(k+1)
                        question.pop(k)
                        question.pop(k-1)                        
                        question.insert(k-1, result)
                        break