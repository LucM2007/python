"""
here you can play blackjack
"""
import random


def deal_card():
    """"
    deals the cards
    """
    global cards_in_play
    card = random.choice(cards_in_play)
    cards_in_play.remove(card)
    return card


def get_points():
    """
    Calculates the points of the player and dealer
    """
    global player_points
    global dealer_points
    player_points = 0
    dealer_points = 0

    player_numbers.clear()
    dealer_numbers.clear()

    for card in player_hand:
        # Splits the card details to extract its value
        card_value = card.split()[0]
        player_numbers.append(card_value)
    for card in dealer_hand:
        card_value = card.split()[0]
        dealer_numbers.append(card_value)

    for value in player_numbers:
        if value == "A" and player_points <= 10:
            player_points += 11
        elif value == "A" and player_points >= 11:
            player_points += 1
        elif value in ["J", "Q", "K"]:
            player_points += 10
        else:
            player_points += int(value)
    for value in dealer_numbers:
        if value == "A" and dealer_points <= 10:
            dealer_points += 11
        elif value == "A" and dealer_points >= 11:
            dealer_points += 1
        elif value in ["J", "Q", "K"]:
            dealer_points += 10
        else:
            dealer_points += int(value)


def start():
    """"
    initializes the game
    """
    for k in range(2):
        cards_2 = deal_card()
        player_hand.append(cards_2)
    cards_3 = deal_card()
    dealer_hand.append(cards_3)
    get_points()

print("Welcome to blackjack!")
balance = 1000
bet = 0
while True:
    cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    suits = ["hearts", "diamonds", "spades", "clubs"]
    cards_in_play = []
    player_points = 0
    dealer_points = 0
    next_dealer_card = []
    play = input("do you want to play (yes/no)").capitalize()
    if play != "Yes" and play != "No":
        continue
    elif play == "No":
        exit()
    print(f"your balance is {balance}")
    print(f"your bet is {bet}")
    if balance == 0 and bet == 0:
        print("you went broke and lost all your money")
        exit()
    print(f'your balance is {balance}')
    bet = input("how much do you want to bet? ")
    if not bet.isdigit():
        print("please enter a valid number")
        continue
    else:
        bet = int(bet)
        if bet > balance:
            print("you don't have enough money")
            continue
        elif bet <= 0:
            print("please enter a valid number")
        balance -= bet

    player_hand = []
    player_numbers = []
    dealer_numbers = []
    dealer_hand = []
    for i in range(len(suits)):
        cards_in_play.append(f"A of {suits[i]}")
        cards_in_play.append(f"A of {suits[i]}")
#       for j in range(len(cards)):
#            cards_in_play.append(f"{cards[j]} of {suits[i]}")
    start()
    while True:

        print(dealer_hand, dealer_points)
        print(player_hand, player_points)
        if len(player_numbers) == 2 and player_points == 21:
            bet *= 2.5
            balance += bet
            print("you win you have blackjack")
            break
        if len(dealer_numbers) == 1 and dealer_points == 11:
            insurance = input(f"do you want to insure your bet? this would be {bet / 2} (yes/no)").capitalize()
            if insurance != "Yes" and insurance != "No":
                continue
            elif insurance == "Yes":
                amount = bet / 2
                balance -= amount
                print(f"you have insured your bet and now have {balance}")
                dealer_insurance = deal_card()
                dealer_hand.append(dealer_insurance)
                get_points()
                print(dealer_hand, dealer_points)
                if dealer_points == 21:
                    print("you're insurance won")
                    amount *= 3
                    balance += amount
                    break
                else:
                    print("you're insurance did not win")
        if len(dealer_numbers) == 2 and dealer_points == 21:
            print("you lose dealer has blackjack")
            bet = 0
            break
        do = input("do you want to hit or stand (hit/stand/double)").capitalize()
        if do != "Hit" and do != "Stand" and do != "Double":
            continue
        elif do == "Hit":
            cards_4 = deal_card()
            player_hand.append(cards_4)
            get_points()
            print(player_hand)
            print(player_points)
            if player_points > 21:
                print("you bust!")
                bet = 0
                break
            else:
                continue
        elif do == "Double" or do == "Stand":
            if do == "Double":
                balance -= bet
                bet *= 2
                cards_5 = deal_card()
                player_hand.append(cards_5)
                get_points()
                print(cards_5)
            for i in range(100):
                if dealer_points < 17:
                    cards = deal_card()
                    dealer_hand.append(cards)
                    get_points()
                    print(cards, "to the dealers hand")
            print(dealer_hand, "with a total of", dealer_points)
            print(player_hand, "with a total of", player_points)


        if player_points == 21:
            bet *= 2
            print("You win!")
        elif dealer_points == 21:
            bet = 0
            print("You lose!")
        elif player_points > 21:
            bet = 0
            print("You bust!")
        elif dealer_points > 21:
            bet *= 2
            print("You win!")
        elif player_points < dealer_points:
            bet = 0
            print("You lose!")
        elif player_points > dealer_points:
            bet *= 2
            print("You win!")
        else:
            print("its a tie")
        balance += bet
        bet = 0
        break