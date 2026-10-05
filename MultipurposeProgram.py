import random as r 
import sys as s
from datetime import datetime, date, time, timedelta
import time
import threading
#:7
((((((((((((((((((((((((((((((((((((((((((((((()))))))))))))))))))))))))))))))))))))))))))))))
#currently <24000 characters, <2450 words
while True:
    print("===================")
    print("=/AI\= made by AI")
    print("type 1 for INSULTER")
    print("type 2 for RANDOM NUMBER GENERATOR")
    print("type 3 for NUMBER GUESSER")
    print("type 4 for GAMBLING")
    print("type 5 for CASH REGISTER")
    print("type 6 for HANGMAN")
    print("type 7 to CHECK THE DATE AND TIME")
    print("type 8 to CHECK HOW LONG IS LEFT UNTIL PARALIVES COME OUT =/AI\= ")
    print("type 9 for THERAPIST")
    print("type 10 for PIG LATIN TRANSLATOR")
    print("type 11 for SEARCH AND REPLACE")
    print("type 12 for ROCK PAPER SCISSORS")
    print("type 13 for RANDOM NEWS HEADLINE =/AI\= ")
    print("type 14 for TEMPATURE CONVERTER")
    print("type 15 for STOCK MARKET GAME =/AI\=")
    print("type 16 for COIN FLIPPER")
    print("type 17 for PYTHAGOREAN THEOREM")
    print("type 18 for WEAPON ROLLING GAME")
    print("type 19 for PIRATE CAPTAIN NAME GENERATOR")
    print("type 20 for LIFE SIMULATION GAME")
    print("type 100 to EXIT")
    print("===================")
    command = int(input("what program do you want >>> "))

    #insulter 3000
    if command == 1:
        bodyParts = ["head", "feet", "hands", "nose", "ears", "forhead", "toes", "hair", "eyes", "legs", "shirt"]
        plural = [False, True, True, False, True, False, True, False, True, True, False]
        senses = ["look", "sound", "smell", "feel", "taste"]
        adjectives = ["gasoline", "poop", "vomit", "wet socks", "dirty underwear", "burnt marshmellows", "rotten eggs", "rainbow unicorns", "pepper spray", "radiation", "wet dog", "blood", "expired milk", "pea soup", "a graphics card"]

        print("type insult to be insulted, type end to end")

        while True:
            

            command1 = input("type>>> ")

            if command1 == "insult":
                part = r.choice(bodyParts)
                is_plural = plural[bodyParts.index(part)]
                sense = r.choice(senses) + ("s" if not is_plural else "")
                adj = r.choice(adjectives)
                print("===================")
                print("your %s %s like %s" %(part, sense, adj))
                print("===================")
            
            elif command1 == "end":
                print("see ya")
                #s.exit()
                break
            else:
                print("===================")
                print("invalid command")
                print("===================")

    #random number generator

    if command == 2:
        
        #intitialize 2 variables
        tries = 0
        rnumber = 0
        chosen_number2 = int(input("choose a number from 1 to 100 >>> "))
        #use a loop to generate a bunch of random numbers

        while True:
            rnumber = r.randint(1, 100)
            tries += 1
            print("Try #%d --> %d" %(tries, rnumber))
            #every while true loop needs a break in order to stop
            if rnumber == chosen_number2:
                print("you got your lucky number!")
                break
            

        print("it took %d tries to generate a %d" %(tries, chosen_number2))
        


    #number guesser

    if command == 3:
        number = r.randint(1, 100)
        guess_amount = 0


        while True:
            guess = int(input("guess a number from 1 to 100 >>>"))
            
            guess_amount += 1
            if guess > number:
                print("the number is smaller than %d" %guess)

            if guess < number:
                print("number is greater than %d" %guess)
            if guess == number:
                break
        print("correct! the number was %d, it took you %d guesses" %(number, guess_amount))
    

    #gambling
    
    if command == 4:
        money = 10        

        while True:
            
            money_won = 0
            number = r.randint(1, 2)

            print("=============")
            print("current money is $%d" %money)
            print("=============")

            bet_amount = int(input("choose how much you wanna bet >>> "))
            chosen_number = int(input("choose 1 or 2 >>> "))
            if chosen_number != 1 or chosen_number != 2:
                print("you can only pick 1 or 2")

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
                break
    
    #cash register

    if command == 5:
        #step 1: INPUT (Ask for things)
        words = ["first", "second", "third", "fourth", "fifth"]
        objects = []
        costs = []

        total = 0
        bought = ""
        while bought != "Q":
            bought = input(f"what did you buy? type 'Q' to end> ")
            if bought != "Q":
                objects.append(bought)
                costs.append(float(input("how much does it cost? > ")))
                total += costs[-1]


        


        #step 2: PROCESSING (calculate one or more things)

        # total = cost1 + cost2 + cost3 + cost4 + cost5
        tax = total / 13
        gtotal = total + tax


        #step 3: OUTPUT (Print the answer or answers)

        print("++++++++++++++")
        print("RECEIPT")
        print("++++++++++++++")
        for i in range(len(objects)):
            print("%s -------- %.2f" %(objects[i], costs[i]))
        # print("%s -------- %.2f" %(buy1, cost1))
        # print("%s -------- %.2f" %(buy2, cost2))
        # print("%s -------- %.2f" %(buy3, cost3))
        # print("%s -------- %.2f" %(buy4, cost4))
        # print("%s -------- %.2f" %(buy5, cost5))
        print("++++++++++++++")
        print("Subtotal: %.2f" %(total))
        print("Tax: %.2f" %(tax))
        print("Grand Total: %.2f" %(gtotal))
    

#hangman

    if command == 6:
        def print_word(word, guessed_letters):
            letters_to_print = [letter if letter in guessed_letters else "_" for letter in word]
            print(" ".join(letters_to_print))

        def is_finished(word, guessed_letters):
            for letter in word:
                if letter not in guessed_letters:
                    return False
            return True

        def is_letter(letter):
            return len(letter) == 1 and letter.lower() in "abcdefghijklmnopqrstuvwxyz"

        words = ["abruptly", "absurd", "abyss", "affix", "askew", "awkward", "blizzard", "buzzing", "crypt", "oxygen", "wizard", "zombie"]
        chosen_word = r.choice(words)
        guessed_letters = []

        max_attempts = 6
        wrong_guesses = 0

        while not is_finished(chosen_word, guessed_letters) and wrong_guesses < max_attempts:
            print_word(chosen_word, guessed_letters)
            user_input = input("Guess a letter > ").lower()

            if user_input == "gravy":
                print(f"The word is {chosen_word}")
                continue

            if is_letter(user_input):
                if user_input in guessed_letters:
                    print("You already guessed that letter!")
                else:
                    guessed_letters.append(user_input)
                    if user_input in chosen_word:
                        print("You guessed correctly!")
                    else:
                        wrong_guesses += 1
                        print(f"Wrong guess! You have {max_attempts - wrong_guesses} tries left.")
            else:
                print("That's not a letter, dummy!")

        # Win/Lose Screen
        if is_finished(chosen_word, guessed_letters):
            print("\n YOU WIN! ")
            print(f"The word was: {chosen_word}")
        else:
            print("\n YOU LOSE! ")
            print(f"The word was: {chosen_word}")
    #date and time

    if command == 7:
        current = datetime.now()
        year = current.year
        month = current.month
        day = current.day
        hour = current.hour
        minute = current.minute
        second = current.second
        microsecond = current.microsecond


        print("===================")
        print("currently it is %d, and its the %d month, the %d day of the week, and %d hour, the %d minute, the %d second, and the %d microsecond " %(year, month, day, hour, minute, second, microsecond))
        print("===================")


#paralives countdown

    if command == 8:
        
        start_date = datetime(2025, 11, 16)
        target_date = datetime(2026, 5, 25)

        running = True

        def colored_progress_bar(progress, length=20):
            filled = int(progress * length)
            unfilled = length - filled
            return (
                "[" +
                "\033[92m" + "#" * filled +
                "\033[91m" + "-" * unfilled +
                "\033[0m" +
                "]"
            )

        def bouncy_ball(frame, length=20):
            pos = frame % (2 * (length - 1))
            if pos >= length:
                pos = (2 * (length - 1)) - pos
            bar = ["-"] * length
            bar[pos] = "●"
            return "[" + "".join(bar) + "]"

        def format_time_breakdown(remaining_seconds):
            total_days = int(remaining_seconds // 86400)

            avg_month_days = 30.44
            months = int(total_days // avg_month_days)

            days_after_months = int(total_days - months * avg_month_days)

            weeks = days_after_months // 7
            days = days_after_months % 7

            hours = int((remaining_seconds % 86400) // 3600)
            minutes = int((remaining_seconds % 3600) // 60)
            seconds = int(remaining_seconds % 60)

            return months, weeks, days, hours, minutes, seconds

        def countdown():
            global running
            frame = 0

            # pre-calc the full length of the entire countdown
            total_seconds = (target_date - start_date).total_seconds()

            if total_seconds <= 0:
                print("Error: Start date must be before target date.")
                running = False
                return

            while running:
                now = datetime.now()

                if now > target_date:
                    s.stdout.write("\r\033[K")
                    s.stdout.flush()
                    print("Day already passed.")
                    running = False
                    break

                remaining_seconds = (target_date - now).total_seconds()
                progress = 1 - (remaining_seconds / total_seconds)

                months, weeks, days, hours, minutes, secs = format_time_breakdown(remaining_seconds)

                color_bar = colored_progress_bar(progress, length=25)
                bounce_bar = bouncy_ball(frame, length=18)

                out = (
                    
                    f"Countdown to PARALIVES: "
                    f"{months}=MONTHS {weeks}=WEEKS {days}=DAYS | "
                    #f"{hours:02d}h:{minutes:02d}m:{secs:02d}s left | "
                    f"{color_bar} {bounce_bar}"
                )

                s.stdout.write("\r" + out + "\033[K")
                s.stdout.flush()

                frame += 1
                time.sleep(0.1)

            

        def wait_for_end():
            global running
            while running:
                try:
                    user_input = input()
                except EOFError:
                    running = False
                    break
                if user_input.strip().lower() == "end":
                    running = False
                    break

        threading.Thread(target=countdown, daemon=True).start()
        wait_for_end()
    if command == 9:
        input("Why are you here today? >>> ")
        while True:
            answer = input("And how does that make you feel? >>> ")

            if answer == "end":
                break
    
    if command == 10:
         #making a enligsh to pig latin converter
        vowels = ["a", "e", "i", "o", "u"]
        while True:
            word = input("Enter a word, or exit to exit > ")

            firstLetter = word[0]
            if firstLetter in vowels:
                pigLatin = word + "ay"
                print(pigLatin)
            else:
                newWord = word[1:]
                pigLatin = newWord + firstLetter + "ay"
                print(pigLatin)
            if word == "exit":
                break
    if command == 11:
        #ask user for sentence, then ask what word they wanna replace, then ask what its replaced with

        sentence = input("Enter a sentence >>> ")
        word = input("Enter a word to replace >>> ")
        replacingWord = input("What do you wanna replace it with >>> ")

        newSentence = sentence.replace(word, replacingWord)

        print(newSentence)
    if command == 12:
        pcScore = 0
        score = 0
        elements = ["rock", "paper", "scissors"]
        while True:
            #rock paper scissors
            chosen = input("choose ROCK, PAPER, or SCISSORS; or end to end >>> ")
            pcChosen = r.choice(elements)
            if chosen == pcChosen:
                print("its a draw")
            if chosen == "rock" and pcChosen == "paper":
                pcScore += 1
                print("you chose %s, and the pc chose %s. YOU LOSE" %(chosen, pcChosen))
            if chosen == "paper" and pcChosen == "rock":
                score += 1
                print("you chose %s, and the pc chose %s. YOU WIN" %(chosen, pcChosen))
            if chosen == "scissors" and pcChosen == "rock":
                pcScore += 1
                print("you chose %s, and the pc chose %s. YOU LOSE" %(chosen, pcChosen))
            if chosen == "rock" and pcChosen == "scissors":
                score += 1
                print("you chose %s, and the pc chose %s. YOU WIN" %(chosen, pcChosen))
            if chosen == "paper" and pcChosen == "scissors":
                pcScore += 1
                print("you chose %s, and the pc chose %s. YOU LOSE" %(chosen, pcChosen))
            if chosen == "scissors" and pcChosen == "paper":
                score += 1
                print("you chose %s, and the pc chose %s. YOU WIN" %(chosen, pcChosen))
            if chosen == "end":
                break
            print("PC %d - %d YOU" %(pcScore, score))
        
    if command == 13:
        #random news headline
        import urllib.request
        import xml.etree.ElementTree as ET
        import random

        def get_random_rss_headline(rss_url):
            try:
                # Added a User-Agent header to prevent the server from blocking the request
                req = urllib.request.Request(rss_url, headers={'User-Agent': 'Mozilla/5.0'})
                
                with urllib.request.urlopen(req) as response:
                    xml_data = response.read()

                root = ET.fromstring(xml_data)
                headlines = []
                for item in root.findall(".//item"):
                    title = item.find("title").text
                    if title:
                        headlines.append(title)

                if headlines:
                    print(">!COULD POTENTIALLY BE INNAPROPRIATE!<")
                    print(f"\n[HOT NEWS] {r.choice(headlines)}")
                else:
                    print("\nNo headlines found in the feed.")

            except Exception as e:
                print(f"\nAn error occurred: {e}")

        if __name__ == "__main__":
            # Updated 2025 RSS URL
            url = "https://feeds.bbci.co.uk/news/rss.xml"
            
            print("---News---")
            print("Commands: 'news' for a headline, 'end' to quit.")

            while True:
                user_input = input("\ntype news for news, and end to end >>> ").lower().strip()

                if user_input == "news":
                    get_random_rss_headline(url)
                elif user_input == "end":
                    print("Goodbye!")
                    break
                else:
                    print("Unknown command. Please type 'news' or 'end'.")
    if command == 14:
        while True:
            command3 = input("enter 'c' for CELCIUS or 'f' for FARENHEIT. type 'end; to end >>> ")
            if command3 == "c":
                temp = int(input("enter celsius temp >>> "))
                farenheit = (temp * 9/5) + 32
                print("%.0d°f" %farenheit)
            elif command3 == "f":
                temp = int(input("enter farenheit temp >>> "))
                celcius = (temp - 32) * 5/9
                print("%.0d°c" %celcius)
            if command3 == "end":
                break
    if command == 15:
    
        
        # Game Variables
        CASH = 1000.00
        SHARES = 0
        STOCK_PRICE = 50.00
        TICKER = "DFKD" # Generic company ticker

        def display_status():
            """Prints the current game status."""
            print("\n" + "="*40)
            print(f"PORTFOLIO STATUS:")
            print(f"Cash: ${CASH:,.2f}")
            print(f"Shares of {TICKER}: {SHARES}")
            print(f"Current Stock Price: ${STOCK_PRICE:.2f}")
            total_value = CASH + (SHARES * STOCK_PRICE)
            print(f"Total Portfolio Value: ${total_value:,.2f}")
            print("="*40)

        def buy_shares():
            """Handles buying stock."""
            global CASH, SHARES
            try:
                amount = int(input(f"How many shares of {TICKER} would you like to buy? "))
                cost = amount * STOCK_PRICE
                if cost <= CASH:
                    CASH -= cost
                    SHARES += amount
                    print(f"Purchased {amount} shares for ${cost:.2f}.")
                else:
                    print("Not enough cash to make this purchase.")
            except ValueError:
                print("Invalid input. Please enter a whole number.")

        def sell_shares():
            """Handles selling stock."""
            global CASH, SHARES
            try:
                amount = int(input(f"How many shares of {TICKER} would you like to sell? "))
                if amount <= SHARES:
                    CASH += amount * STOCK_PRICE
                    SHARES -= amount
                    print(f"Sold {amount} shares.")
                else:
                    print("Not enough shares to sell.")
            except ValueError:
                print("Invalid input. Please enter a whole number.")

        def update_price():
            """Randomly changes the stock price to simulate market volatility."""
            global STOCK_PRICE
            # Price changes randomly by -2 to +2 dollars
            change = r.uniform(-2, 2)
            STOCK_PRICE += change
            if STOCK_PRICE < 1: # Prevents price from going below zero
                STOCK_PRICE = 1
            print(f"\nMarket update: {TICKER} price changed by ${change:,.2f}.")

        # Main game loop
        if __name__ == "__main__":
            print("Welcome to the Python Stock Market Simulator!")
            
            
            while True:
                print("Type 'status', 'buy', 'sell', 'quit', or 'next' to advance time.")
                command = input("\nEnter command: ").lower().strip()

                if command == "quit":
                    print("Game over.")
                    display_status()
                    break
                elif command == "status":
                    display_status()
                elif command == "buy":
                    buy_shares()
                elif command == "sell":
                    sell_shares()
                elif command == "next":
                    update_price()
                    display_status()
                else:
                    print("Unknown command. Please use 'status', 'buy', 'sell', 'quit', or 'next'.")
    if command == 16:
        import random

        #flips coin to get highest streak
        streak = 1
        lastflip = None
        attempts = 0
        highestStreak = 1
        choice = input("do you want to choose a goal of what streak to get, or see what the higherst you can get is? [goal, highest] >>> ")
        if choice == "goal":
            goal = int(input("What streak to you want to get to >>> "))
            while True:
                attempts += 1
                flip = random.randint(1, 2)
                
                if flip == lastflip:
                    streak += 1
                elif flip != lastflip:
                    streak = 1
                    print("streak broken")
                if flip == 1:
                    print("HEADS")
                    
                else:
                    print("TAILS")
                print("attempt #%d" %attempts)
                print("streak : %d" %streak)
                if streak == goal:
                    print("done")
                    input("press enter to continue")
                    break
                
                lastflip = flip
        if choice == "highest":
            limit = int(input("how many attempts do you want? >>> "))
            while True:
                attempts += 1
                flip = random.randint(1, 2)
                
                if flip == lastflip:
                    streak += 1
                elif flip != lastflip:
                    streak = 1
                    print("streak broken")
                if flip == 1:
                    print("HEADS")
                    
                else:
                    print("TAILS")
                print("attempt #%d" %attempts)
                print("streak : %d" %streak)
                if streak > highestStreak:
                    highestStreak = streak

                
                lastflip = flip
                if attempts == limit:
                    print("highest streak: %d" %highestStreak)
                    input("press enter to continue")
                    break
    if command == 17:
        import math
        #calculate side C
        a = float(input("Enter A >>> "))
        b = float(input("Enter B >>> ")) 
        print("Equation: %.2f^2 + %.2f^2 = C^2" %(a, b))

        solution1 = ((a**2) + (b**2))
        solution2 = (math.sqrt(solution1))
        print("C = %.2f" %solution2)
        input("Enter to continue >>> ")
    
    if command == 18:
        import random
        #roll a weapon of random rarity (wooden, bronze, iron, gold, diamond, etc), diffrent type (eg. sword, bow, rapier, shield, etc)
        pweapons = []
        weights=[80, 60, 30, 20, 5, 0.1]
        rarity = ["Wooden", "Bronze", "Iron", "Gold", "Diamond", "GODLY"]
        #rarity = [1, 2, 3, 4, 5]
        weapons = ["shortsword", "longsword", "bow", "dagger", "rapier", "shield", "cutlass"]
        removing = ["Wooden, Bronze"]
        while True:
            chosen1 = random.choices(rarity, weights)[0]
            chosen2 = random.choice(weapons)
            createdweapon = ("%s %s" %(chosen1, chosen2))
            pweapons.append(createdweapon)
            print("======================")
            print("%s was created" %createdweapon)
            print("======================")
            input("Press 'enter' to roll again >>> ")

    if command == 19:
        while True:
            description = ["Black", "Green", "Red", "Blue", "Seashell", "Fish", "Seaweed", "Barnacle"]
            item = ["Beard", "Boot", "Jacket", "Hat"]
            chosendescription = r.choice(description)
            chosenitem = r.choice(item)
            print("Captain %s%s" %(chosendescription, chosenitem))
            chosen = input("Type end to end, or [enter] to continue >>> ")
            if chosen == "end":
                break
    if command == 20:
        import random
        import time
        import sys
        #life sim #:7
        #####SETUP#####
        date = 0
        choosing = True
        drinks = ["drank Coffee", "drank Tea", "drank Water", "drank Orange Juice", "drank Apple Juice", "drank Milk", "drank Hot Chocolate", "drank Lemonade", "drank Cola", "drank Iced Tea"]
        food = ["ate Burger", "ate Pizza", "ate Sandwich", "ate Pasta", "ate Salad", "ate Soup", "ate Fries", "ate Tacos", "ate Rice", "ate Pancakes"]
        names = ["Aiden", "Luna", "Marcus", "Ivy", "Rowan", "Caleb", "Nova", "Elias", "Freya", "Julian", "Willow", "Theo", "Aria", "Mason", "Hazel", "Leo", "Daphne", "Silas", "Quinn", "Aurora", "Jasper", "Maya", "Nolan", "Elodie", "Finn", "Sienna", "Victor", "Lyra", "Owen", "Zara", "Ryan", "Sydney"]

        lastname = "Unknown"
        name = []
        lastnames = []
        buildings = []
        building = []
        chosen0 = input("Do you want to make your own people, or generate? [make, generate] >>> ")
        if chosen0 == "make":
            amount = int(input("How many people do you want? (min 2)>>> "))
            if amount < 2:
                sys.exit()
            for x in range(amount):
                chosenname = input("What do you want your person to be named? >>> ")
                name.append(chosenname)
            lastname = input("What do you want their last name to be? >>> ")
        if chosen0 == "generate":
            lastnames = ["Smith", "Johnson", "Walker", "Bennett", "Carter", "Reynolds", "Parker", "Collins", "Anderson", "Hughes", "Turner", "Mitchell", "Hayes", "Brooks", "Foster", "Morrison", "Sullivan", "Price", "Hamilton", "Reed", "Watson", "Bell", "Cooper", "Ward", "Murphy", "Bailey", "Rivera", "Lopez", "Kim", "Patel"]
            amount = random.randint(1, 7)
            for x in range(amount):
                name.append(random.choice(names))
                lastname = random.choice(lastnames)
        residence = ("%s residence" %lastname)
        print("You will live at %s" %residence)
        print("here is you list of residents:")
        for x in range(amount):
            print(name[x], lastname)

        chosen1 = input("Do you want to choose name of buildings, or randomly generate? [choose, generate] >>> ")
        if chosen1 == "choose":
            while choosing == True:
                chosenbuilding = input("What do you want to name the building, or 'end' to continue. eg[Town Hall, St. Michael church, Drunk Pig Bar, Jim's Burgers, etc...] >>> ")
                building.append(chosenbuilding)
                if chosenbuilding == "end":
                    choosing = False
        if chosen1 == "generate":
            buildings = ["Drunk Goose Bar", "Sleep Tite Motel", "Fat Joe Burgers", "Rusty Anchor Tavern", "Neon Moon Arcade", "Golden Kettle Café", "Broken Clock Antiques", "Lucky Lantern Noodles", "Wandering Fox Inn", "Midnight Owl Books", "Cracked Bell Pub", "Sunny Side Laundromat", "Iron Horse Garage", "Blue Harbor Fish & Chips", "Dusty Trail Outfitters", "Velvet Rose Lounge", "Cornerstone Hardware", "Paper Crane Stationery", "Foggy Window Diner", "Silver Pike Smokehouse", "Maple Street Market", "Starfall Cinema", "Crooked Nail Workshop", "Moonbeam Bakery", "Last Stop Convenience", "Thistle & Thorn Florist", "Red Brick Records", "Hollow Creek Lodge", "Electric Sparrow Café", "Old Mill Supply", "Laughing Badger Pub", "Sleepy Hollow Hostel", "Copper Spoon Deli", "Three Crowns Barbershop", "Lazy River Bait & Tackle", "Whiskey Barrel Saloon", "Sunset Ridge Motel", "Busted Lantern Brewery", "Pinecone Pantry", "Crimson Fox Tavern", "Dust & Ash Pawnshop", "Golden Hour Photography", "Worn Leather Boot Shop", "Midtown Repair Co.", "Clover Patch Grocers", "Tin Can Arcade", "Moonrise Tea House", "Back Alley Ramen", "North Star Outfitters", "Rattletrap Auto Parts", "Blue Door Bookshop", "Gravel Road Diner", "Firefly Music Hall", "Crooked River Canoes", "Sleepy Bear Daycare", "Hearthstone Bakery", "Iron Key Locksmith", "Rainy Day Thrift", "Hawk & Hammer Tools", "Last Light Observatory"]
            buildingamount = random.randint(10, 58)
            for x in range(buildingamount):
                building.append(random.choice(buildings))
            print("%d buildings in the city" %buildingamount)
        if len(building) == 0:
            print("No buildings exist.")
            sys.exit()
        chosen3 = input("Auto or manual time progress? [manual, auto] >>> ")
        #####SIMULATION#####
        print("----------SIMULATION START----------")
        while True:
            print("---day %d---" %date)
            date += 1
            if chosen3 == "auto":
                time.sleep(random.randint(3, 7))
            death = random.randint(1, 10) 
            if len(name) == 1:
                print("%s got depressed from being alone" %(name[0]))
                name.remove(name[0])
            if death == 4:
                deadperson = random.choice(name)
                name.remove(deadperson)
                print("💀-%s HAD DIED-💀" %deadperson)
            if death == 3:
                born = random.choice(names)
                name.append(born)
                print("-----%s WAS BORN------" %born)
            if len(name) == 0:
                print("Everyone has died")
                break
            person = random.choice(name)
            place = random.choice(building)
            action = random.randint(1, 2)
            if action == 1:
                action = str(random.choice(food))
            else:
                action = str(random.choice(drinks))
            company = random.randint(1, 2)
            if company == 1:
                company = str("")
            else:
                withperson = random.choice(name)
                company = str("with %s" %withperson)
            print("%s went to %s and %s %s" %(person, place, action, company))
            if date == 365 or date == 730 or date == 1095:
                print("------HAPPY NEW YEAR------")
            if chosen3 == "manual":
                chosen2 = input("press ENTER to continue >>> ")
                if chosen2 == "":
                    pass
                elif chosen2 == "die":
                    name.remove(name[0])
            
    

        
#end
    if command == 100:
        print("come back soon")
        s.exit()