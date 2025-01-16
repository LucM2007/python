while true:
    print("i will reverse the sentences you give me")
    play = input("do you want to play? (yes/no): ").capitalize()
    if play != "yes" or play != "no":
        print("you didn't enter yes or no")
        continue
    if play == "no":
        exit()
    sentence = input("enter a sentence: ")
    if sentence == "":
        print("you didn't enter a sentence")

    sentence_list = [sentence]
    for word in sentence_list:
        word = word.split()
        word.reverse()
        sentence_list = " ".join(word)
    print(sentence_list)