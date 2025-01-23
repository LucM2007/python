import random
how_manny_tries = 0
while True:
    if how_manny_tries > 0:
        want_to_go_again = input("Do you want to play again? (yes/no): ").lower()
    else:
        want_to_go_again = input("Do you want to play? (yes/no): ").lower()
    if want_to_go_again != "yes" and want_to_go_again != "no":
        continue
    elif want_to_go_again == "no":
        exit()
    elif want_to_go_again == "yes":
        random_number = random.randint(1, 100)
        how_manny_tries = 0
        while True:
            your_number = input("Enter a number between 1 and 100: ")
            if not your_number.isdigit():
                print("Please enter a valid number")
                continue
            your_number = int(your_number)
            if random_number > your_number:
                print("Too low")
                how_manny_tries += 1
            elif random_number < your_number:
                print("Too high")
                how_manny_tries += 1
            else:
                print("You guessed it!")
                print(f"You guessed it in {how_manny_tries+1} tries")
                break
