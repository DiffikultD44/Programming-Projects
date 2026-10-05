import random as r
import sys as s

money = 10

while True:
    
    money_won = 0
    number = r.randint(1, 2)

    print("=============")
    print("current money is $%d" %money)
    print("=============")

    bet_amount = int(input("choose how much you wanna bet >>> "))
    chosen_number = int(input("choose 1 or 2 >>> "))

    if bet_amount > money:
        print("YOU CANT AFFORD THAT")
    
    if bet_amount <= money:
        if chosen_number == number:
            money_won = bet_amount * 2
            money = money + money_won
            print("=============")
            print("you won $%d" %money_won)
            print("congrats, you now have $%d" %money)
            print("=============")
        if chosen_number != number:
            money = money - bet_amount
            print("=============")
            print("you lost $%d" %bet_amount)
            print("you now have $%d" %money)
            print("=============")

    


    

    if money <= 0:
        print("=============")
        print("you lost all your money ¯\_(ツ)_/¯")
        print("=============")
        s.exit()
