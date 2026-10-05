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
            
    