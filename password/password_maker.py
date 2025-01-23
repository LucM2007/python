import random
print("hi i will make a password for you")
password = []
usable_characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0","!", "#", "$", "%", "&" ,"'" ,"(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "]", "^", "_","`", "{", "|", "}", "~","]", "\""]
def random_character():
    """
generate a random character out of usable characters
    """
    char_1 = random.choice(range(len(usable_characters)))
    return char_1
while True:
    use = input("do you want one (yes/no)").capitalize()
    if use != "Yes" and use != "No":
        continue
    elif use == "No":
        exit()
    characters = input("how manny characters do you want? 1 to 300: ")
    if characters.isdigit():
        characters = int(characters)
        if characters < 1 or characters > 300:
            print("you need to enter a number between 1 and 300")
            continue
    else:
        print("you need to enter a number")
        continue
    for i in range(characters):
        char = random_character()
        password.append(usable_characters[char])
    print("".join(password))
    password.clear()