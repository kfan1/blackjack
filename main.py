import blackjack

money = 5
lets_go = input("Do you want to play a game of Blackjack? Press enter to continue, type 'n' to quit ")
if lets_go == "":
    money = int(input("How much money do you have? (minimum bid is $5) $"))
if money < 5:
    print("You're broke")
    lets_go = "n"

while lets_go == "":
    if money < 5:
        print("You're broke")
        break
    money = blackjack.blackjack(money)
    print(f"You have ${money} left")
    lets_go = input("Do you want to play another round? Press enter to continue, type 'n' to quit ")
