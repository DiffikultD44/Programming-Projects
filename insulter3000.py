import random as r 
import sys as s

# Insulter 3000
# Variables
bodyParts = ["head", "feet", "hands", "nose", "ears", "forhead", "toes", "hair", "eyes", "legs"]
plural = [False, True, True, False, True, False, True, False, True, True]
senses = ["look", "sound", "smell", "feel", "taste"]
adjectives = ["gasoline", "poop", "vomit", "wet socks", "dirty underwear", "burnt marshmellows", "rotten eggs", "rainbow unicorns", "pepper spray", "radiation", "wet dog", "blood", "expired milk", "pee soup", "moldy cheese", "stale bread", "cigarette smoke", "sweaty gym socks", "fermented cabbage", "sour milk", "mildewed curtains", "dusty attic air", "plain oatmeal", "old socks", "soggy cereal", "garbage juice", "bruised banana", "slimy seaweed"]

print("type insult to be insulted, type end to end the program")
# the main loop
while True:
    

    command1 = input(">>> ")

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
        s.exit()
    else:
        print("===================")
        print("invalid command")
        print("===================")