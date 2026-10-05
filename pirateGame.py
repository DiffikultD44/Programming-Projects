import random as r
import sys as s
import time
shipName = input("Name your ship >>> The ")
roll = 0
die = 0
skeletonsKilled = 0
voyages = 0
money = 0
earnedmoney = 0
crewroster = ["Jack", "Edward", "Anne", "Mary", "William", "Henry", "Grace", "Francis", "Thomas", "Samuel", "James", "Richard", "Jimothy"]
crew = []
islands = ["Cannon Cove", "Crescent Isle", "Lone Cove", "Mermaid's Hideaway", "Sailor's Bounty", "Smugglers' Bay", "Wanderers Refuge", "Crook's Hollow", "Devil's Ridge", "Discovery Ridge", "Plunder Valley", "Shark Bait Cove", "Snake Island", "Thieves' Haven", "Kraken's Fall", "Marauder's Arch", "Old Faithful Isle", "Shipwreck Bay", "The Crooked Masts", "The Sunken Grove"]
chosen = input("Would you like to make your own pirates or generate? [make, generate] >>> ")
if chosen == "make":
    amount = int(input("How large is your crew? [3-10] >>> "))
    if amount > 10 or amount < 3:
        print("invalid amount")
        s.exit()
    for x in range(amount):
        piratename = input("%d - What is the pirate named? >>> " %x)
        crew.append(piratename)
        if piratename in crewroster:
            crewroster.remove(piratename)
if chosen == "generate":
    amount = r.randint(3, 10)
    for x in range(amount):
        piratename = r.choice(crewroster)
        crew.append(piratename)
        crewroster.remove(piratename)
print("Crew of %s" %amount)
for x in range(amount):
    print(crew[x]) 


#gameplay
while True:
    typed = input("[enter] to continue, or [end] to forfeit your crew>>> ")
    if typed == "end":
        crew.clear()
    earnedmoney = 0
    roll = r.randint(1, 2)
    if len(crew) == 0:
        print("Your crew is no more...")
        print("==========================================")
        print("total money earned = %d" %money)
        print("total amount of voyages sailed = %d" %voyages)
        print("total skeletons slain = %d" %skeletonsKilled)
        print("==========================================")
        s.exit()

    if roll == 1:
        voyages += 1
        #treaure
        island = r.choice(islands)
        print("The %s sails to %s to hunt for treasure" %(shipName, island))
        while True:
            streak = r.randint(1, 2)
            print(("your pirates found a chest! $1000"))
            earnedmoney += 1000
            if streak == 1:
                print("your earned $%d from this voyage" %earnedmoney)
                money += earnedmoney
                break
            print("digging...")
            time.sleep(r.randint(1, 5))
    if roll == 2:
        voyages += 1
        #skeleton hunting
        
        island = r.choice(islands)
        print("The %s sails to %s to hunt some skeletons" %(shipName, island))
        while True:
            die = r.randint(1, 10)
            streak = r.randint(1, 2)
            print(("your pirates killed a skeleton! $1500"))
            earnedmoney += 1500
            skeletonsKilled += 1
            if streak == 1:
                print("your earned $%d from this voyage" %earnedmoney)
                money += earnedmoney
                break
            if die == 4:
                deadpirate = r.choice(crew)
                print("%s died while fighting a skeleton" %deadpirate)
                crew.remove(deadpirate)
            print("fighting...")
            time.sleep(r.randint(1, 5))