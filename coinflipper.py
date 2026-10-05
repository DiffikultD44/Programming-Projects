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
            break