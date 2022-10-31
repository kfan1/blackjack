import random

import art

card_list = list("A23456789") + [10] + list("JQK")


def random_card():
    return str(random.choice(card_list))


def converter(card):
    if str(card) == "J" or str(card) == "Q" or str(card) == "K":
        return 10
    elif str(card) == "A":
        return 11  # need to find a way to return 1 or 11
    else:
        return int(str(card))

def aceorone(cardlist):
    numberlist = []
    for x in cardlist:
        numberlist.append(converter(x))
    if sum(numberlist) > 21:
        return str(1)
    else:
        return "A"



def blackjack(money):
    print(art.logo)
    bet = int(input("How much are you bidding? $"))
    while bet < 5:
        bet = int(input("Minimum bet is $5, please bid more. $ "))
    while money - bet < 0:
        bet = int(input("You don't have enough money, please bid less. $ "))
    money -= bet
    d1 = random_card()
    d2 = random_card()
    u1 = random_card()
    u2 = random_card()
    print(f"Your cards [{u1}, {u2}]")

    user_cards = [u1, u2]
    dealer_cards = [d1, d2]

    if u1 == "A":
        u1 = aceorone(user_cards)
    if u2 == "A":
        u2 = aceorone(user_cards)
    if d1 == "A":
        d1 = aceorone(dealer_cards)
    if d2 == "A":
        d2 = aceorone(dealer_cards)

#    print(f"!!!!!!Dealer's cards [{d1}, {d2}]!!!!!!")

    unum1 = converter(u1)
    unum2 = converter(u2)
    dnum1 = converter(d1)
    dnum2 = converter(d2)

    user_numbers = [unum1, unum2]
    dealer_numbers = [dnum1, dnum2]

    if dnum1 + dnum2 == 21 and unum1 + unum2 == 21:
        print(f"Dealer's cards [{d1}, {d2}]")
        print("It's a draw")
        money += bet
        return money
    elif dnum1 + dnum2 == 21:
        print(f"Dealer's cards [{d1}, {d2}]")
        print("You lose")
        return money
    elif unum1 + unum2 == 21:
        print("Blackjack! You win! (Blackjack pays out 1.5x)")
        print(f"Dealer's cards [{d1}, {d2}]")
        money += bet * 2.5
        return money

    print(f"Dealer's card [{d1}]")

    hit_or_stay = input("Hit? (y/n) ")
    while hit_or_stay == "y":
        u3 = random_card()
        unum3 = converter(u3)
        user_cards.append(u3)
        user_numbers.append(unum3)
        print("[" + ",".join(user_cards) + "]")
        if sum(user_numbers) > 21:
            if "A" in user_cards:
                for x in range(len(user_cards)):
                    if user_cards[x] == "A":
                        user_numbers[x] = 1
                        hit_or_stay = input("Hit? (y/n) ")
            else:
                print("You lose")
                print(f"Dealer's cards [{d1}, {d2}]")
                return money
        elif sum(user_numbers) == 21:
            hit_or_stay = "n"
        else:
            hit_or_stay = input("Hit? (y/n) ")


    while sum(dealer_numbers) < 17:
        d3 = random_card()
        dnum3 = converter(d3)
        dealer_cards.append(d3)
        dealer_numbers.append(dnum3)
        print(f"Dealer's cards " + "[" + ",".join(dealer_cards) + "]")
        if sum(dealer_numbers) > 21:
            if "A" in dealer_cards:
                for x in range(len(dealer_cards)):
                    if dealer_cards[x] == "A":
                        dealer_numbers[x] = 1
            else:
                print("You win!")
                money += bet * 2
                return money

    if sum(dealer_numbers) == sum(user_numbers):
        print(f"Dealer's cards " + "[" + ",".join(dealer_cards) + "]")
        print("It's a draw")
        money += bet
        return money

    if sum(dealer_numbers) > sum(user_numbers):
        print(f"Dealer's cards " + "[" + ",".join(dealer_cards) + "]")
        print("You lose")
        return money

    if sum(dealer_numbers) < sum(user_numbers):
        print(f"Dealer's cards " + "[" + ",".join(dealer_cards) + "]")
        print("You win!")
        money += bet * 2
        return money
